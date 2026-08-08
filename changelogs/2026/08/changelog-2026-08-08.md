# [Claude docs changes for August 8th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/f96cccaca0e58c6043fb23015911c76c5158857e) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/f96cccaca0e58c6043fb23015911c76c5158857e)]

## Executive Summary
- New cross-session messaging lets a Claude Code session discover and message your other independent sessions — directly on the same machine, or reply-only to sessions on other machines and Claude Code on the web via Remote Control — via new `ListAgents`/`SendMessage` tools, the `/list-agents` command, and settings (`crossSessionInbound`, `isolatePeerMachines`) to control it.
- Auto mode becomes the default permission mode for new Claude Code sessions on Pro, Max, and Team plans starting August 14, 2026 (existing user- or org-set defaults are preserved).
- Claude Managed Agents gains session budgets (hard spend caps that pause a session with `budget_reached`), session advisors (a mid-turn consultation model added to a session's roster), `inference_geo` pinning at the agent level, and skill discovery from a mounted GitHub repository's `.claude/skills` directory.
- New `claude import` / `/import [codex|gemini]` command migrates configuration — CLAUDE.md content, MCP servers, commands, subagents, and skills — from Codex or Gemini into Claude Code.
- Claude Code 2.1.225 fixes several reliability issues, including a transient 401 that could replace a long-lived `CLAUDE_CODE_OAUTH_TOKEN` and break headless sessions until restart, and intermittent MCP OAuth failures on macOS after a keychain read timeout.

## New Claude Code versions

### [2.1.225](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/versions/2.1.225.md)

#### New features

* Added gateway spend-limit support to Claude Code's usage warning; the limit-reached message now names the cap, its reset time, and the operator's message (requires the gateway on 2.1.225)
* Added a workspace trust prompt to `claude agents` for untrusted directories, matching the behavior of `claude`
* SendMessage can now start a conversation with your Remote Control sessions on other machines by name (`ListAgents` shows them as `name [ref]`), instead of only replying after they message you first

#### Existing feature improvements

* Improved Remote Control: photos attached from the Claude app are now shown to Claude directly instead of being read from disk with a separate tool call
* SendMessage: a Remote Control recipient you already confirmed is never swapped for a same-named session on this machine when its own list couldn't be checked

#### Major bug fixes

* Fixed a transient 401 replacing a long-lived `CLAUDE_CODE_OAUTH_TOKEN` with a stored login's short-lived token, breaking headless sessions until restart
* Fixed MCP OAuth servers on macOS intermittently failing with a burst of 401 errors, as if never authenticated, after a keychain read timed out
* Fixed auto mode counting a safety-filter refusal of its own permission check toward the consecutive-block limit; the action is still denied, but the model is now told to move on rather than retry
* Fixed cross-session messages staying parked without a notice or expiry in headless sessions and during startup
* Fixed conversation history breaking on Remote Control session resume after very large conversations were compacted
* Fixed hovering over a session in another project in the agents list changing the directory the next agent starts in
* Fixed `claude self-hosted-runner` registering and then failing every session when `--base-dir` cannot be created or written; it now exits at startup with a clear error
* Fixed Claude Code on the web sessions being misreported as stuck, re-sending a growing event backlog on every reconnect
* [VSCode] Fixed Focus view folding away the latest to-do list, a pending question's context, and settled answers; thinking-only folds show "Thought for Ns" and re-collapse when their turn completes

### [2.1.226](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/versions/2.1.226.md)

#### Major bug fixes

* Bug fixes and reliability improvements (no further detail provided)

-----

## Claude Code changes

### New Documents

#### [agent-sdk/examples](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/agent-sdk/examples.md) [[Source](https://code.claude.com/docs/en/agent-sdk/examples)]

New page routing to complete, runnable Agent SDK example projects and guided Claude Cookbook recipes. Links the `claude-agent-sdk-demos` GitHub repo for TypeScript demos (from an email client to a multi-agent research system), the Claude Cookbook's Agent SDK Python notebook series (a progression from a one-liner research agent to sophisticated multi-agent systems), and the Agent SDK quickstart / minimal "Hello World" project for starting from scratch.

#### [cross-session-messaging](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/cross-session-messaging.md) [[Source](https://code.claude.com/docs/en/cross-session-messaging)]

New page documenting cross-session messaging (requires Claude Code v2.1.224+, macOS/Linux only), which lets Claude use new `ListAgents` and `SendMessage` tools to discover and message a user's *other* independent Claude Code sessions — directly via a per-session inbox socket on the same machine, or reply-only to sessions on other machines/Claude Code on the web via Remote Control. It covers message delivery semantics (delivered/held/refused), the `crossSessionInbound` and `isolatePeerMachines` settings for controlling inbound/outbound messages, safety guarantees (a message never grants consent or changes config), and platform/provider availability limits.

### Changed documents

#### [agent-sdk/agent-loop](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/agent-sdk/agent-loop.md) [[Source](https://code.claude.com/docs/en/agent-sdk/agent-loop)]

* `bypassPermissions` mode description now notes the cross-session messaging safeguards still apply even in this mode. [[line 198](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/agent-sdk/agent-loop.md?plain=1#L198)] [[Source](https://code.claude.com/docs/en/agent-sdk/agent-loop#permission-mode)]

#### [agent-sdk/cost-tracking](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/agent-sdk/cost-tracking.md) [[Source](https://code.claude.com/docs/en/agent-sdk/cost-tracking)]

* `total_cost_usd`/`usage` fields in the Python SDK are now documented as optionally `None` on some error paths. [[lines 43, 251](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/agent-sdk/cost-tracking.md?plain=1#L43)]
* The 5-minute default prompt-cache TTL now also explicitly applies when authenticating via Claude Platform on AWS. [[line 264](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/agent-sdk/cost-tracking.md?plain=1#L264)] [[Source](https://code.claude.com/docs/en/agent-sdk/cost-tracking#track-cache-tokens)]
* New clarification: subscription users only get the automatic 1-hour cache TTL "within included usage"; once drawing on usage credits the SDK drops to a 5-minute TTL unless `ENABLE_PROMPT_CACHING_1H` is set. [[line 306](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/agent-sdk/cost-tracking.md?plain=1#L306)] [[Source](https://code.claude.com/docs/en/agent-sdk/cost-tracking#extend-the-prompt-cache-ttl-to-one-hour)]

#### [agent-sdk/permissions](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/agent-sdk/permissions.md) [[Source](https://code.claude.com/docs/en/agent-sdk/permissions)]

* `bypassPermissions` mode section updated: cross-session messaging safeguards still apply; subagent inheritance note now mentions the `isolatePeerMachines` approval requirement for cross-machine messages. [[lines 101, 230-238](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/agent-sdk/permissions.md?plain=1#L230-L238)]

#### [agent-sdk/sessions](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/agent-sdk/sessions.md) [[Source](https://code.claude.com/docs/en/agent-sdk/sessions)]

* `persistSession: false` is now clarified as TypeScript-only; Python has no equivalent (use `CLAUDE_CODE_SKIP_PROMPT_HISTORY` instead). [[line 18](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/agent-sdk/sessions.md?plain=1#L18)] [[Source](https://code.claude.com/docs/en/agent-sdk/sessions#choose-an-approach)]
* Session resume cross-directory lookup behavior expanded into explicit bullets ("Cross-directory lookup", "Same machine only"); notes that before v2.1.223 lookup was scoped only to the current project directory and its worktrees, and older SDK-bundled CLIs still behave that way. [[lines 254-264, 375-378](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/agent-sdk/sessions.md?plain=1#L254-L264)]

#### [agent-sdk/typescript](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* `peer` origin type documentation expanded: a cross-session peer can now be on another of the user's machines or on Claude Code on the web (via Remote Control), not just a local process; a one-way cross-machine reply has no reply address and `from` resolves to `"unknown"`. [[lines 1465-1476](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L1465-L1476)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#sdkmessageorigin)]

#### [agent-teams](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/agent-teams.md) [[Source](https://code.claude.com/docs/en/agent-teams)]

* Cross-references cross-session messaging as the tool for separate sessions passing messages without forming a team. [[line 20](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/agent-teams.md?plain=1#L20)] [[Source](https://code.claude.com/docs/en/agent-teams#when-to-use-agent-teams)]
* "Messages between agents" section: the no-consent/no-relay rules now explicitly extend to cross-session messages, not just teammates; auto-mode classifier behavior restated as two distinct checks. [[lines 234-241](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/agent-teams.md?plain=1#L234-L241)] [[Source](https://code.claude.com/docs/en/agent-teams#permissions)]
* Removed the specific "5-6 tasks per teammate" sizing guidance sentence. [[line 309](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/agent-teams.md?plain=1#L309)] [[Source](https://code.claude.com/docs/en/agent-teams#choose-an-appropriate-team-size)]
* Troubleshooting section restructured: "Teammates stopping on errors" renamed to "Agents stopping early" and merged with the former separate "Lead shuts down before work is done" section. [[lines 360-368](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/agent-teams.md?plain=1#L360-L368)] [[Source](https://code.claude.com/docs/en/agent-teams#too-many-permission-prompts)]

#### [agent-view](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/agent-view.md) [[Source](https://code.claude.com/docs/en/agent-view)]

* `/fork` behavior clarified: after forking, the two conversations are independent by default, but in sessions with cross-session messaging enabled, either side's Claude can now explicitly message the other. [[lines 305-309](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/agent-view.md?plain=1#L305-L309)] [[Source](https://code.claude.com/docs/en/agent-view#send-the-session-to-the-background)]

#### [agents](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/agents.md) [[Source](https://code.claude.com/docs/en/agents)]

* Now lists three (previously two) coordination-support tools, adding cross-session messaging alongside worktrees and `/batch`. [[lines 10-15](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/agents.md?plain=1#L10-L15)] [[Source](https://code.claude.com/docs/en/agents)]
* "Do the workers need to talk to each other?" guidance updated to mention cross-session messaging as an option for separate sessions. [[line 33](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/agents.md?plain=1#L33)] [[Source](https://code.claude.com/docs/en/agents#choose-an-approach)]

#### [amazon-bedrock](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/amazon-bedrock.md) [[Source](https://code.claude.com/docs/en/amazon-bedrock)]

* New `ANTHROPIC_BEDROCK_REGION_PREFIX` environment variable introduced as an alternative to pinning model IDs, letting users set a preferred cross-region inference-profile prefix while keeping the built-in default models. [[lines 184-192](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/amazon-bedrock.md?plain=1#L184-L192)] [[Source](https://code.claude.com/docs/en/amazon-bedrock#4-pin-model-versions)]
* New "Cross-region inference profile prefixes" section (requires v2.1.224+): documents the default prefix per AWS region (`us-gov.`, `us.`, `eu.`, `apac.`, `global.`), valid override values, the resolution order Claude Code follows when it can vs. can't list inference profiles in the account, and that GovCloud always forces `us-gov.` regardless of the variable. [[lines 257-296](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/amazon-bedrock.md?plain=1#L257-L296)] [[Source](https://code.claude.com/docs/en/amazon-bedrock#startup-model-checks)]

#### [auto-mode-config](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/auto-mode-config.md) [[Source](https://code.claude.com/docs/en/auto-mode-config)]

* New announcement: starting August 14, 2026, auto mode becomes the default permission mode for new sessions on Pro, Max, and Team plans (user- or org-set defaults are preserved). [[line 2](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/auto-mode-config.md?plain=1#L2)] [[Source](https://code.claude.com/docs/en/auto-mode-config)]

#### [channels](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/channels.md) [[Source](https://code.claude.com/docs/en/channels)]

* The list of checks that still prompt under `--dangerously-skip-permissions` in a channels session expands from 3 to 5 items, adding "removals targeting `/` or your home directory" and the cross-session messaging safeguards. [[lines 281-291](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/channels.md?plain=1#L281-L291)] [[Source](https://code.claude.com/docs/en/channels#quickstart)]

#### [claude-apps-gateway-config](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/claude-apps-gateway-config.md) [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config)]

* `${file:/path}` reference must now be the entire field value, not embedded in a longer string like `postgres_url`. [[line 32](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/claude-apps-gateway-config.md?plain=1#L32)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config#secret-expansion)]
* `public_url` requirement changed from "required behind a proxy" to "required unless `host` is loopback," including when TLS terminates at the gateway itself; boot now fails without it in that case. [[line 44](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/claude-apps-gateway-config.md?plain=1#L44)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config#listen)]
* `allowed_groups` matching clarified as exact, case-sensitive string comparison with no nested-group expansion. [[line 58](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/claude-apps-gateway-config.md?plain=1#L58)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config#oidc)]
* `ca_cert_pem` clarified to require the literal PEM content, not a file path (use `${file:...}` to load from a mounted file). [[line 72](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/claude-apps-gateway-config.md?plain=1#L72)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config#oidc)]
* `postgres_url`: schema migrations now explicitly run "at boot and on upgrade," not just boot. [[line 89](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/claude-apps-gateway-config.md?plain=1#L89)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config#store)]
* Bedrock "Model access" row rewritten: model access is now enabled by default in commercial regions; the remaining gate is Anthropic's one-time AWS Organizations use-case form. [[line 162](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/claude-apps-gateway-config.md?plain=1#L162)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config#amazon-bedrock)]
* `upstream_model` map behavior clarified: for built-in Claude models, an upstream omitted from the map still serves the model with the provider's default ID; only a fully custom model `id` skips upstreams missing from its map. [[lines 286, 307](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/claude-apps-gateway-config.md?plain=1#L286)]
* `fail_closed_on_error` now requires an `admin:` block configured; the gateway refuses to start if set `true` without one. [[line 351](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/claude-apps-gateway-config.md?plain=1#L351)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config#enforcement)]
* New note: each `upstream_model` key must match a configured upstream's `name`, or boot fails. [[line 369](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/claude-apps-gateway-config.md?plain=1#L369)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config#models)]
* New requirement: `telemetry.forward_to` URLs must use `https://`, with a narrow loopback exception gated by `CLAUDE_GATEWAY_ALLOW_LOOPBACK=1`. [[line 576](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/claude-apps-gateway-config.md?plain=1#L576)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config#telemetry)]
* New telemetry detail: a signed-in CLI with OTLP export enabled sends exports to the gateway even without a configured `forward_to` destination for that signal, which the gateway then silently discards. [[line 591](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/claude-apps-gateway-config.md?plain=1#L591)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config#telemetry)]
* `CLAUDE_GATEWAY_LOG_LEVEL` gains a new `debug` level that also logs id_token claim names, for diagnosing `groups_claim`/`email_claim` config. [[line 620](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/claude-apps-gateway-config.md?plain=1#L620)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config#complete-example)]

#### [claude-apps-gateway-deploy](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/claude-apps-gateway-deploy.md) [[Source](https://code.claude.com/docs/en/claude-apps-gateway-deploy)]

* Removed documentation of the "Anthropic-operated public gateway endpoints" exemption from the private-network deployment requirement. [[line 10](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/claude-apps-gateway-deploy.md?plain=1#L10)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-deploy)]
* Audit event list expanded: new `device.callback` event; new `admin.limit.upsert` and `admin.limit.delete` events; `admin.denied` now distinguishes `invalid_key`, `bearer_rejected`, and `no_credentials` reasons. [[line 95](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/claude-apps-gateway-deploy.md?plain=1#L95)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-deploy#logs)]
* Database role requirement simplified to "rights to create and alter tables" (removed the old pre-create-schema-for-DDL-restricted-roles guidance); concurrent gateway replicas now serialize schema migrations via a Postgres advisory lock during rolling upgrades. [[line 142](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/claude-apps-gateway-deploy.md?plain=1#L142)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-deploy#postgres)]
* SSRF loopback guard clarified: `CLAUDE_GATEWAY_ALLOW_LOOPBACK=1` also skips a boot-time check of cloud-metadata-endpoint reachability. [[line 171](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/claude-apps-gateway-deploy.md?plain=1#L171)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-deploy#threat-model-summary)]
* Troubleshooting table updated to match the removed public-endpoint exemption and the new DDL-rights guidance. [[lines 211-234](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/claude-apps-gateway-deploy.md?plain=1#L211-L234)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-deploy#troubleshooting)]

#### [claude-apps-gateway-on-aws](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/claude-apps-gateway-on-aws.md) [[Source](https://code.claude.com/docs/en/claude-apps-gateway-on-aws)]

* `public_url` requirement updated to "required for any non-loopback bind." [[line 251](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/claude-apps-gateway-on-aws.md?plain=1#L251)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-on-aws#deploy-the-gateway)]
* SSRF guard clarified: the gateway now rejects an IP-literal loopback telemetry URL (e.g. `http://127.0.0.1:4318`) at boot, not just at send time. [[line 259](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/claude-apps-gateway-on-aws.md?plain=1#L259)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-on-aws#deploy-the-gateway)]

#### [claude-apps-gateway-on-gcp](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/claude-apps-gateway-on-gcp.md) [[Source](https://code.claude.com/docs/en/claude-apps-gateway-on-gcp)]

* Reworded architecture description: the internal Application Load Balancer is now something the operator provides; the walkthrough configures the gateway for it but doesn't create it. [[line 273](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/claude-apps-gateway-on-gcp.md?plain=1#L273)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-on-gcp#deploy-the-gateway)]
* Deploy command changed: added `--max-instances=8`; changed `--ingress=internal-and-cloud-load-balancing` to `--ingress=internal`; new guidance to keep `max-instances × store.max_connections` below the Cloud SQL tier's connection limit. [[lines 300-311](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/claude-apps-gateway-on-gcp.md?plain=1#L300-L311)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-on-gcp#next-steps)]
* Clarifies `internal` Cloud Run ingress works with or without an internal ALB in front, so `internal-and-cloud-load-balancing` is no longer needed for either topology on this page. [[lines 318-321](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/claude-apps-gateway-on-gcp.md?plain=1#L318-L321)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-on-gcp#next-steps)]

#### [claude-apps-gateway-spend-limits](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/claude-apps-gateway-spend-limits.md) [[Source](https://code.claude.com/docs/en/claude-apps-gateway-spend-limits)]

* New documented behavior: spend caps reset on UTC calendar boundaries (daily 00:00 UTC, weekly Monday 00:00 UTC, monthly 1st 00:00 UTC). [[line 343](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/claude-apps-gateway-spend-limits.md?plain=1#L343)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-spend-limits#related)]
* `GET /v1/organizations/spend_limits` gains a new `scope_type` filter query param. [[line 352](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/claude-apps-gateway-spend-limits.md?plain=1#L352)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-spend-limits#related)]
* `/audit` endpoint gains `after_id` pagination, default limit 100. [[lines 358, 381](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/claude-apps-gateway-spend-limits.md?plain=1#L358)]

#### [claude-apps-gateway](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/claude-apps-gateway.md) [[Source](https://code.claude.com/docs/en/claude-apps-gateway)]

* Removed the "Anthropic-operated public gateway endpoints" exemption text (matches claude-apps-gateway-deploy.md). [[line 393](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/claude-apps-gateway.md?plain=1#L393)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway#next-steps)]
* HTTPS prerequisite clarified: plain `http://` is accepted only when the host is literally `localhost`/`127.0.0.1`/`::1`. [[line 403](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/claude-apps-gateway.md?plain=1#L403)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway#next-steps)]
* Boot sequence log example updated: now shows a "waiting for migration lock" line and one "migration N applied" line per schema migration on a fresh database. [[lines 431-440](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/claude-apps-gateway.md?plain=1#L431-L440)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway#next-steps)]
* Claude Desktop policy delivery clarified: Desktop builds its own model/disabled-tools list from `/user/bootstrap`; only the egress allowlist requires the `parentSettingsBehavior: "merge"` opt-in, while hooks/env/scoped permission rules only reach `/login` clients. [[lines 457-463](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/claude-apps-gateway.md?plain=1#L457-L463)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway#next-steps)]
* `sandbox.credentials` forwarding rules gain a new bullet: `awsPairs` and `sigv4` blocks are forwarded restriction-only (only `deny` values kept; a configured `sigv4` block pins all three AWS request forms to deny). [[lines 470-475](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/claude-apps-gateway.md?plain=1#L470-L475)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway#next-steps)]
* Telemetry destination behavior changed: the CLI now always sends OTLP/HTTP exports to the gateway (ignoring any local `OTEL_EXPORTER_OTLP_ENDPOINT`), and the gateway relays to `forward_to` destinations, discarding signals with none configured. [[line 484](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/claude-apps-gateway.md?plain=1#L484)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway#next-steps)]

#### [claude-code-on-the-web](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/claude-code-on-the-web.md) [[Source](https://code.claude.com/docs/en/claude-code-on-the-web)]

* New teleport method: from inside a cloud session, typing `/teleport` now replies with the exact `claude --teleport <session-id>` command (requires v2.1.223+ in the session's environment). [[line 149](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L149)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#from-web-to-terminal)]
* "Correct repository" teleport requirement rewritten with clearer error messaging when the checkout doesn't match the session's repo. [[lines 23-24](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L23-L24)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#cloud-environments)]

#### [claude-directory](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/claude-directory.md) [[Source](https://code.claude.com/docs/en/claude-directory)]

* `cleanupPeriodDays` minimum clarified as 1 (0 fails validation); the same cutoff now applies to automatic orphaned-worktree removal. [[line 55](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/claude-directory.md?plain=1#L55)] [[Source](https://code.claude.com/docs/en/claude-directory#explore-the-directory)]
* New behavior: if Claude Code can't read/parse a settings file, it pauses the retention cleanup sweep and warns in `/status` until fixed, unless managed settings supply `cleanupPeriodDays` (before v2.1.203 cleanup ran at the 30-day default and could delete transcripts meant to be kept longer). [[line 63](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/claude-directory.md?plain=1#L63)] [[Source](https://code.claude.com/docs/en/claude-directory#explore-the-directory)]
* New documented path `~/.claude/paste-cache/`, holding pasted text for recalled prompts. [[line 80](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/claude-directory.md?plain=1#L80)] [[Source](https://code.claude.com/docs/en/claude-directory#explore-the-directory)]

#### [cli-reference](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* New `claude import [codex|gemini]` command documented, importing configuration from other coding agents (`--dry-run`/`--yes` supported); requires v2.1.213+. [[line 99](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/cli-reference.md?plain=1#L99)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-flags)]

#### [cloud-environments](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/cloud-environments.md) [[Source](https://code.claude.com/docs/en/cloud-environments)]

* New note: self-hosted environment IDs (`ccpool_...`) follow a stricter settings-source rule for `remote.defaultEnvironmentId` than Anthropic-hosted IDs. [[line 111](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/cloud-environments.md?plain=1#L111)] [[Source](https://code.claude.com/docs/en/cloud-environments#allow-specific-domains)]
* New "GraphQL restrictions" bullet: the GitHub proxy in Anthropic-hosted cloud sessions now serves only a pinned set of GraphQL operations, rejecting everything else with 403 regardless of supplied credentials (Projects v2 unreachable through the proxy). [[line 119](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/cloud-environments.md?plain=1#L119)] [[Source](https://code.claude.com/docs/en/cloud-environments#github-proxy)]
* VM now documented explicitly as Ubuntu 24.04 on x86_64, with guidance to use x86_64 Linux precompiled binaries; sessions routed to a self-hosted environment run on the org's own runners instead. [[lines 128-130](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/cloud-environments.md?plain=1#L128-L130)] [[Source](https://code.claude.com/docs/en/cloud-environments#github-proxy)]
* Node.js version install paths documented (`/opt/node20/21/22`), with 22 on `PATH` by default. [[line 147](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/cloud-environments.md?plain=1#L147)] [[Source](https://code.claude.com/docs/en/cloud-environments#what-carries-over-from-your-setup)]

#### [code-review](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/code-review.md) [[Source](https://code.claude.com/docs/en/code-review)]

* Effort-level "reuse last" rule clarified: it reuses the last `low` through `max` level typed, and `ultra` neither updates nor consumes the remembered level. [[lines 168-169](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/code-review.md?plain=1#L168-L169)] [[Source](https://code.claude.com/docs/en/code-review#example)]

#### [commands](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/commands.md) [[Source](https://code.claude.com/docs/en/commands)]

* New `/import [codex|gemini] [--dry-run] [--yes]` command documented; `/init` now offers to run `/import` when it detects importable config from another coding agent. [[lines 197-199](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/commands.md?plain=1#L197-L199)] [[Source](https://code.claude.com/docs/en/commands#see-also)]
* New `/list-agents` command (alias `/peers`) documented — lists messageable subagents/other sessions; requires v2.1.224+ and only available where cross-session messaging is enabled. [[line 204](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/commands.md?plain=1#L204)] [[Source](https://code.claude.com/docs/en/commands#see-also)]

#### [costs](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/costs.md) [[Source](https://code.claude.com/docs/en/costs)]

* New note: usage-credit users can set `ENABLE_PROMPT_CACHING_1H=1` to keep the 1-hour cache TTL. [[line 226](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/costs.md?plain=1#L226)] [[Source](https://code.claude.com/docs/en/costs#manage-agent-team-costs)]
* New bullet: "Cross-session messages" listed as a cause of unexpected token usage — delivering a message from another session as a new turn resends full context; can be mitigated by setting `crossSessionInbound` to `hold`. [[line 228](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/costs.md?plain=1#L228)] [[Source](https://code.claude.com/docs/en/costs#manage-agent-team-costs)]

#### [data-usage](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/data-usage.md) [[Source](https://code.claude.com/docs/en/data-usage)]

* Cloud sessions clarified to run in Anthropic-managed VMs "by default"; sessions routed to a self-hosted environment run on customer infrastructure instead. [[line 241](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/data-usage.md?plain=1#L241)] [[Source](https://code.claude.com/docs/en/data-usage#webfetch-domain-safety-check)]
* WebFetch domain safety check caching behavior changed: only a hostname that passes the check is cached for 5 minutes; a blocked or failed hostname is now re-checked on the next request. [[line 250](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/data-usage.md?plain=1#L250)] [[Source](https://code.claude.com/docs/en/data-usage#webfetch-domain-safety-check)]

#### [desktop-scheduled-tasks](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/desktop-scheduled-tasks.md) [[Source](https://code.claude.com/docs/en/desktop-scheduled-tasks)]

* Clarified that scheduled-task sessions can do everything a normal session can (edit, run commands, commit, open PRs) but can't send/receive messages through the desktop app's session-to-session messaging surface. [[line 15](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/desktop-scheduled-tasks.md?plain=1#L15)] [[Source](https://code.claude.com/docs/en/desktop-scheduled-tasks#compare-scheduling-options)]

#### [desktop](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)]

* `bypassPermissions` mode's exception list expands to include removals targeting `/`/home directory and the cross-session messaging safeguards. [[line 29](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/desktop.md?plain=1#L29)] [[Source](https://code.claude.com/docs/en/desktop)]
* "Work across sessions" scoped explicitly to the desktop app's own Code-tab surface; new note that in sessions with cross-session messaging enabled, Claude can separately list/message other Claude Code sessions on the machine, including terminal sessions. [[lines 37-45](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/desktop.md?plain=1#L37-L45)] [[Source](https://code.claude.com/docs/en/desktop#start-a-session)]

#### [devcontainer](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/devcontainer.md) [[Source](https://code.claude.com/docs/en/devcontainer)]

* `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` now also disables cross-session messaging in containers (previously only Remote Control). [[line 57](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/devcontainer.md?plain=1#L57)] [[Source](https://code.claude.com/docs/en/devcontainer#add-claude-code-to-your-dev-container)]

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* New `ANTHROPIC_BEDROCK_REGION_PREFIX` variable documented. [[line 70](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/env-vars.md?plain=1#L70)] [[Source](https://code.claude.com/docs/en/env-vars#in-settings-files)]
* `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC`, `DISABLE_GROWTHBOOK`, `DISABLE_TELEMETRY`, and `DO_NOT_TRACK` all updated to note they also disable cross-session messaging. [[lines 79, 112, 121, 125](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/env-vars.md?plain=1#L79)]
* New `CLAUDE_CODE_MESSAGING_SOCKET` variable documented (auto-set by Claude Code, not user-settable). [[line 87](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/env-vars.md?plain=1#L87)] [[Source](https://code.claude.com/docs/en/env-vars#precedence)]
* New `CLAUDE_CODE_USER_DIALOG_TIMEOUT_MS` variable documented. [[line 95](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/env-vars.md?plain=1#L95)] [[Source](https://code.claude.com/docs/en/env-vars#precedence)]
* New `CLAUDE_SUBAGENT_BG_SHELL_MAX_MS` variable documented — caps subagent background-shell command lifetime at 60 minutes by default (requires v2.1.133+). [[line 103](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/env-vars.md?plain=1#L103)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* `ENABLE_PROMPT_CACHING_1H` updated: usage-credit-drawing subscription users can now set it to keep the 1-hour TTL. [[line 128](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/env-vars.md?plain=1#L128)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* New error row/section: `403` with "This GraphQL query is not enabled for this session" in cloud sessions. [[line 140](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/errors.md?plain=1#L140)] [[Source](https://code.claude.com/docs/en/errors#tune-retry-behavior)]
* New error row/section: "Could not locate the Claude CLI on PATH" — a VS Code extension error on Windows/PowerShell terminals, with full cause and fix steps. [[lines 148, 165-177](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/errors.md?plain=1#L165-L177)]

#### [feature-availability](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/feature-availability.md) [[Source](https://code.claude.com/docs/en/feature-availability)]

* New "Cross-session messaging" row added to the feature availability table (macOS/Linux only), gated to v2.1.224+, with WSL2 counting as Linux, native Windows unsupported, and cross-machine messaging requiring the same-machine or Remote Control conditions to be met (API key auth doesn't support cross-machine). [[lines 199-209](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/feature-availability.md?plain=1#L199-L209)] [[Source](https://code.claude.com/docs/en/feature-availability#related-resources)]
* `/list-agents`/`/peers` commands' availability gated on cross-session messaging noted. [[line 191](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/feature-availability.md?plain=1#L191)] [[Source](https://code.claude.com/docs/en/feature-availability#related-resources)]
* Provider "Not available" feature lists (Vertex/Bedrock/Foundry/Claude Platform on AWS tabs) all updated to add cross-session messaging as unavailable. [[lines 217-243](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/feature-availability.md?plain=1#L217-L243)] [[Source](https://code.claude.com/docs/en/feature-availability#related-resources)]

#### [features-overview](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/features-overview.md) [[Source](https://code.claude.com/docs/en/features-overview)]

* Cross-references cross-session messaging for separate sessions passing messages without forming a team. [[line 279](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/features-overview.md?plain=1#L279)] [[Source](https://code.claude.com/docs/en/features-overview#learn-more)]

#### [fullscreen](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/fullscreen.md) [[Source](https://code.claude.com/docs/en/fullscreen)]

* New behavior: users can scroll back to the start of a session even after compaction — Claude Code retains every earlier message in fullscreen scrollback across repeated compactions. [[line 291](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/fullscreen.md?plain=1#L291)] [[Source](https://code.claude.com/docs/en/fullscreen#research-preview)]

#### [gateways](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/gateways.md) [[Source](https://code.claude.com/docs/en/gateways)]

* Telemetry description updated: gateway pins OTLP export to itself and relays it to configured `forward_to` destinations. [[line 304](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/gateways.md?plain=1#L304)] [[Source](https://code.claude.com/docs/en/gateways#next-steps)]

#### [goal](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/goal.md) [[Source](https://code.claude.com/docs/en/goal)]

* Removed documented behavior: the description of running `/goal` with no argument to see turns/tokens spent, and that a goal runs until met or `/goal clear`, was deleted from the page. [[line 316](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/goal.md?plain=1#L316)] [[Source](https://code.claude.com/docs/en/goal#see-also)]

#### [headless](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/headless.md) [[Source](https://code.claude.com/docs/en/headless)]

* New clarification: `total_cost_usd` and the per-model cost breakdown in JSON output are client-side estimates and can differ from the actual bill. [[line 329](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/headless.md?plain=1#L329)] [[Source](https://code.claude.com/docs/en/headless#next-steps)]

#### [hooks-guide](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/hooks-guide.md) [[Source](https://code.claude.com/docs/en/hooks-guide)]

* New `DirectoryAdded` row added to the hook event field-matching table (`slash_command`, `register_repo_root` match values). [[line 638](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/hooks-guide.md?plain=1#L638)] [[Source](https://code.claude.com/docs/en/hooks-guide#filter-hooks-with-matchers)]

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* `DirectoryAdded` hook documentation expanded: now explicitly lists three cases where it does not fire (`--add-dir` startup flag, adding a directory via the `/permissions` Workspace tab, or re-adding an already-present directory, which errors); also clarifies the hook runs asynchronously in the background with the 600-second default timeout and doesn't block the add. [[lines 2402-2410](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/hooks.md?plain=1#L2402-L2410)] [[Source](https://code.claude.com/docs/en/hooks#cwdchanged-output)]

#### [interactive-mode](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* Command history section substantially rewritten: Up-arrow recall now reaches prompts from past sessions of the same project, not just the current session; running `/clear` no longer "resets" history — it lists the new session's prompts first, then earlier sessions' prompts; new note that recalling a prompt with pasted text resends the full paste content, referencing the paste-cache expiry behavior. [[lines 221-231](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/interactive-mode.md?plain=1#L221-L231)] [[Source](https://code.claude.com/docs/en/interactive-mode#command-history)]

#### [llm-gateway-protocol](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/llm-gateway-protocol.md) [[Source](https://code.claude.com/docs/en/llm-gateway-protocol)]

* Amazon Bedrock InvokeModel format gains an optional `/model/{model}/count-tokens` endpoint. [[line 31](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/llm-gateway-protocol.md?plain=1#L31)] [[Source](https://code.claude.com/docs/en/llm-gateway-protocol#api-formats)]
* Startup traffic changed: Anthropic Messages-format gateways now receive a `HEAD /api/hello` connection-warming probe (replacing the old `HEAD /`), skipped when a proxy or client cert is configured; Bedrock-format gateways also receive `GET /inference-profiles/{profile}` lookups when the configured model is an inference profile. [[line 41](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/llm-gateway-protocol.md?plain=1#L41)] [[Source](https://code.claude.com/docs/en/llm-gateway-protocol#optional-endpoints-and-startup-traffic)]

#### [mcp-quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/mcp-quickstart.md) [[Source](https://code.claude.com/docs/en/mcp-quickstart)]

* "Failed to connect"/"Connection error" troubleshooting expanded: `claude mcp list`/`get` now surface the HTTP status/error code and server-reported error text for "Failed to connect" (as of v2.1.219); "Connection error" still shows no detail; new guidance to check `claude mcp list` for hidden-whitespace warnings. [[lines 288-298](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/mcp-quickstart.md?plain=1#L288-L298)] [[Source](https://code.claude.com/docs/en/mcp-quickstart#troubleshooting)]

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* New behavior: in `--output-format stream-json` runs, a skipped `--mcp-config` entry is now reported in the `system/init` event's `mcp_server_errors` field (requires v2.1.219+). [[line 15](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/mcp.md?plain=1#L15)] [[Source](https://code.claude.com/docs/en/mcp#what-you-can-do-with-mcp)]
* New "Configuration warnings" subsection: Claude Code now detects and warns about hidden leading/trailing whitespace in MCP config values (`command`, `url`, `args`, `env`/`headers` keys and values) in `claude mcp list` and `/mcp`, without echoing the values. [[line 49](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/mcp.md?plain=1#L49)] [[Source](https://code.claude.com/docs/en/mcp#find-and-build-mcp-servers)]
* New capability: with tool search enabled, when a server finishes connecting mid-turn, Claude Code surfaces its tool names to Claude on the next request within the same turn instead of waiting for the user's next message. [[line 62](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/mcp.md?plain=1#L62)] [[Source](https://code.claude.com/docs/en/mcp#option-1-add-a-remote-http-server)]
* GitHub PAT connection-failure example now shows the HTTP status returned (e.g. 401). [[line 113](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/mcp.md?plain=1#L113)] [[Source](https://code.claude.com/docs/en/mcp#option-3-add-a-local-stdio-server)]

#### [memory](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/memory.md) [[Source](https://code.claude.com/docs/en/memory)]

* New cross-reference: `/init`/`/import` can bring another coding agent's configuration into Claude Code, appending instruction files to `CLAUDE.md` and importing MCP servers, commands, subagents, and skills (requires v2.1.213+). [[line 168](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/memory.md?plain=1#L168)] [[Source](https://code.claude.com/docs/en/memory#set-up-rules)]

#### [model-config](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* Clarified that a skill/command running in a forked subagent (`context: fork`) follows the subagent model-substitution rules instead of being ignored when its model override is blocked. [[line 181](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/model-config.md?plain=1#L181)] [[Source](https://code.claude.com/docs/en/model-config#enforce-the-allowlist-for-the-default-model)]

#### [permission-modes](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/permission-modes.md) [[Source](https://code.claude.com/docs/en/permission-modes)]

* New announcement: auto mode becomes the default permission mode for new sessions on Pro/Max/Team starting August 14, 2026. [[line 208](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/permission-modes.md?plain=1#L208)] [[Source](https://code.claude.com/docs/en/permission-modes#what-the-classifier-blocks-by-default)]
* New note: the Cowork tab has its own separate, independently-enabled permission modes and doesn't use the CLI's mode selector. [[line 200](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/permission-modes.md?plain=1#L200)] [[Source](https://code.claude.com/docs/en/permission-modes#what-the-classifier-blocks-by-default)]
* `bypassPermissions` mode gains two new documented cross-session messaging safeguards: the `isolatePeerMachines` approval prompt for cross-machine sends still fires, and inbound messages follow `crossSessionInbound` rules, delivered without asking only when the sender also identifies as bypassing. [[lines 223-230](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/permission-modes.md?plain=1#L223-L230)] [[Source](https://code.claude.com/docs/en/permission-modes#what-the-classifier-blocks-by-default)]
* Classifier token-usage note narrowed: classifier calls count toward usage specifically on Enterprise plans and API-key/Bedrock/Vertex/Foundry/Claude-Platform-on-AWS accounts. [[line 218](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/permission-modes.md?plain=1#L218)] [[Source](https://code.claude.com/docs/en/permission-modes#what-the-classifier-blocks-by-default)]

#### [permissions](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/permissions.md) [[Source](https://code.claude.com/docs/en/permissions)]

* `bypassPermissions` mode row/prose updated to note the cross-session messaging safeguards still apply. [[lines 243, 246](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/permissions.md?plain=1#L243)]

#### [prompt-caching](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/prompt-caching.md) [[Source](https://code.claude.com/docs/en/prompt-caching)]

* New note: set `ENABLE_PROMPT_CACHING_1H=1` to keep the 1-hour TTL while drawing on usage credits. [[line 51](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/prompt-caching.md?plain=1#L51)] [[Source](https://code.claude.com/docs/en/prompt-caching#actions-that-invalidate-the-cache)]

#### [remote-control](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/remote-control.md) [[Source](https://code.claude.com/docs/en/remote-control)]

* New paragraph: the Remote Control connection now also carries cross-session messages between a user's machines and from Claude Code on the web sessions (requires v2.1.224+). [[line 63](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/remote-control.md?plain=1#L63)] [[Source](https://code.claude.com/docs/en/remote-control#start-a-remote-control-session)]
* New limitation documented: non-permission/non-`AskUserQuestion` forwarded dialogs now expire after a default 5-minute deadline, configurable via `dialogExpiry` (requires v2.1.224+). [[line 71](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/remote-control.md?plain=1#L71)] [[Source](https://code.claude.com/docs/en/remote-control#start-a-remote-control-session)]

#### [sandbox-environments](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/sandbox-environments.md) [[Source](https://code.claude.com/docs/en/sandbox-environments)]

* `--dangerously-skip-permissions` exception list reformatted into bullets, adding the cross-session messaging safeguards as a new exception. [[lines 150-159](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/sandbox-environments.md?plain=1#L150-L159)] [[Source](https://code.claude.com/docs/en/sandbox-environments#see-also)]

#### [sandboxing](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/sandboxing.md) [[Source](https://code.claude.com/docs/en/sandboxing)]

* WSL2 Windows-binary-launch behavior changed: now governed by the sandbox's Unix-socket settings (`allowAllUnixSockets`/`allowUnixSockets`) and requires the optional seccomp filter to be installed to block it in the first place. [[line 92](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/sandboxing.md?plain=1#L92)] [[Source](https://code.claude.com/docs/en/sandboxing#set-up-linux-and-wsl2)]
* New optional env-var masking fields: `extract` (regex-based structured masking), `onExtractNoMatch` (warn/deny/error), and `decode: "jwt"` with `maskClaims` for JWT-aware masking (requires v2.1.224+). [[lines 189-198](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/sandboxing.md?plain=1#L189-L198)] [[Source](https://code.claude.com/docs/en/sandboxing#which-settings-can-disable-it)]
* New "Re-sign AWS requests" section: documents `credentials.awsPairs` (group non-standard AWS variable names for SigV4 re-signing) and `credentials.sigv4` (per-request-form policy — `streaming`/`presigned`/`sigv4a` — `deny` vs `passthrough`), requires v2.1.224+. [[lines 200-235](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/sandboxing.md?plain=1#L200-L235)] [[Source](https://code.claude.com/docs/en/sandboxing#which-settings-can-disable-it)]
* Credential-file masking gains the same `decode: "jwt"`/`maskClaims` support as env vars. [[lines 244-253](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/sandboxing.md?plain=1#L244-L253)] [[Source](https://code.claude.com/docs/en/sandboxing#protect-credentials)]

#### [security](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/security.md) [[Source](https://code.claude.com/docs/en/security)]

* Cloud execution security section now clarifies self-hosted environment sessions run on customer infrastructure with isolation/network/git-credential responsibility on the deploying org. [[line 29](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/security.md?plain=1#L29)] [[Source](https://code.claude.com/docs/en/security#protect-against-prompt-injection)]

#### [sessions](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/sessions.md) [[Source](https://code.claude.com/docs/en/sessions)]

* Cross-project session ID resolution now requires the other project to hold "a transcript with messages" (stricter than just any transcript) to disambiguate. [[line 55](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/sessions.md?plain=1#L55)] [[Source](https://code.claude.com/docs/en/sessions#where-the-session-picker-looks)]

#### [settings](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* New `crossSessionInbound` setting fully documented (`accept`/`hold`/`refuse`, with precedence rules), requires v2.1.224+. [[line 70](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/settings.md?plain=1#L70)] [[Source](https://code.claude.com/docs/en/settings#what-uses-scopes)]
* New `dialogExpiry` setting documented — default `5m`, governs forwarded-dialog and held-cross-session-message-approval deadlines. [[line 73](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/settings.md?plain=1#L73)] [[Source](https://code.claude.com/docs/en/settings#settings-files)]
* `env` setting: `CLAUDE_CODE_MESSAGING_SOCKET` is now explicitly ignored if set there, since Claude Code exports its own per-session value (requires v2.1.224+). [[line 82](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/settings.md?plain=1#L82)] [[Source](https://code.claude.com/docs/en/settings#settings-files)]
* New `isolatePeerMachines` setting documented — requires approval before a `SendMessage` reply reaches a session beyond the local machine; a `true` from any scope applies (requires v2.1.224+). [[line 90](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/settings.md?plain=1#L90)] [[Source](https://code.claude.com/docs/en/settings#settings-files)]
* `remote.defaultEnvironmentId`: self-hosted environment IDs (`ccpool_...`) are now honored only from user/managed/`--settings` sources, ignored with a warning from project/local settings. [[line 99](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/settings.md?plain=1#L99)] [[Source](https://code.claude.com/docs/en/settings#settings-files)]
* Major new sandbox-credentials settings documented: `credentials.files[].decode`, `credentials.files[].maskClaims`, `credentials.envVars[].extract`, `credentials.envVars[].onExtractNoMatch`, `credentials.envVars[].decode`, `credentials.envVars[].maskClaims`, `credentials.awsPairs`, `credentials.sigv4` (all requiring v2.1.224+). [[lines 112-133](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/settings.md?plain=1#L112-L133)] [[Source](https://code.claude.com/docs/en/settings#settings-files)]
* `network.allowAllUnixSockets` behavior clarified as tied to seccomp filter installation on Linux/WSL2; on WSL2 it also reopens the Windows-binary interop socket. [[line 136](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/settings.md?plain=1#L136)] [[Source](https://code.claude.com/docs/en/settings#settings-files)]
* Settings precedence section: new documented exceptions for `isolatePeerMachines` (a `true` from any scope always wins) and `crossSessionInbound` (stricter project/local value overrides trusted sources). [[lines 144-145](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/settings.md?plain=1#L144-L145)] [[Source](https://code.claude.com/docs/en/settings#settings-files)]
* Plugin marketplace `source` gains a new `file` type (local path to a `marketplace.json` file, distinct from the existing `directory` type). [[line 153](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/settings.md?plain=1#L153)] [[Source](https://code.claude.com/docs/en/settings#when-edits-take-effect)]

#### [skills](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)]

* `model` frontmatter field: with `context: fork`, the model override now applies to the forked subagent's model rather than the main session, following subagent model-substitution rules. [[line 33](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/skills.md?plain=1#L33)] [[Source](https://code.claude.com/docs/en/skills#run-and-verify-your-app)]

#### [sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* New cross-reference distinguishing cross-session messaging (separate sessions) from agent teams (Claude-supervised). [[line 76](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/sub-agents.md?plain=1#L76)] [[Source](https://code.claude.com/docs/en/sub-agents#quickstart-create-your-first-subagent)]
* `ListAgents` tool now follows the same foreground/background filters as other built-in tools — inherited by foreground subagents when cross-session messaging is enabled, removed from background subagents. [[line 93](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/sub-agents.md?plain=1#L93)] [[Source](https://code.claude.com/docs/en/sub-agents#quickstart-create-your-first-subagent)]
* `bypassPermissions` subagent mode's still-prompting list gains the `isolatePeerMachines` cross-machine-message approval. [[lines 101-110](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/sub-agents.md?plain=1#L101-L110)] [[Source](https://code.claude.com/docs/en/sub-agents#quickstart-create-your-first-subagent)]
* `SendMessage` tool description expanded: in cross-session-messaging-enabled sessions, subagents can message other Claude Code sessions on the machine, or reply to sessions beyond it. [[line 119](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/sub-agents.md?plain=1#L119)] [[Source](https://code.claude.com/docs/en/sub-agents#quickstart-create-your-first-subagent)]

#### [terminal-config](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/terminal-config.md) [[Source](https://code.claude.com/docs/en/terminal-config)]

* New paste-cache behavior documented: pasted content is cached under `~/.claude/paste-cache/` so recalled prompts resend full content (even across sessions) until the cache file ages out per `cleanupPeriodDays`; documents distinct handling when the cache has expired (plain prompt vs. shell-mode/slash-command vs. empty-after-removal cases). [[lines 131-136](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/terminal-config.md?plain=1#L131-L136)] [[Source](https://code.claude.com/docs/en/terminal-config#create-a-custom-theme)]

#### [tools-reference](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/tools-reference.md) [[Source](https://code.claude.com/docs/en/tools-reference)]

* New `ListAgents` tool row added — lists messageable agents (subagents, local sessions, reply-only Remote Control sessions); backs `/list-agents`; requires v2.1.224+, only in cross-session-messaging-enabled sessions. [[line 26](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/tools-reference.md?plain=1#L26)] [[Source](https://code.claude.com/docs/en/tools-reference)]
* `SendMessage` tool description expanded to cover messaging other Claude Code sessions (same-machine or cross-machine reply via Remote Control). [[line 157](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/tools-reference.md?plain=1#L157)] [[Source](https://code.claude.com/docs/en/tools-reference#background-commands)]

#### [troubleshoot-install](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/troubleshoot-install.md) [[Source](https://code.claude.com/docs/en/troubleshoot-install)]

* New error row and full new section: `npm error code ENOTEMPTY` during update/reinstall, with diagnosis and fix steps (identify and remove leftover package/temp directories, reinstall, verify). [[lines 175, 241-279](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/troubleshoot-install.md?plain=1#L241-L279)]
* New error row and expanded section: Windows install command printing script text instead of installing (missing `| iex` or `-o`), with fixed commands for PowerShell and CMD. [[lines 176, 184-205](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/troubleshoot-install.md?plain=1#L184-L205)]
* `dyld: cannot load` on macOS section reorganized to clearly separate two distinct causes (old macOS/`libicucore` `Symbol not found` vs. loader rejecting the binary's load commands / `Abort trap`), each with its own example. [[lines 211-234](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/troubleshoot-install.md?plain=1#L211-L234)] [[Source](https://code.claude.com/docs/en/troubleshoot-install#check-for-conflicting-installations)]

#### [whats-new/2026-w24](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/whats-new/2026-w24.md) [[Source](https://code.claude.com/docs/en/whats-new/2026-w24)]

* Retroactive terminology correction: an existing changelog entry originally reading "Cross-session messaging is hardened" was changed to "Agent messaging is hardened," disambiguating it from the new cross-session-messaging feature (that entry was actually about intra-team agent message hardening). [[line 292](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/whats-new/2026-w24.md?plain=1#L292)] [[Source](https://code.claude.com/docs/en/whats-new/2026-w24)]

#### [workflows](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/workflows.md) [[Source](https://code.claude.com/docs/en/workflows)]

* New runtime constraint: a dynamic workflow script fails before the run starts if it contains `import()` — module loading is disallowed; the script body is plain JavaScript. [[line 305](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/workflows.md?plain=1#L305)] [[Source](https://code.claude.com/docs/en/workflows#resume-after-a-pause)]
* New behavior: when an org's `availableModels` allowlist blocks a model a workflow script requests for an agent, that agent now runs on a substituted model per the standard subagent substitution rules, with a warning shown in the `/workflows` progress view. [[line 313](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/claude-code/workflows.md?plain=1#L313)] [[Source](https://code.claude.com/docs/en/workflows#resume-after-a-pause)]

-----

## API changes

### Changed documents

#### [about-claude/pricing](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/api/about-claude/pricing.md) [[Source](https://platform.claude.com/docs/en/about-claude/pricing)]

* The data residency multiplier (1.1x) now explicitly applies to Claude Managed Agents sessions when `model.inference_geo` is pinned to `"us"`; the pricing table row previously stating this multiplier didn't apply to Managed Agents was removed. [[line 391](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/api/about-claude/pricing.md?plain=1#L391)] [[Source](https://platform.claude.com/docs/en/about-claude/pricing)]

#### [agents-and-tools/tool-use/advisor-tool](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/api/agents-and-tools/tool-use/advisor-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool)]

* New section documenting the advisor tool's availability within Claude Managed Agents sessions, configured as a roster entry (`{"type": "advisor", "model": ...}`) rather than a tool definition; no `max_uses`/`max_tokens`/`caching`, and advice arrives as thread events instead of `advisor_tool_result` blocks. [[lines 654-657](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/api/agents-and-tools/tool-use/advisor-tool.md?plain=1#L654-L657)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool)]

#### [api/overview](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/api/api/overview.md) [[Source](https://platform.claude.com/docs/en/api/overview)]

* Rate limits and spend limits are now viewed/managed on separate Console pages (Rate limits page vs. Billing page), replacing the old single "Limits" page reference. [[line 162](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/api/api/overview.md?plain=1#L162)] [[Source](https://platform.claude.com/docs/en/api/overview)]

#### [manage-claude/data-residency](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/api/manage-claude/data-residency.md) [[Source](https://platform.claude.com/docs/en/manage-claude/data-residency)]

* Claude Managed Agents now supports geographic inference pinning at the agent level via `inference_geo` in the agent's model configuration (with per-session overrides), reversing prior documentation stating this wasn't supported. [[line 14](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/api/manage-claude/data-residency.md?plain=1#L14)] [[Source](https://platform.claude.com/docs/en/manage-claude/data-residency)]
* The 1.1x data-residency pricing multiplier now explicitly applies to Managed Agents sessions running an agent pinned to `"us"`. [[line 113](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/api/manage-claude/data-residency.md?plain=1#L113)] [[Source](https://platform.claude.com/docs/en/manage-claude/data-residency)]

#### [manage-claude/inference-hooks](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/api/manage-claude/inference-hooks.md) [[Source](https://platform.claude.com/docs/en/manage-claude/inference-hooks)]

* Added an explanatory flow diagram (with new image asset) walking through a Cowork example, clarifying that hooks fire at two points: prompt arrival and tool-result return. [[lines 26-28](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/api/manage-claude/inference-hooks.md?plain=1#L26-L28)] [[Source](https://platform.claude.com/docs/en/manage-claude/inference-hooks)]

#### [manage-claude/workspaces](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/api/manage-claude/workspaces.md) [[Source](https://platform.claude.com/docs/en/manage-claude/workspaces)]

* Workspace limits configuration is now split across two separate Console tabs, "Rate limits" and "Spend limits" (previously a single "Limits" tab combining rate limits and spend notifications). [[lines 121-124](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/api/manage-claude/workspaces.md?plain=1#L121-L124)] [[Source](https://platform.claude.com/docs/en/manage-claude/workspaces)]
* Corresponding update to the workspace limits explanation, pointing to the specific "Spend limits" and "Rate limits" settings tabs. [[lines 233-234](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/api/manage-claude/workspaces.md?plain=1#L233-L234)] [[Source](https://platform.claude.com/docs/en/manage-claude/workspaces)]

#### [managed-agents/agent-setup](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/api/managed-agents/agent-setup.md) [[Source](https://platform.claude.com/docs/en/managed-agents/agent-setup)]

* The `model` object now accepts an `inference_geo` field in addition to `speed`/`effort`. [[line 20](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/api/managed-agents/agent-setup.md?plain=1#L20)] [[Source](https://platform.claude.com/docs/en/managed-agents/agent-setup)]
* New documentation: how to pin `inference_geo` (`"us"` or `"global"`) on an agent's model config, validation against workspace `allowed_inference_geos` at save/session-create/each turn, a 400 error if set on an unsupported model, and the requirement that in a multiagent config the coordinator and all roster members must share the same pin (or all be unset). [[lines 63-67](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/api/managed-agents/agent-setup.md?plain=1#L63-L67)] [[Source](https://platform.claude.com/docs/en/managed-agents/agent-setup)]
* Clarified update semantics: supplying a `model` object without `inference_geo` clears any existing pin, in addition to the existing `effort` reset behavior. [[line 143](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/api/managed-agents/agent-setup.md?plain=1#L143)] [[Source](https://platform.claude.com/docs/en/managed-agents/agent-setup)]

#### [managed-agents/events-and-streaming](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/api/managed-agents/events-and-streaming.md) [[Source](https://platform.claude.com/docs/en/managed-agents/events-and-streaming)]

* New "Reaching a session budget" section: describes the `budget_reached` stop reason, the pause sequence (three ordered stream events), how a thread that both crosses the cap and finishes reports `end_turn` while the session reports `budget_reached`, which events are still accepted while paused, and that resuming requires a budget update. [[lines 396-408](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/api/managed-agents/events-and-streaming.md?plain=1#L396-L408)] [[Source](https://platform.claude.com/docs/en/managed-agents/events-and-streaming)]
* The session `usage` object now documents new fields: `list_cost`, `active_seconds`, and `server_tool_use` (web_search_requests/web_fetch_requests), alongside existing token counts, plus per-thread vs. session-level usage reconciliation. [[lines 450-471](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/api/managed-agents/events-and-streaming.md?plain=1#L450-L471)] [[Source](https://platform.claude.com/docs/en/managed-agents/events-and-streaming)]
* New guidance that the `session.usage` stream event carries the same cumulative snapshot plus `budget`, emitted before idle transitions and when a thread pauses at budget, with a recommendation to use session budgets instead of manually polling usage to enforce spend limits. [[lines 469-471](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/api/managed-agents/events-and-streaming.md?plain=1#L469-L471)] [[Source](https://platform.claude.com/docs/en/managed-agents/events-and-streaming)]

#### [managed-agents/github](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/api/managed-agents/github.md) [[Source](https://platform.claude.com/docs/en/managed-agents/github)]

* Mounting a GitHub repository now also loads skills from its root `.claude/skills` directory automatically, discovered once at session start. [[line 57](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/api/managed-agents/github.md?plain=1#L57)] [[Source](https://platform.claude.com/docs/en/managed-agents/github)]

#### [managed-agents/multiagent-orchestration](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/api/managed-agents/multiagent-orchestration.md) [[Source](https://platform.claude.com/docs/en/managed-agents/multiagent-orchestration)]

* New roster entry type `{"type": "advisor", "model": "<model id>"}` giving the session's primary thread a mid-turn advisor (max one per roster). [[line 63](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/api/managed-agents/multiagent-orchestration.md?plain=1#L63)] [[Source](https://platform.claude.com/docs/en/managed-agents/multiagent-orchestration)]
* New "Give the session an advisor" section: entry schema, reserved roster name `anthropic.advisor`, model-capability pairing rules, differences from the Messages API advisor tool, consultation thread lifecycle/event ordering, redacted vs. plaintext advice delivery per advisor model policy, interrupt behavior, exemption from concurrent-thread limits, prompt caching/billing, and how to remove the advisor. [[lines 71-130](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/api/managed-agents/multiagent-orchestration.md?plain=1#L71-L130)] [[Source](https://platform.claude.com/docs/en/managed-agents/multiagent-orchestration)]
* New rule: when agents pin `inference_geo`, the coordinator's and all roster members' pins must match (all same value or all unset), enforced with a 400 on save or session-create override. [[line 69](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/api/managed-agents/multiagent-orchestration.md?plain=1#L69)] [[Source](https://platform.claude.com/docs/en/managed-agents/multiagent-orchestration)]
* New note: session budgets are a single shared cap across all threads, with each thread priced at its own served model; advisor consultation threads are exempt from the 25-concurrent-thread limit. [[lines 202-206](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/api/managed-agents/multiagent-orchestration.md?plain=1#L202-L206)] [[Source](https://platform.claude.com/docs/en/managed-agents/multiagent-orchestration)]
* The multiagent thread events table now notes advisor consultations emit the same events under the reserved name `anthropic.advisor`. [[line 246](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/api/managed-agents/multiagent-orchestration.md?plain=1#L246)] [[Source](https://platform.claude.com/docs/en/managed-agents/multiagent-orchestration)]

#### [managed-agents/scheduled-deployments](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/api/managed-agents/scheduled-deployments.md) [[Source](https://platform.claude.com/docs/en/managed-agents/scheduled-deployments)]

* Deployments can now take an optional `budget` object (same shape as a session budget) that's copied onto every session the deployment starts, bounding each run independently rather than acting as a cumulative cap; example shows updating an existing deployment's budget via PATCH, and budgets can be cleared with `"budget": null`. [[lines 84-110](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/api/managed-agents/scheduled-deployments.md?plain=1#L84-L110)] [[Source](https://platform.claude.com/docs/en/managed-agents/scheduled-deployments)]

#### [managed-agents/self-hosted-sandboxes](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/api/managed-agents/self-hosted-sandboxes.md) [[Source](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes)]

* Added Fly.io to the list of platform-specific self-hosted sandbox integration guides. [[line 36](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/api/managed-agents/self-hosted-sandboxes.md?plain=1#L36)] [[Source](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes)]

#### [managed-agents/session-operations](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/api/managed-agents/session-operations.md) [[Source](https://platform.claude.com/docs/en/managed-agents/session-operations)]

* Clarified that an agent's model configuration, including its `inference_geo` pin, cannot change mid-session — it must be set at agent save time or via a session-create `model` override. [[line 28](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/api/managed-agents/session-operations.md?plain=1#L28)] [[Source](https://platform.claude.com/docs/en/managed-agents/session-operations)]
* New "Updating the session budget" section: how to replace or remove (`null`) a session's budget, both of which auto-resume paused work; a replacement cap must exceed consumed list cost, and removal is one-way (can't re-add). [[lines 52-54](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/api/managed-agents/session-operations.md?plain=1#L52-L54)] [[Source](https://platform.claude.com/docs/en/managed-agents/session-operations)]

#### [managed-agents/sessions](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/api/managed-agents/sessions.md) [[Source](https://platform.claude.com/docs/en/managed-agents/sessions)]

* New behavior: a session-create `model` override now also sets/clears the `inference_geo` pin for that session, validated against workspace `allowed_inference_geos`. [[line 103](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/api/managed-agents/sessions.md?plain=1#L103)] [[Source](https://platform.claude.com/docs/en/managed-agents/sessions)]
* New "Set a session budget" section: `budget` object schema (`type: "limit"`, `max_list_cost` with `amount` in cents as a string + `currency`, USD only), pause behavior at `budget_reached`, budget can only be set at creation, and can be changed or removed later (not added after the fact), with a full cURL example. [[lines 135-163](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/api/managed-agents/sessions.md?plain=1#L135-L163)] [[Source](https://platform.claude.com/docs/en/managed-agents/sessions)]

#### [managed-agents/skills](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/api/managed-agents/skills.md) [[Source](https://platform.claude.com/docs/en/managed-agents/skills)]

* Skills can now reach an agent two ways: attached via the agent's `skills` array, or newly, loaded from a GitHub repository mounted on the session. [[line 9](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/api/managed-agents/skills.md?plain=1#L9)] [[Source](https://platform.claude.com/docs/en/managed-agents/skills)]
* New major section "Load skills from a GitHub repository": discovery at exactly `.claude/skills/<skill-name>/SKILL.md` (one level deep at repo root), requires the `read` tool, a security warning about the trust boundary (repo contributors can inject instructions), cloud-sandbox-only (not supported for self-hosted sandboxes), discovery runs once at session start against the checked-out ref, and repository skills can coexist with attached skills. [[lines 73-142](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/api/managed-agents/skills.md?plain=1#L73-L142)] [[Source](https://platform.claude.com/docs/en/managed-agents/skills)]

#### [managed-agents/webhooks](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/api/managed-agents/webhooks.md) [[Source](https://platform.claude.com/docs/en/managed-agents/webhooks)]

* New webhook event `session.budget_reached`: fires when a session hits its budget and pauses; fires at most once per budget value, re-armed by changing the budget. [[line 45](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/api/managed-agents/webhooks.md?plain=1#L45)] [[Source](https://platform.claude.com/docs/en/managed-agents/webhooks)]
* `session.thread_created` description updated to also cover advisor consultations starting. [[line 48](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/api/managed-agents/webhooks.md?plain=1#L48)] [[Source](https://platform.claude.com/docs/en/managed-agents/webhooks)]

#### [release-notes/overview](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/api/release-notes/overview.md) [[Source](https://platform.claude.com/docs/en/release-notes/overview)]

* New "August 7, 2026" release notes entry covering four features: session budgets, session advisors, Managed Agents `inference_geo` pinning, and loading skills from a GitHub repository. [[lines 15-20](https://github.com/gpambrozio/ClaudeDocs/blob/f96cccaca0e58c6043fb23015911c76c5158857e/docs-md/api/release-notes/overview.md?plain=1#L15-L20)] [[Source](https://platform.claude.com/docs/en/release-notes/overview)]
