# [Claude docs changes for October 9th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/a03cac3a3aee5b3f6a553fcbb640282179d85cea) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/a03cac3a3aee5b3f6a553fcbb640282179d85cea)]

## Executive Summary
- Claude Managed Agents gain **dynamic workflows** (beta): an agent can write a program that runs many agents in phases and combines their results. Two new pages cover workflow runs and session threads.
- Claude Code 2.1.295 adds `onFailure: "block"` for command and HTTP hooks, so a hook that fails to start, times out, or exits unexpectedly blocks the action instead of letting it through.
- Elicitation hooks are now documented in full: they can accept, decline, or cancel an MCP form request without a dialog, with a complete script example.
- The 1M context window docs were reworked. Fable, Sonnet 5+, and Opus 4.7+ run with 1M by default, including on Bedrock, Vertex, Foundry, and the Claude apps gateway, and `[1m]` is now only needed for Opus 4.6 and Sonnet 4.6.
- The API docs add per-request Haiku 5.5 long-prompt pricing details, workspace rate-limit `source`/inheritance details, and new Haiku 5.5 breaking-change notes.

## New Claude Code versions

### [2.1.295](https://github.com/gpambrozio/ClaudeDocs/blob/a03cac3a3aee5b3f6a553fcbb640282179d85cea/versions/2.1.295.md)

#### New features

* Added `onFailure: "block"` for command and HTTP hooks: a hook that can't start, times out, or exits with an unexpected code now blocks the action
* Added Program Status Protocol (OSC 7501) support so terminals can show whether Claude Code is working, waiting, or done
* Added `$.ui.notify` for mods, and children (strings and `Text`) for a mod's `Button`
* Added an optional `models` list to every Claude apps gateway upstream (with `*` wildcard), plus `timeouts.upstream_ttfb_ms` for cloud upstreams and an `upstream_request_id` in the `inference` audit event
* Added `forceLoginMethod: "gateway"` and `forceLoginGatewayUrl` in user settings on machines with no managed settings
* Added `CLAUDE_CODE_RETRY_WATCHDOG_MAX_WAIT_MS` to cap how long unattended retry mode waits out 429/529 errors
* Added a warning for `claude plugin install`, `enable`, `disable` and `marketplace add` when the target settings file does not load, and install-line advice in `claude plugin validate`
* Added quoted text to the `/copy` picker
* [VSCode] Added a chat row for files Claude sends you, which opens them in the editor

#### Existing feature improvements

* Token counts behind a Claude apps gateway on Bedrock now use AWS's CountTokens API (requires `bedrock:CountTokens`)
* Background requests behind a Claude apps gateway now use Haiku 4.5, falling back to the session model
* The gateway logs a warning every 30 seconds while its PostgreSQL database is read-only
* Headless `rate_limit_event` warnings now say whether extra usage is on
* MCP tool descriptions loaded through tool search are now cut at 16,384 characters (was 2,048)
* Subagents preload at most 32 skills from the `skills` field
* claude.ai connectors negotiate MCP protocol version 2026-07-28 by default (`MCP_PROTOCOL_NEGOTIATION=legacy` opts out)
* WebSocket MCP servers now close the connection on messages over 16 MiB
* Grep now runs searches sent with `-l`, `-c` or `-r` instead of failing
* Ctrl+C at the idle prompt of an attached background session leaves a pending `/loop` wakeup alone

#### Major bug fixes

* Fixed every request failing on a `[1m]` model when a gateway, Bedrock, Vertex or Foundry refuses the context-1m beta
* Fixed `claude -p` text output dropping earlier responses when background work started another turn
* Fixed remote MCP servers staying disconnected after outages in headless/SDK sessions, and reconnect loops now back off up to 30s
* Fixed `--tools` and `--restricted` not applying to built-in tools that register after launch
* Fixed SessionStart hook issues: repeated async context on resume, and `CLAUDE_ENV_FILE` variables not reaching Bash after `/resume` or `/branch`
* Fixed a skill's `allowed-tools` and `effort` being dropped in `-p` runs
* Fixed terminal freezes on very long responses, deeply nested quotes, and syntax highlighting of pathological code
* Fixed a tampered server-managed settings cache making a user's own plugin count as organization-managed
* Fixed `/model`, `/fast`, `/output-style` and auto-update channel changes bypassing a plugin's `config.set` hook
* Fixed a mod's `prompt.submit` rewrite still being saved to history as typed

-----

## Claude Code changes

### New Documents

None.

### Changed documents

#### [claude-apps-gateway](https://github.com/gpambrozio/ClaudeDocs/blob/a03cac3a3aee5b3f6a553fcbb640282179d85cea/docs-md/claude-code/claude-apps-gateway.md) [[Source](https://code.claude.com/docs/en/claude-apps-gateway)]

* Feature table now lists the 1M token context window as available, with Fable, Sonnet 5+, and Opus 4.7+ using 1M by default. [[line 468](https://github.com/gpambrozio/ClaudeDocs/blob/a03cac3a3aee5b3f6a553fcbb640282179d85cea/docs-md/claude-code/claude-apps-gateway.md?plain=1#L468)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway#availability-and-limitations)]

#### [discover-plugins](https://github.com/gpambrozio/ClaudeDocs/blob/a03cac3a3aee5b3f6a553fcbb640282179d85cea/docs-md/claude-code/discover-plugins.md) [[Source](https://code.claude.com/docs/en/discover-plugins)]

* New "Add and install from your shell" section: `claude plugin install <plugin> --marketplace <source>` adds the marketplace without confirmation (v2.1.292+), alongside the in-session form (v2.1.275+). [[lines 207-229](https://github.com/gpambrozio/ClaudeDocs/blob/a03cac3a3aee5b3f6a553fcbb640282179d85cea/docs-md/claude-code/discover-plugins.md?plain=1#L207-L229)] [[Source](https://code.claude.com/docs/en/discover-plugins#add-a-marketplace-and-install-in-one-command)]
* Note that the official marketplace isn't registered on a machine where no interactive session has run, so install scripts must add it first. [[line 170](https://github.com/gpambrozio/ClaudeDocs/blob/a03cac3a3aee5b3f6a553fcbb640282179d85cea/docs-md/claude-code/discover-plugins.md?plain=1#L170)] [[Source](https://code.claude.com/docs/en/discover-plugins#install-from-your-shell)]

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/a03cac3a3aee5b3f6a553fcbb640282179d85cea/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* New `CLAUDE_CODE_OVERLOADED_RETRY_BASE_DELAY_MS` (backoff start for 529 errors) and `CLAUDE_CODE_RETRY_WATCHDOG_MAX_WAIT_MS`.
* `CLAUDE_ASYNC_AGENT_STALL_TIMEOUT_MS` now also covers workflow agents (v2.1.286+).
* `CLAUDE_CODE_DISABLE_1M_CONTEXT` reworded: removes `[1m]` variants and holds default-1M models to 200K.
* `CLAUDE_CODE_DISABLE_ATTACHMENTS` is ignored in project and local settings.

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/a03cac3a3aee5b3f6a553fcbb640282179d85cea/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* Added the 529 retry base-delay variable to the retry-tuning table, and clarified stalled-stream re-streaming.
* Updated the background-session "stopped before first response" explanation and recovery steps.
* Clarified marketplace-name conflict wording for `--marketplace` installs and model-fallback notes on the cyber safeguards message.

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/a03cac3a3aee5b3f6a553fcbb640282179d85cea/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* Elicitation hooks: new table of how to accept, decline, cancel, or defer to the dialog; exit code 2 and top-level `decision: "block"` also decline; a decline from any hook wins. [[lines 3404-3430](https://github.com/gpambrozio/ClaudeDocs/blob/a03cac3a3aee5b3f6a553fcbb640282179d85cea/docs-md/claude-code/hooks.md?plain=1#L3404-L3430)] [[Source](https://code.claude.com/docs/en/hooks#elicitation-output)]
* New "Answer a form request from a script" worked example with settings entry and script. [[line 3359](https://github.com/gpambrozio/ClaudeDocs/blob/a03cac3a3aee5b3f6a553fcbb640282179d85cea/docs-md/claude-code/hooks.md?plain=1#L3359)] [[Source](https://code.claude.com/docs/en/hooks#elicitation)]
* Exit code 2 on Elicitation now declines the request with no dialog; `decision` was ignored for Elicitation hooks from v2.1.105 until v2.1.284. [[lines 857-1002](https://github.com/gpambrozio/ClaudeDocs/blob/a03cac3a3aee5b3f6a553fcbb640282179d85cea/docs-md/claude-code/hooks.md?plain=1#L1002)] [[Source](https://code.claude.com/docs/en/hooks#exit-code-2-behavior-per-event)]
* SessionStart output reorganized, with a new "Reload skills that a hook installs" section and a note that plugin-supplied `initialUserMessage`/`sessionTitle` need the plugin installed before the session starts. [[lines 1134-1175](https://github.com/gpambrozio/ClaudeDocs/blob/a03cac3a3aee5b3f6a553fcbb640282179d85cea/docs-md/claude-code/hooks.md?plain=1#L1134-L1175)] [[Source](https://code.claude.com/docs/en/hooks#sessionstart-decision-control)]
* WebFetch input gains an `offset` field (v2.1.290+). [[line 1703](https://github.com/gpambrozio/ClaudeDocs/blob/a03cac3a3aee5b3f6a553fcbb640282179d85cea/docs-md/claude-code/hooks.md?plain=1#L1703)] [[Source](https://code.claude.com/docs/en/hooks#webfetch)]
* TaskCreated, TaskCompleted and TeammateIdle inputs gain an `agent_id` field (v2.1.290+). [[line 2438](https://github.com/gpambrozio/ClaudeDocs/blob/a03cac3a3aee5b3f6a553fcbb640282179d85cea/docs-md/claude-code/hooks.md?plain=1#L2438)] [[Source](https://code.claude.com/docs/en/hooks#taskcreated-input)]

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/a03cac3a3aee5b3f6a553fcbb640282179d85cea/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Servers can set `_meta["anthropic/alwaysLoad"]` on a tool to load it upfront; a user's `alwaysLoad: false` can defer all of a server's tools (new "Defer a server's tools" section). [[lines 1408-1505](https://github.com/gpambrozio/ClaudeDocs/blob/a03cac3a3aee5b3f6a553fcbb640282179d85cea/docs-md/claude-code/mcp.md?plain=1#L1408-L1505)] [[Source](https://code.claude.com/docs/en/mcp#for-mcp-server-authors)]
* Servers can mark a tool as requiring approval on every call with `_meta["anthropic/requiresUserInteraction"]`. [[line 1308](https://github.com/gpambrozio/ClaudeDocs/blob/a03cac3a3aee5b3f6a553fcbb640282179d85cea/docs-md/claude-code/mcp.md?plain=1#L1308)] [[Source](https://code.claude.com/docs/en/mcp#require-approval-for-a-specific-tool)]
* Response size limit for HTTP and SSE servers, and HTTP/stdio/claude.ai connectors now probe for the newer MCP revision. [[lines 320-1240](https://github.com/gpambrozio/ClaudeDocs/blob/a03cac3a3aee5b3f6a553fcbb640282179d85cea/docs-md/claude-code/mcp.md?plain=1#L1240)] [[Source](https://code.claude.com/docs/en/mcp#mcp-client-runtimes)]

#### [microsoft-foundry](https://github.com/gpambrozio/ClaudeDocs/blob/a03cac3a3aee5b3f6a553fcbb640282179d85cea/docs-md/claude-code/microsoft-foundry.md) [[Source](https://code.claude.com/docs/en/microsoft-foundry)]

* New "1M token context window" section: default 1M for Fable, Sonnet 5+, and Opus 4.7+ when Claude Code can identify the deployment's model (via `modelOverrides`); Opus/Sonnet 4.6 need `[1m]`.

#### [model-config](https://github.com/gpambrozio/ClaudeDocs/blob/a03cac3a3aee5b3f6a553fcbb640282179d85cea/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* Extended context rewritten: 1M is the default on supported models across Anthropic API, Bedrock, Vertex, Foundry and gateway; new sections for selecting 1M on Opus/Sonnet 4.6, context window behind an LLM gateway, and turning off 1M.
* Model fallback: fallback model now depends on which model refused; new "Ask before switching" behavior and a first-time prompt to switch automatically; `switchModelsOnFlag` semantics clarified.
* Server-managed settings delivery requirements reworded for API-key fleets.

#### [ultrareview](https://github.com/gpambrozio/ClaudeDocs/blob/a03cac3a3aee5b3f6a553fcbb640282179d85cea/docs-md/claude-code/ultrareview.md) [[Source](https://code.claude.com/docs/en/ultrareview)]

* PR mode requires a `github.com` repository (use the no-argument form for GitHub Enterprise Server), uses the connected GitHub account, and can post findings as a single PR comment (v2.1.227+). [[lines 47-92](https://github.com/gpambrozio/ClaudeDocs/blob/a03cac3a3aee5b3f6a553fcbb640282179d85cea/docs-md/claude-code/ultrareview.md?plain=1#L47-L92)] [[Source](https://code.claude.com/docs/en/ultrareview#review-a-pull-request)]
* Too-large repositories prompt you to use PR mode; `claude ultrareview` fallback behavior documented. [[line 150](https://github.com/gpambrozio/ClaudeDocs/blob/a03cac3a3aee5b3f6a553fcbb640282179d85cea/docs-md/claude-code/ultrareview.md?plain=1#L150)] [[Source](https://code.claude.com/docs/en/ultrareview#run-ultrareview-non-interactively)]

#### [workflows](https://github.com/gpambrozio/ClaudeDocs/blob/a03cac3a3aee5b3f6a553fcbb640282179d85cea/docs-md/claude-code/workflows.md) [[Source](https://code.claude.com/docs/en/workflows)]

* New "When an agent stalls and restarts" section: stalled agents restart up to five times, the `stallMs` option, error messages for each failure mode, and how failures propagate. [[lines 400-423](https://github.com/gpambrozio/ClaudeDocs/blob/a03cac3a3aee5b3f6a553fcbb640282179d85cea/docs-md/claude-code/workflows.md?plain=1#L400-L423)] [[Source](https://code.claude.com/docs/en/workflows#when-an-agent-stalls-and-restarts)]
* `agent()` resolves to `null` if stopped or on unrecoverable API error; `pipeline()` keeps the `null`. [[line 305](https://github.com/gpambrozio/ClaudeDocs/blob/a03cac3a3aee5b3f6a553fcbb640282179d85cea/docs-md/claude-code/workflows.md?plain=1#L305)] [[Source](https://code.claude.com/docs/en/workflows#what-the-saved-script-looks-like)]

#### [plugins/mods/troubleshoot](https://github.com/gpambrozio/ClaudeDocs/blob/a03cac3a3aee5b3f6a553fcbb640282179d85cea/docs-md/claude-code/plugins/mods/troubleshoot.md) [[Source](https://code.claude.com/docs/en/plugins/mods/troubleshoot)]

* New entries: remote "rollout switch" turning mods off, `session.start ran again in a fresh copy`, `ui.render ... threw while drawn`, `the module failed without a message`, and "A toast doesn't appear" diagnostics. [[lines 25-192](https://github.com/gpambrozio/ClaudeDocs/blob/a03cac3a3aee5b3f6a553fcbb640282179d85cea/docs-md/claude-code/plugins/mods/troubleshoot.md?plain=1#L25-L192)] [[Source](https://code.claude.com/docs/en/plugins/mods/troubleshoot#check-whether-mods-can-load)]
* Hot-reload transcript lines for `--plugin-dir` mods are described. [[line 260](https://github.com/gpambrozio/ClaudeDocs/blob/a03cac3a3aee5b3f6a553fcbb640282179d85cea/docs-md/claude-code/plugins/mods/troubleshoot.md?plain=1#L260)] [[Source](https://code.claude.com/docs/en/plugins/mods/troubleshoot#read-the-debug-log)]

-----

## API changes

### New Documents

#### [managed-agents/session-threads](https://github.com/gpambrozio/ClaudeDocs/blob/a03cac3a3aee5b3f6a553fcbb640282179d85cea/docs-md/api/managed-agents/session-threads.md) [[Source](https://platform.claude.com/docs/en/managed-agents/session-threads)]

Beta guide to the threads of a multiagent session (managed-agents-2026-04-01). It covers listing, interrupting, and archiving threads, reading their events, how session status and the shared session budget aggregate across threads, and tool permission handling across them. Threads created by workflow runs are covered as well. This largely splits out content previously in the multiagent orchestration page.

#### [managed-agents/workflow-runs](https://github.com/gpambrozio/ClaudeDocs/blob/a03cac3a3aee5b3f6a553fcbb640282179d85cea/docs-md/api/managed-agents/workflow-runs.md) [[Source](https://platform.claude.com/docs/en/managed-agents/workflow-runs)]

Beta guide to dynamic workflows. An agent writes a workflow, a program that runs many agents in phases and combines their results, and the server runs it in the background as a workflow run. It explains run layers (run, phases, threads), run states and events on the session event stream, what a run blocks, when work is done, budgets, and limits.

### Changed documents

#### [about-claude/pricing](https://github.com/gpambrozio/ClaudeDocs/blob/a03cac3a3aee5b3f6a553fcbb640282179d85cea/docs-md/api/about-claude/pricing.md) [[Source](https://platform.claude.com/docs/en/about-claude/pricing)]

* Haiku 5.5 long-prompt pricing is per request, and the 100K-token threshold counts cache reads and writes; the US-only inference 1.1x multiplier also applies to the higher prices. [[lines 158-222](https://github.com/gpambrozio/ClaudeDocs/blob/a03cac3a3aee5b3f6a553fcbb640282179d85cea/docs-md/api/about-claude/pricing.md?plain=1#L222)] [[Source](https://platform.claude.com/docs/en/about-claude/pricing#data-residency-pricing)]
* Tool token overhead tables updated: bash tool 325 tokens for Claude 4.7+ and Mythos Preview; `text_editor_20250728` 974/745 tokens. [[lines 277-321](https://github.com/gpambrozio/ClaudeDocs/blob/a03cac3a3aee5b3f6a553fcbb640282179d85cea/docs-md/api/about-claude/pricing.md?plain=1#L277-L324)] [[Source](https://platform.claude.com/docs/en/about-claude/pricing#bash-tool)]
* Claude 4.7+ and Mythos Preview use a newer tokenizer producing about 30% more tokens for the same text; Google Cloud regional endpoints apply only to Sonnet 4.6 and earlier. [[line 512](https://github.com/gpambrozio/ClaudeDocs/blob/a03cac3a3aee5b3f6a553fcbb640282179d85cea/docs-md/api/about-claude/pricing.md?plain=1#L512)] [[Source](https://platform.claude.com/docs/en/about-claude/pricing#how-is-token-usage-calculated)]

#### [agents-and-tools/tool-use/advisor-tool](https://github.com/gpambrozio/ClaudeDocs/blob/a03cac3a3aee5b3f6a553fcbb640282179d85cea/docs-md/api/agents-and-tools/tool-use/advisor-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool)]

* Examples switched to Haiku 5.5 and agent loops now break on non-`tool_use` stop reasons; guidance on handling `max_tokens`. [[line 779](https://github.com/gpambrozio/ClaudeDocs/blob/a03cac3a3aee5b3f6a553fcbb640282179d85cea/docs-md/api/agents-and-tools/tool-use/advisor-tool.md?plain=1#L779)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool#mid-conversation-nudge-for-under-calling-executors)]
* Notes that `clear_thinking` with a `keep` value other than `all` causes advisor cache misses, and that Managed Agents support an advisor via the agent's configuration. [[lines 1389-1815](https://github.com/gpambrozio/ClaudeDocs/blob/a03cac3a3aee5b3f6a553fcbb640282179d85cea/docs-md/api/agents-and-tools/tool-use/advisor-tool.md?plain=1#L1389)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool#advisor-side-caching)]

#### [build-with-claude/claude-on-vertex-ai](https://github.com/gpambrozio/ClaudeDocs/blob/a03cac3a3aee5b3f6a553fcbb640282179d85cea/docs-md/api/build-with-claude/claude-on-vertex-ai.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai)]

* Java SDK updated to 2.71.0, with the Vertex client example now configuring Google credentials, region, and project explicitly. [[lines 49-77](https://github.com/gpambrozio/ClaudeDocs/blob/a03cac3a3aee5b3f6a553fcbb640282179d85cea/docs-md/api/build-with-claude/claude-on-vertex-ai.md?plain=1#L49-L77)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai#install-an-sdk-for-accessing-agent-platform)]

#### [build-with-claude/compaction-threshold](https://github.com/gpambrozio/ClaudeDocs/blob/a03cac3a3aee5b3f6a553fcbb640282179d85cea/docs-md/api/build-with-claude/compaction-threshold.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/compaction-threshold)]

* New example using `pause_after_compaction` to keep recent messages (without thinking blocks) after the compaction block. [[lines 2877-2967](https://github.com/gpambrozio/ClaudeDocs/blob/a03cac3a3aee5b3f6a553fcbb640282179d85cea/docs-md/api/build-with-claude/compaction-threshold.md?plain=1#L2877-L2985)] [[Source](https://platform.claude.com/docs/en/build-with-claude/compaction-threshold#examples)]

#### [manage-claude/rate-limits-api](https://github.com/gpambrozio/ClaudeDocs/blob/a03cac3a3aee5b3f6a553fcbb640282179d85cea/docs-md/api/manage-claude/rate-limits-api.md) [[Source](https://platform.claude.com/docs/en/manage-claude/rate-limits-api)]

* Workspace limit values now carry `source` (workspace override vs. inherited from the organization), and the workspace endpoint can optionally include inherited values; `org_limit` documented. [[lines 156-482](https://github.com/gpambrozio/ClaudeDocs/blob/a03cac3a3aee5b3f6a553fcbb640282179d85cea/docs-md/api/manage-claude/rate-limits-api.md?plain=1#L156)] [[Source](https://platform.claude.com/docs/en/manage-claude/rate-limits-api#key-concepts)]

#### [managed-agents/multiagent-orchestration](https://github.com/gpambrozio/ClaudeDocs/blob/a03cac3a3aee5b3f6a553fcbb640282179d85cea/docs-md/api/managed-agents/multiagent-orchestration.md) [[Source](https://platform.claude.com/docs/en/managed-agents/multiagent-orchestration)]

* Restructured around subagents, dynamic workflows, and the advisor, with a comparison table and instructions to turn on dynamic workflows; thread details moved to session-threads. [[lines 21-90](https://github.com/gpambrozio/ClaudeDocs/blob/a03cac3a3aee5b3f6a553fcbb640282179d85cea/docs-md/api/managed-agents/multiagent-orchestration.md?plain=1#L21-L90)] [[Source](https://platform.claude.com/docs/en/managed-agents/multiagent-orchestration#hand-work-to-other-agents)]

#### [managed-agents/tools-web-restrictions](https://github.com/gpambrozio/ClaudeDocs/blob/a03cac3a3aee5b3f6a553fcbb640282179d85cea/docs-md/api/managed-agents/tools-web-restrictions.md) [[Source](https://platform.claude.com/docs/en/managed-agents/tools-web-restrictions)]

* In multiagent sessions, domain lists from the session agent, the listed agent, and the tool combine: `allowed_domains` must be covered by all lists, `blocked_domains` add together. Empty intersections make every call fail with `url_not_allowed`. [[lines 460-489](https://github.com/gpambrozio/ClaudeDocs/blob/a03cac3a3aee5b3f6a553fcbb640282179d85cea/docs-md/api/managed-agents/tools-web-restrictions.md?plain=1#L460-L489)] [[Source](https://platform.claude.com/docs/en/managed-agents/tools-web-restrictions#multiagent-and-outcome-driven-sessions)]

#### [release-notes/overview](https://github.com/gpambrozio/ClaudeDocs/blob/a03cac3a3aee5b3f6a553fcbb640282179d85cea/docs-md/api/release-notes/overview.md) [[Source](https://platform.claude.com/docs/en/release-notes/overview)]

* October 9, 2026 entry announcing dynamic workflows for Managed Agents (beta). [[line 15](https://github.com/gpambrozio/ClaudeDocs/blob/a03cac3a3aee5b3f6a553fcbb640282179d85cea/docs-md/api/release-notes/overview.md?plain=1#L15)] [[Source](https://platform.claude.com/docs/en/release-notes/overview#october-9-2026)]
* Haiku 5.5 migration warning expanded: `temperature`, `top_p`, `top_k`, assistant prefill, and `computer_20250124` can return 400 errors. [[line 27](https://github.com/gpambrozio/ClaudeDocs/blob/a03cac3a3aee5b3f6a553fcbb640282179d85cea/docs-md/api/release-notes/overview.md?plain=1#L27)] [[Source](https://platform.claude.com/docs/en/release-notes/overview#october-7-2026)]

#### [api/beta](https://github.com/gpambrozio/ClaudeDocs/blob/a03cac3a3aee5b3f6a553fcbb640282179d85cea/docs-md/api/api/beta.md) [[Source](https://platform.claude.com/docs/en/api/beta)]

* Beta API reference (and per-endpoint pages for agents, deployments, environments, files, memory stores and more) now documents an optional `anthropic-version` header on each endpoint.
