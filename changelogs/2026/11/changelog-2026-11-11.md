# [Claude docs changes for November 11th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/b62d81cf7251346db587924ef1221e0895fc3bdf) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/b62d81cf7251346db587924ef1221e0895fc3bdf)]

## Executive Summary
- The Compliance API now documents **Security posture** events and results, with a seven-page guide covering SIEM ingestion, change detection, OCSF mapping, and event/result references.
- Enterprise admins can give different member groups their own **server-managed settings** instead of one organization-wide configuration.
- **Fast mode** now supports Fable 5.2 (on the Anthropic API and, with conditions, Google Cloud's Agent Platform). The docs also list new pricing, and Opus 5.5 is the default fast model.
- A new **Fork a session from your browser** feature for Remote Control. There is also a new `CLAUDE_CODE_DISABLE_FEATURE_FLAGS` variable, which makes Remote Control and the advisor unavailable when set.
- API **preserved thinking** now has a per-model, per-account enforcement table for the prefix check. A new "Per-message effort" page covers changing effort mid-conversation, and the prompt caching docs were expanded.

## New Claude Code versions

No new version files in this commit.

-----

## Claude Code changes

### Changed documents

#### [advisor](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/claude-code/advisor.md) [[Source](https://code.claude.com/docs/en/advisor)]

* The advisor tool now works on Claude Platform on AWS (Claude Code v2.1.300 or later), but still not on Amazon Bedrock. [[line 7](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/claude-code/advisor.md?plain=1#L7)] [[Source](https://code.claude.com/docs/en/advisor#escalate-hard-decisions-with-the-advisor-tool)]
* New requirements covering LLM gateways and feature-flag fetching. A session with `DISABLE_TELEMETRY` set has no advisor outside Claude Platform on AWS. [[lines 173-177](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/claude-code/advisor.md?plain=1#L173-L177)] [[Source](https://code.claude.com/docs/en/advisor#requirements)]

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* Added `CLAUDE_CODE_DISABLE_FEATURE_FLAGS` (v2.1.319 or later). It supersedes `DISABLE_GROWTHBOOK`. [[lines 247-451](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/claude-code/env-vars.md?plain=1#L247-L451)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* Added `CLAUDE_CODE_DISABLE_CRON`, which disables session-scoped scheduled tasks, `/loop`, and `CronCreate`. [[line 242](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/claude-code/env-vars.md?plain=1#L242)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* The list of features that need feature-flag fetching now includes Remote Control and the advisor. [[lines 569-582](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/claude-code/env-vars.md?plain=1#L569-L582)] [[Source](https://code.claude.com/docs/en/env-vars#features-that-need-feature-flag-fetching)]

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* New entry for login refresh failures when the config-directory disk or quota is full. [[line 1481](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/claude-code/errors.md?plain=1#L1481)] [[Source](https://code.claude.com/docs/en/errors#could-not-refresh-your-login-the-disk-that-holds-the-claude-code-config-directory-is-full)]
* New entry for "The search failed, so this is not a 'no matches' result" (Grep/Glob), with steps to capture a ripgrep error. [[line 5145](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/claude-code/errors.md?plain=1#L5145)] [[Source](https://code.claude.com/docs/en/errors#the-search-failed-so-this-is-not-a-no-matches-result)]
* New entry for "This forked session could not be started" for Remote Control forks. [[line 5737](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/claude-code/errors.md?plain=1#L5737)] [[Source](https://code.claude.com/docs/en/errors#this-forked-session-could-not-be-started)]
* New retry variables `CLAUDE_CODE_RETRY_WATCHDOG_MAX_USAGE_LIMIT_WAIT_MS` and `CLAUDE_CODE_NONSTREAMING_TIMEOUT_RETRIES`. A new section explains how long a non-streaming attempt waits. [[lines 556-571](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/claude-code/errors.md?plain=1#L556-L571)] [[Source](https://code.claude.com/docs/en/errors#tune-retry-behavior)]
* Clarified what to do after a `Context exceeds` warning, depending on whether auto-compact is on. [[lines 2479-2494](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/claude-code/errors.md?plain=1#L2479-L2494)] [[Source](https://code.claude.com/docs/en/errors#context-exceeds-the-token-limit)]
* Rewrote the recovery steps for a corrupt `~/.claude.json`. [[lines 3338-3353](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/claude-code/errors.md?plain=1#L3338-L3353)] [[Source](https://code.claude.com/docs/en/errors#configuration-error-in-claudejson)]
* Cloud environment network errors now cover the Default environment's Limited access and the package-manager allowlist. [[lines 2218-2225](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/claude-code/errors.md?plain=1#L2218-L2225)] [[Source](https://code.claude.com/docs/en/errors#host-not-allowed-in-a-cloud-session)]

#### [fast-mode](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/claude-code/fast-mode.md) [[Source](https://code.claude.com/docs/en/fast-mode)]

* Fast mode is now supported on Fable 5.2, Opus 5.5, Opus 5, and Opus 4.8. Pricing per MTok input/output is $16/$80 on Fable 5.2, $8/$40 on Opus 5.5, and $10/$50 on Opus 5 and Opus 4.8. [[lines 11-24](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/claude-code/fast-mode.md?plain=1#L11-L24)] [[Source](https://code.claude.com/docs/en/fast-mode#speed-up-responses-with-fast-mode)]
* Opus 5.5 is the fast mode default from v2.1.280. Fast mode on Fable 5.2 persists across sessions only if you turned it on while using Fable 5.2. [[lines 38-64](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/claude-code/fast-mode.md?plain=1#L38-L64)] [[Source](https://code.claude.com/docs/en/fast-mode#toggle-fast-mode)]
* New section "Use fast mode on Agent Platform", covering Fable 5.2 in the `global`, `us`, and `eu` regions. It also covers the fallback messages shown to users. [[lines 162-183](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/claude-code/fast-mode.md?plain=1#L162-L183)] [[Source](https://code.claude.com/docs/en/fast-mode#use-fast-mode-on-agent-platform)]
* If your `availableModels` allowlist excludes the model `/fast` switches to, turning on fast mode is refused. The availability check goes directly to `api.anthropic.com` and ignores `ANTHROPIC_BASE_URL`. [[lines 149-190](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/claude-code/fast-mode.md?plain=1#L149-L190)] [[Source](https://code.claude.com/docs/en/fast-mode#requirements)]

#### [feature-availability](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/claude-code/feature-availability.md) [[Source](https://code.claude.com/docs/en/feature-availability)]

* Updated the provider matrix: fast mode on Agent Platform and the advisor on Claude Platform on AWS (v2.1.300 or later). [[lines 92-261](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/claude-code/feature-availability.md?plain=1#L92-L261)] [[Source](https://code.claude.com/docs/en/feature-availability#cli-capabilities-that-vary-by-provider)]
* Feature availability behind an LLM gateway matches the underlying provider. [[line 220](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/claude-code/feature-availability.md?plain=1#L220)] [[Source](https://code.claude.com/docs/en/feature-availability#admin-and-analytics)]

#### [goal](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/claude-code/goal.md) [[Source](https://code.claude.com/docs/en/goal)]

* A goal is cleared with a `(disk full)` warning when Claude Code can't renew the login. [[lines 130-133](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/claude-code/goal.md?plain=1#L130-L133)] [[Source](https://code.claude.com/docs/en/goal#errors-you-have-to-fix-clear-the-goal)]

#### [model-config](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* New guidance on turning thinking off or reducing it. You can't turn it off on Opus 5.5, Sonnet 5.5, Haiku 5.5, or the Fable models, and there are separate steps for the Anthropic API and third-party providers. Interactive sessions get redacted thinking blocks by default. [[lines 771-782](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/claude-code/model-config.md?plain=1#L771-L782)] [[Source](https://code.claude.com/docs/en/model-config#extended-thinking)]

#### [monitoring-usage](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* `claude_code.safety_event` is no longer sent from v2.1.312. Use `tool_decision` events to see refused tool calls. [[lines 1046-1057](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/claude-code/monitoring-usage.md?plain=1#L1046-L1057)] [[Source](https://code.claude.com/docs/en/monitoring-usage#safety-event)]
* From v2.1.312, official-marketplace plugin MCP server names appear as `plugin_<plugin>_<server>`. [[line 710](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/claude-code/monitoring-usage.md?plain=1#L710)] [[Source](https://code.claude.com/docs/en/monitoring-usage#cost-counter)]
* Updated detection-rule table for hook-blocked actions. [[lines 1685-1687](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/claude-code/monitoring-usage.md?plain=1#L1685-L1687)] [[Source](https://code.claude.com/docs/en/monitoring-usage#map-security-questions-to-events)]

#### [permission-modes](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/claude-code/permission-modes.md) [[Source](https://code.claude.com/docs/en/permission-modes)]

* Auto mode's classifier now blocks recursive forced deletes (`rm -rf "$VAR"`) when the variable is not assigned in the conversation. The block clears when you name the exact path. [[lines 483-485](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/claude-code/permission-modes.md?plain=1#L483-L485)] [[Source](https://code.claude.com/docs/en/permission-modes#what-the-classifier-blocks-by-default)]
* Protected path writes are now documented per mode. In auto mode they are routed to the classifier. [[lines 731-737](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/claude-code/permission-modes.md?plain=1#L731-L737)] [[Source](https://code.claude.com/docs/en/permission-modes#protected-paths)]

#### [plugins/org](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/claude-code/plugins/org.md) [[Source](https://code.claude.com/docs/en/plugins/org)]

* `strictPluginOnlyCustomization` now blocks skills, agents, hooks, and MCP servers, and can lock them individually. It also stops skills-directory plugins from loading. [[line 184](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/claude-code/plugins/org.md?plain=1#L184)] [[Source](https://code.claude.com/docs/en/plugins/org#control-matrix)]
* New guidance on release channels per user group, with Enterprise group configurations. [[lines 335-383](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/claude-code/plugins/org.md?plain=1#L335-L383)] [[Source](https://code.claude.com/docs/en/plugins/org#assign-release-channels-to-user-groups)]

#### [remote-control](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/claude-code/remote-control.md) [[Source](https://code.claude.com/docs/en/remote-control)]

* New "Fork a session from your browser" section. Fork from claude.ai/code, from the session menu or from an earlier message. It is declined when the session is busy or hosted by the VS Code extension or an Agent SDK app. [[lines 184-194](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/claude-code/remote-control.md?plain=1#L184-L194)] [[Source](https://code.claude.com/docs/en/remote-control#fork-a-session-from-your-browser)]
* Remote Control is unavailable with `CLAUDE_CODE_DISABLE_FEATURE_FLAGS`. `DISABLE_TELEMETRY` and `DO_NOT_TRACK` no longer block it on subscription plans. [[lines 32-457](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/claude-code/remote-control.md?plain=1#L32-L457)] [[Source](https://code.claude.com/docs/en/remote-control#requirements)]

#### [server-managed-settings](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/claude-code/server-managed-settings.md) [[Source](https://code.claude.com/docs/en/server-managed-settings)]

* New "Give groups different settings" section for Enterprise plans. It covers per-group configurations, ranking, a catch-all for everyone else, a "Check effective settings" tool, and the switch to group-based mode. Configurations don't merge. [[lines 107-145](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/claude-code/server-managed-settings.md?plain=1#L107-L145)] [[Source](https://code.claude.com/docs/en/server-managed-settings#give-groups-different-settings)]
* Team plans still apply one configuration to everyone. [[line 163](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/claude-code/server-managed-settings.md?plain=1#L163)] [[Source](https://code.claude.com/docs/en/server-managed-settings#current-limitations)]

#### [settings-reference](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/claude-code/settings-reference.md) [[Source](https://code.claude.com/docs/en/settings-reference)]

* Added `strictPluginOnlyCustomization.skills`, `.agents`, `.hooks`, and `.mcp` sub-keys. The key takes `true` or an array of types. [[lines 228-231](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/claude-code/settings-reference.md?plain=1#L228-L231), [lines 4170-4173](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/claude-code/settings-reference.md?plain=1#L4170-L4173)]
* The login-restriction setting now accepts `"gateway"` to send people to a cloud gateway. [[line 5277](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/claude-code/settings-reference.md?plain=1#L5277)] [[Source](https://code.claude.com/docs/en/settings-reference#forceloginmethod)]
* Fast mode setting updated for the supported models. The advisor setting notes Claude Platform on AWS support. [[lines 288-448](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/claude-code/settings-reference.md?plain=1#L288-L448)] [[Source](https://code.claude.com/docs/en/settings-reference#advisormodel)]

#### [whats-new](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/claude-code/whats-new.md) [[Source](https://code.claude.com/docs/en/whats-new)]

* Weekly digest links were adjusted for Weeks 35 to 37. Only the link lines changed. [[line 15](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/claude-code/whats-new.md?plain=1#L15)] [[Source](https://code.claude.com/docs/en/whats-new#whats-new)]

-----

## API changes

### New Documents

#### [build-with-claude/effort-per-message](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/api/build-with-claude/effort-per-message.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/effort-per-message)]

New beta page on changing the effort level partway through a conversation with a system message, so the prompt cache is kept. The beta header is `mid-conversation-output-config-2026-07-01`. It is supported on Fable 5.x, Mythos 5.x, Opus 5.5, Sonnet 5.5, and Haiku 5.5. It was split out of the Effort page.

#### [manage-claude/compliance-security-posture/check-events-against-results](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/api/manage-claude/compliance-security-posture/check-events-against-results.md) [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-security-posture/check-events-against-results)]

How to verify stored Security posture events against current results from the endpoint.

#### [manage-claude/compliance-security-posture/detect-changes](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/api/manage-claude/compliance-security-posture/detect-changes.md) [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-security-posture/detect-changes)]

How to alert on risky Security posture changes.

#### [manage-claude/compliance-security-posture/events-reference](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/api/manage-claude/compliance-security-posture/events-reference.md) [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-security-posture/events-reference)]

Reference for the events, including who accepted which risk, when, and until when.

#### [manage-claude/compliance-security-posture/ocsf-mapping](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/api/manage-claude/compliance-security-posture/ocsf-mapping.md) [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-security-posture/ocsf-mapping)]

How to map Security posture events to the Open Cybersecurity Schema Framework (OCSF).

#### [manage-claude/compliance-security-posture/overview](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/api/manage-claude/compliance-security-posture/overview.md) [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-security-posture/overview)]

Overview of what the Compliance API exposes about the claude.ai **Security posture** page (Security Center). It covers the change events and current results, and has a "Choose your path" guide.

#### [manage-claude/compliance-security-posture/results-reference](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/api/manage-claude/compliance-security-posture/results-reference.md) [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-security-posture/results-reference)]

Reference for the current-results endpoint, for building dashboards. It explains how an attestation shows in the response.

#### [manage-claude/compliance-security-posture/send-events](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/api/manage-claude/compliance-security-posture/send-events.md) [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-security-posture/send-events)]

How to send Security posture events to a SIEM, including a check if you already ingest the full Activity Feed.

### Changed documents

#### [about-claude/models/model-ids-and-versions](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/api/about-claude/models/model-ids-and-versions.md) [[Source](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions)]

* On `bedrock-runtime`, cross-region models such as Fable 5.2 and Mythos 5.2 take an inference profile ID with a prefix such as `global.` or `us.`. [[line 37](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/api/about-claude/models/model-ids-and-versions.md?plain=1#L37)] [[Source](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions#the-46-generation-and-later)]

#### [about-claude/pricing](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/api/about-claude/pricing.md) [[Source](https://platform.claude.com/docs/en/about-claude/pricing)]

* New per-model cache-hit pricing: 0.025x on Fable/Mythos 5.x, 0.05x on Opus 5.5 and Sonnet 5.5, and 0.1x on others. Also the break-even point for caching. [[lines 145-165](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/api/about-claude/pricing.md?plain=1#L145-L165)] [[Source](https://platform.claude.com/docs/en/about-claude/pricing#prompt-caching)]
* Fast mode section: up to 2.5x output speed for Fable 5.2, Opus 5.5, Opus 5, and Opus 4.8, with availability by platform. [[line 182](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/api/about-claude/pricing.md?plain=1#L182)] [[Source](https://platform.claude.com/docs/en/about-claude/pricing#fast-mode-pricing)]
* Toolset definition overhead is now documented: about 4,500 tokens for `computer_toolset_20260801` and about 6,600 for `browser_toolset_20260801`. [[lines 410-428](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/api/about-claude/pricing.md?plain=1#L410-L428)] [[Source](https://platform.claude.com/docs/en/about-claude/pricing#computer-use-tool)]
* The Claude Consumption Unit (CCU) billing tables were clarified for AWS and Azure Marketplaces. [[lines 88-126](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/api/about-claude/pricing.md?plain=1#L88-L126)] [[Source](https://platform.claude.com/docs/en/about-claude/pricing#claude-platform-on-aws-pricing)]

#### [agents-and-tools/tool-use/advisor-tool](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/api/agents-and-tools/tool-use/advisor-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool)]

* You can drop the advisor tool from `tools` while history still contains `advisor_tool_result` blocks, but you must keep sending the beta header. If the history also has thinking blocks, this counts as a `tools` edit and fails the prefix check, so the request gets a 400. Fix this with `prefix_mismatch_behavior: "drop_block"`. [[lines 745-757](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/api/agents-and-tools/tool-use/advisor-tool.md?plain=1#L745-L757)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool#multi-turn-conversations)]
* There is no conversation-level cap on advisor calls. Count them client-side and remove the tool at your ceiling. Keep the `caching` setting constant, because toggling it causes cache misses. [[lines 1430-1826](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/api/agents-and-tools/tool-use/advisor-tool.md?plain=1#L1430-L1826)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool#advisor-side-caching)]

#### [build-with-claude/cache-diagnostics](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/api/build-with-claude/cache-diagnostics.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/cache-diagnostics)]

* Include `diagnostics` on every turn, because it is the opt-in. On the first turn, pass `"previous_message_id": null`. The multi-turn examples now read `cache_miss_reason` across all SDKs. [[lines 50-940](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/api/build-with-claude/cache-diagnostics.md?plain=1#L50-L940)] [[Source](https://platform.claude.com/docs/en/build-with-claude/cache-diagnostics#basic-usage)]

#### [build-with-claude/compaction-threshold](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/api/build-with-claude/compaction-threshold.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/compaction-threshold)]

* Supported models now include Haiku 4.5. Beta availability was added for Amazon Bedrock (`bedrock-runtime`) and Claude Platform on AWS. The Java examples were rewritten as runnable programs. [[lines 25-460](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/api/build-with-claude/compaction-threshold.md?plain=1#L25-L460)] [[Source](https://platform.claude.com/docs/en/build-with-claude/compaction-threshold#append-the-response-including-any-compaction-block-to-continue-the-conversation)]

#### [build-with-claude/effort](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/api/build-with-claude/effort.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/effort)]

* The mid-conversation effort content moved to the new [effort-per-message](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/api/build-with-claude/effort-per-message.md) page, and this page is much shorter. [[line 408](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/api/build-with-claude/effort.md?plain=1#L408)] [[Source](https://platform.claude.com/docs/en/build-with-claude/effort#change-effort-mid-conversation)]

#### [build-with-claude/fast-mode](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/api/build-with-claude/fast-mode.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/fast-mode)]

* Updated model support and availability across platforms, to match the pricing page.

#### [build-with-claude/preserved-thinking](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/api/build-with-claude/preserved-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking)]

* New table of prefix-check enforcement per model and account creation date (cutoff August 31, 2026). It is always enforced with a 400 error on Fable 5.2 and Mythos 5.2, and varies by account for Fable 5.1, Opus 5.5, Sonnet 5.5, and Haiku 5.5. [[lines 47-62](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/api/build-with-claude/preserved-thinking.md?plain=1#L47-L62)] [[Source](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking#when-prefix_mismatch_behavior-is-unset)]
* The Message Batches API drops failing blocks instead of erroring when the field is unset. Added how to test which behavior your account gets, and a new `thinking_mismatch_allowed` entry in `input_transformations`. [[lines 62-117](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/api/build-with-claude/preserved-thinking.md?plain=1#L62-L117), [line 414](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/api/build-with-claude/preserved-thinking.md?plain=1#L414)]
* With compaction at a token threshold, the check covers `messages` only from the latest compaction block. Added Amazon Bedrock availability. [[line 94](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/api/build-with-claude/preserved-thinking.md?plain=1#L94)] [[Source](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking#keeping-the-prefix-unchanged)]

#### [build-with-claude/prompt-caching](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/api/build-with-claude/prompt-caching.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)]

* Substantially expanded (about 340 lines changed). See the diff for details.

#### [release-notes/overview](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/api/release-notes/overview.md) [[Source](https://platform.claude.com/docs/en/release-notes/overview)]

* The Fable 5.2 and Mythos 5.2 note now says they read other models' thinking blocks on the Claude API and Google Cloud (Google managed), so conversations moving onto them keep their reasoning. [[lines 17-19](https://github.com/gpambrozio/ClaudeDocs/blob/b62d81cf7251346db587924ef1221e0895fc3bdf/docs-md/api/release-notes/overview.md?plain=1#L17-L19)] [[Source](https://platform.claude.com/docs/en/release-notes/overview#november-9-2026)]

Many other API pages (the model overview and migration pages, SDK pages, tool-use pages, and others) received small wording, example, and consistency edits. These were not itemized.
