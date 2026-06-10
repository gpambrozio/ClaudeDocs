# [Claude docs changes for June 10th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/3d5a6866b6bfcec2daef36cb3365b4bb1c304807) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/3d5a6866b6bfcec2daef36cb3365b4bb1c304807)]

## Executive Summary
- Claude Fable 5 (Mythos-class model) is now generally available via Claude Code v2.1.170, with full documentation coverage across the API and advisor tool
- New server-side fallback and fallback credit beta features allow automatic retrying of refused Fable 5 requests on another model (e.g. Opus 4.8) without double-paying prompt cache costs
- Scheduled deployments are now documented for Managed Agents, enabling cron-based autonomous agent runs with full lifecycle management (pause, unpause, archive, manual run)
- New comprehensive advisor tool documentation for Claude Code, including Fable 5 model pairing support and billing details
- New Deployments and Deployment Runs API endpoints added across all SDK languages

## New Claude Code versions

### [2.1.170](https://github.com/gpambrozio/ClaudeDocs/blob/3d5a6866b6bfcec2daef36cb3365b4bb1c304807/versions/2.1.170.md)

#### New features

* Introduced Claude Fable 5: a Mythos-class model now available for general use, exceeding the capabilities of any previously generally-available model. Requires v2.1.170 for access.

#### Major bug fixes

* Fixed sessions not saving transcripts (and not appearing in `--resume`) when launched from the VS Code integrated terminal or any shell that inherited Claude Code environment variables.

-----

## Claude Code changes

### New Documents

#### [advisor](https://github.com/gpambrozio/ClaudeDocs/blob/3d5a6866b6bfcec2daef36cb3365b4bb1c304807/docs-md/claude-code/advisor.md) [[Source](https://code.claude.com/docs/en/advisor)]

New comprehensive document covering the advisor tool, which lets Claude consult a second (typically stronger) model at key decision points during a task. Covers how to enable the advisor via `/advisor` command, `advisorModel` setting, or `--advisor` flag; supported model pairings (including Fable 5 as both main and advisor model starting from v2.1.170); billing details; prompt caching behavior; and comparison with related features like `opusplan` and subagents.

-----

## API changes

### New Documents

#### [api/beta/deployment_runs](https://github.com/gpambrozio/ClaudeDocs/blob/3d5a6866b6bfcec2daef36cb3365b4bb1c304807/docs-md/api/api/beta/deployment_runs.md) [[Source](https://platform.claude.com/docs/en/api/beta/deployment_runs)]

New API reference for the Deployment Runs resource. Documents the `BetaManagedAgentsDeploymentRun` object and lists endpoints to retrieve and list deployment run records, which track individual scheduled or manual deployment execution attempts including session creation success/failure.

#### [api/beta/deployments](https://github.com/gpambrozio/ClaudeDocs/blob/3d5a6866b6bfcec2daef36cb3365b4bb1c304807/docs-md/api/api/beta/deployments.md) [[Source](https://platform.claude.com/docs/en/api/beta/deployments)]

New API reference for the Deployments resource. Documents CRUD endpoints plus lifecycle operations: create, list, retrieve, update, archive, pause, unpause, and manually run a deployment. The `BetaManagedAgentsDeployment` object includes schedule configuration (cron expression, timezone, upcoming run times), pause/archive status, and agent/environment references.

#### [build-with-claude/fallback-credit](https://github.com/gpambrozio/ClaudeDocs/blob/3d5a6866b6bfcec2daef36cb3365b4bb1c304807/docs-md/api/build-with-claude/fallback-credit.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/fallback-credit)]

New guide covering the fallback credit beta feature, which avoids double-billing prompt cache write costs when retrying a refused Fable 5 request on another model. Documents the opt-in flow using the `fallback-credit-2026-06-01` beta header, how to read `fallback_credit_token` and `fallback_has_prefill_claim` from a refusal's `stop_details`, how to construct the retry request, and error handling for rejected token redemptions.

#### [build-with-claude/refusals-and-fallback](https://github.com/gpambrozio/ClaudeDocs/blob/3d5a6866b6bfcec2daef36cb3365b4bb1c304807/docs-md/api/build-with-claude/refusals-and-fallback.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback)]

New guide covering how to detect and handle Fable 5 refusals (`stop_reason: "refusal"`). Documents `stop_details` fields (`category`, `explanation`), when refusals are billed, and three fallback strategies: server-side fallback (single API call with `fallbacks` parameter and `server-side-fallback-2026-06-01` beta header), SDK middleware (`BetaRefusalFallbackMiddleware`), and manual retry with fallback credit. Includes pitfalls, streaming behavior, and how to handle refusals in Message Batches.

#### [managed-agents/scheduled-deployments](https://github.com/gpambrozio/ClaudeDocs/blob/3d5a6866b6bfcec2daef36cb3365b4bb1c304807/docs-md/api/managed-agents/scheduled-deployments.md) [[Source](https://platform.claude.com/docs/en/managed-agents/scheduled-deployments)]

New guide for scheduled deployments in Managed Agents. Documents how to create a deployment with a cron schedule and timezone (IANA), how deployment runs track execution history (success and failure), lifecycle management (pause, unpause, archive), failure behavior for rate limits and archived resources, and how to trigger a manual run outside the schedule.

### Changed documents

#### [agents-and-tools/tool-use/advisor-tool](https://github.com/gpambrozio/ClaudeDocs/blob/3d5a6866b6bfcec2daef36cb3365b4bb1c304807/docs-md/api/agents-and-tools/tool-use/advisor-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool)]

* Added Claude Fable 5 (`claude-fable-5`) and Claude Mythos 5 (`claude-mythos-5`) as supported executor/advisor model pairings. Both models can only advise themselves. [[line 37](https://github.com/gpambrozio/ClaudeDocs/blob/3d5a6866b6bfcec2daef36cb3365b4bb1c304807/docs-md/api/agents-and-tools/tool-use/advisor-tool.md?plain=1#L37)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool)]

#### [api/beta](https://github.com/gpambrozio/ClaudeDocs/blob/3d5a6866b6bfcec2daef36cb3365b4bb1c304807/docs-md/api/api/beta.md) [[Source](https://platform.claude.com/docs/en/api/beta)]

* Added two new beta header values: `server-side-fallback-2026-06-01` and `fallback-credit-2026-06-01` to the `AnthropicBeta` enum.
* Added `claude-fable-5` ("Next generation of intelligence for the hardest knowledge work and coding problems") and `claude-mythos-5` ("Most capable model for cybersecurity and biology research") to the model enum.
* Added `allowed_fallback_models` field to `BetaModelInfo` — lists model IDs accepted as `fallbacks[i].model` on the Messages API; empty list means `fallbacks` parameter is not supported for that model as primary.

#### [api/beta/messages/create](https://github.com/gpambrozio/ClaudeDocs/blob/3d5a6866b6bfcec2daef36cb3365b4bb1c304807/docs-md/api/api/beta/messages/create.md) [[Source](https://platform.claude.com/docs/en/api/beta/messages/create)]

* Added new `fallbacks` request parameter — an optional array of fallback model configurations to retry when Fable 5 refuses.
* Added `fallback_credit_token` request parameter — pass the token from a prior refusal's `stop_details` to avoid double-paying prompt cache costs on retry.
* Added new `BetaFallbackBlockParam` content block type — echoed back from a prior response at model-handoff boundaries; position is load-bearing for thinking verification hash chains.
* Added `stop_details` on responses with new `fallback_credit_token` and `fallback_has_prefill_claim` fields for refusal handling.

#### [api/beta/models/list](https://github.com/gpambrozio/ClaudeDocs/blob/3d5a6866b6bfcec2daef36cb3365b4bb1c304807/docs-md/api/api/beta/models/list.md) [[Source](https://platform.claude.com/docs/en/api/beta/models/list)]

* Added `allowed_fallback_models` field to the `BetaModelInfo` response object, listing model IDs this model accepts as fallback targets on the Messages API.
