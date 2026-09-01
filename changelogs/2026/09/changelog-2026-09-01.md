# [Claude docs changes for September 1st, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/ae60f34c65b80d9abe1c2852641c85a9340905a1) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/ae60f34c65b80d9abe1c2852641c85a9340905a1)]

## Executive Summary
- New "account on hold" handling: a suspended Claude account now gets a dedicated error state and structured error code (`account_on_hold`) across the CLI, hooks, and Agent SDK, instead of being reported as a generic expired login.
- Sandbox settings that let the sandbox proxy read/reroute/authenticate traffic or weaken isolation (`sandbox.network.tlsTerminate`, proxy ports, `sandbox.credentials`, and others) now require developer approval when delivered via server-managed settings — previously applied silently.
- One-off routine scheduling from the CLI (`/schedule`) is now generally available, and `/schedule` no longer depends on feature-flag fetching.
- Subagents running in the background by default (introduced gradually in v2.1.198) is now fully rolled out, and `/tasks` now shows which model and effort level a subagent is running on.
- Code execution and programmatic tool calling now support Claude Fable 5 and Claude Mythos 5, and cross-account KMS keys are no longer supported for Claude Platform on AWS CMEK.

## New Claude Code versions

### [2.1.252](https://github.com/gpambrozio/ClaudeDocs/blob/ae60f34c65b80d9abe1c2852641c85a9340905a1/versions/2.1.252.md)

#### Major bug fixes

* Fixed Bash commands failing with "task output swap refused (tasks dir moved or linked)" on some Macs
* Fixed "always allow" not saving in a project that has no `.claude/settings.local.json` yet
* Fixed Remote Control sessions hosted by Claude Desktop or VS Code stalling for minutes after a tool finished when the connection to claude.ai was degraded
* Fixed background task notifications with very large failure output (for example git errors on a full disk) making the conversation exceed the API request size limit

-----

## Claude Code changes

### Changed documents

#### [agent-sdk/subagents](https://github.com/gpambrozio/ClaudeDocs/blob/ae60f34c65b80d9abe1c2852641c85a9340905a1/docs-md/claude-code/agent-sdk/subagents.md) [[Source](https://code.claude.com/docs/en/agent-sdk/subagents)]

* Subagents running in the background by default is now fully rolled out; before v2.1.198 an Agent tool call omitting `run_in_background` ran synchronously. [[line 154](https://github.com/gpambrozio/ClaudeDocs/blob/ae60f34c65b80d9abe1c2852641c85a9340905a1/docs-md/claude-code/agent-sdk/subagents.md?plain=1#L154)] [[Source](https://code.claude.com/docs/en/agent-sdk/subagents#create-subagents)]
* Clarified that the built-in `general-purpose` subagent is available even when you define no agents of your own, and documented the `subagent_type is required` error returned when `CLAUDE_AGENT_SDK_DISABLE_BUILTIN_AGENTS=1` removes it. [[line 161](https://github.com/gpambrozio/ClaudeDocs/blob/ae60f34c65b80d9abe1c2852641c85a9340905a1/docs-md/claude-code/agent-sdk/subagents.md?plain=1#L161)] [[Source](https://code.claude.com/docs/en/agent-sdk/subagents#create-subagents)]

#### [agent-sdk/typescript](https://github.com/gpambrozio/ClaudeDocs/blob/ae60f34c65b80d9abe1c2852641c85a9340905a1/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* Added `'account_on_hold'` as a new `SDKAssistantMessageError` value, returned when the authenticated account is suspended. [[line 1139](https://github.com/gpambrozio/ClaudeDocs/blob/ae60f34c65b80d9abe1c2852641c85a9340905a1/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L1139)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#sdkassistantmessage)]

#### [amazon-bedrock](https://github.com/gpambrozio/ClaudeDocs/blob/ae60f34c65b80d9abe1c2852641c85a9340905a1/docs-md/claude-code/amazon-bedrock.md) [[Source](https://code.claude.com/docs/en/amazon-bedrock)]

* Guardrail headers delivered through a Claude apps gateway policy now count as settings that need developer approval. [[line 371](https://github.com/gpambrozio/ClaudeDocs/blob/ae60f34c65b80d9abe1c2852641c85a9340905a1/docs-md/claude-code/amazon-bedrock.md?plain=1#L371)] [[Source](https://code.claude.com/docs/en/amazon-bedrock#aws-guardrails)]

#### [claude-apps-gateway](https://github.com/gpambrozio/ClaudeDocs/blob/ae60f34c65b80d9abe1c2852641c85a9340905a1/docs-md/claude-code/claude-apps-gateway.md) [[Source](https://code.claude.com/docs/en/claude-apps-gateway)]

* When a gateway's pinned TLS certificate rotates, developers now also see the security approval dialog again (not just the trust prompt), since approval memory is keyed to the pinned certificate. [[line 233](https://github.com/gpambrozio/ClaudeDocs/blob/ae60f34c65b80d9abe1c2852641c85a9340905a1/docs-md/claude-code/claude-apps-gateway.md?plain=1#L233)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway#steps)]

#### [claude-apps-gateway-config](https://github.com/gpambrozio/ClaudeDocs/blob/ae60f34c65b80d9abe1c2852641c85a9340905a1/docs-md/claude-code/claude-apps-gateway-config.md) [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config)]

* Added sandbox settings that intercept traffic, inject credentials, or weaken isolation (e.g. `sandbox.network.tlsTerminate`, the proxy port settings) to the list of settings a gateway policy can only deliver with developer approval. [[line 566](https://github.com/gpambrozio/ClaudeDocs/blob/ae60f34c65b80d9abe1c2852641c85a9340905a1/docs-md/claude-code/claude-apps-gateway-config.md?plain=1#L566)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config#required-sections)]

#### [costs](https://github.com/gpambrozio/ClaudeDocs/blob/ae60f34c65b80d9abe1c2852641c85a9340905a1/docs-md/claude-code/costs.md) [[Source](https://code.claude.com/docs/en/costs)]

* In self-serve Enterprise, Enterprise trial, and AWS-Marketplace-billed Enterprise organizations, `/usage-credits` now requires Claude Code v2.1.248 or later; earlier versions reject it. [[line 76](https://github.com/gpambrozio/ClaudeDocs/blob/ae60f34c65b80d9abe1c2852641c85a9340905a1/docs-md/claude-code/costs.md?plain=1#L76)] [[Source](https://code.claude.com/docs/en/costs#add-usage-credits-to-your-subscription)]

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/ae60f34c65b80d9abe1c2852641c85a9340905a1/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* An `ANTHROPIC_CUSTOM_HEADERS` value that sets a credential, org/tenant, routing, or API-behavior header now counts as a setting that needs developer approval when delivered via server-managed settings. [[line 125](https://github.com/gpambrozio/ClaudeDocs/blob/ae60f34c65b80d9abe1c2852641c85a9340905a1/docs-md/claude-code/env-vars.md?plain=1#L125)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* `CLAUDE_CODE_AUTO_COMPACT_WINDOW` is now also capped at the model's context window. [[line 192](https://github.com/gpambrozio/ClaudeDocs/blob/ae60f34c65b80d9abe1c2852641c85a9340905a1/docs-md/claude-code/env-vars.md?plain=1#L192)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB` now also strips any variable Claude Code recognizes as a credential and credentials embedded in package registry URLs, not just the fixed Anthropic/cloud-provider list. [[line 344](https://github.com/gpambrozio/ClaudeDocs/blob/ae60f34c65b80d9abe1c2852641c85a9340905a1/docs-md/claude-code/env-vars.md?plain=1#L344)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* With feature-flag fetching off, messaging sessions beyond the local machine is now also unavailable, while scheduling from the CLI with `/schedule` no longer needs feature-flag fetching (see the `routines` entry below). [[line 480](https://github.com/gpambrozio/ClaudeDocs/blob/ae60f34c65b80d9abe1c2852641c85a9340905a1/docs-md/claude-code/env-vars.md?plain=1#L480)] [[Source](https://code.claude.com/docs/en/env-vars#features-that-need-feature-flag-fetching)]

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/ae60f34c65b80d9abe1c2852641c85a9340905a1/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* New "Your account is on hold" section, covering the `account_on_hold` structured error code shown when a Claude account is suspended; before v2.1.235 this was reported as a generic "Login expired" instead. [[lines 917-925](https://github.com/gpambrozio/ClaudeDocs/blob/ae60f34c65b80d9abe1c2852641c85a9340905a1/docs-md/claude-code/errors.md?plain=1#L917-L925)] [[Source](https://code.claude.com/docs/en/errors#authentication-errors)]

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/ae60f34c65b80d9abe1c2852641c85a9340905a1/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* Added `account_on_hold` to the `StopFailure` error type values, in both the matcher table and the hook input field reference. [[line 294](https://github.com/gpambrozio/ClaudeDocs/blob/ae60f34c65b80d9abe1c2852641c85a9340905a1/docs-md/claude-code/hooks.md?plain=1#L294)] [[Source](https://code.claude.com/docs/en/hooks#stopfailure)]

#### [hooks-guide](https://github.com/gpambrozio/ClaudeDocs/blob/ae60f34c65b80d9abe1c2852641c85a9340905a1/docs-md/claude-code/hooks-guide.md) [[Source](https://code.claude.com/docs/en/hooks-guide)]

* Added `account_on_hold` to the `StopFailure` error type values in the matcher-field table. [[line 659](https://github.com/gpambrozio/ClaudeDocs/blob/ae60f34c65b80d9abe1c2852641c85a9340905a1/docs-md/claude-code/hooks-guide.md?plain=1#L659)] [[Source](https://code.claude.com/docs/en/hooks-guide#filter-hooks-with-matchers)]

#### [llm-gateway-connect](https://github.com/gpambrozio/ClaudeDocs/blob/ae60f34c65b80d9abe1c2852641c85a9340905a1/docs-md/claude-code/llm-gateway-connect.md) [[Source](https://code.claude.com/docs/en/llm-gateway-connect)]

* Routing and tenant header names set via `ANTHROPIC_CUSTOM_HEADERS` now count as headers that need developer approval. [[line 278](https://github.com/gpambrozio/ClaudeDocs/blob/ae60f34c65b80d9abe1c2852641c85a9340905a1/docs-md/claude-code/llm-gateway-connect.md?plain=1#L278)] [[Source](https://code.claude.com/docs/en/llm-gateway-connect#send-additional-headers)]

#### [monitoring-usage](https://github.com/gpambrozio/ClaudeDocs/blob/ae60f34c65b80d9abe1c2852641c85a9340905a1/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* When a `PreToolUse` hook defers a tool call, Claude Code now preserves the trace context so the tool's spans join the original turn's trace as children when the session resumes. [[line 170](https://github.com/gpambrozio/ClaudeDocs/blob/ae60f34c65b80d9abe1c2852641c85a9340905a1/docs-md/claude-code/monitoring-usage.md?plain=1#L170)] [[Source](https://code.claude.com/docs/en/monitoring-usage#traces-beta)]

#### [routines](https://github.com/gpambrozio/ClaudeDocs/blob/ae60f34c65b80d9abe1c2852641c85a9340905a1/docs-md/claude-code/routines.md) [[Source](https://code.claude.com/docs/en/routines)]

* One-off scheduling from the CLI is now generally available; it was previously a gradual rollout, with a fallback to the web UI. [[line 114](https://github.com/gpambrozio/ClaudeDocs/blob/ae60f34c65b80d9abe1c2852641c85a9340905a1/docs-md/claude-code/routines.md?plain=1#L114)] [[Source](https://code.claude.com/docs/en/routines#schedule-a-one-off-run)]
* `/schedule` no longer depends on feature-flag fetching, so it now works even with `DISABLE_TELEMETRY`, `DO_NOT_TRACK`, `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC`, or `DISABLE_GROWTHBOOK` set. [[line 347](https://github.com/gpambrozio/ClaudeDocs/blob/ae60f34c65b80d9abe1c2852641c85a9340905a1/docs-md/claude-code/routines.md?plain=1#L347)] [[Source](https://code.claude.com/docs/en/routines#schedule-returns-unknown-command)]

#### [sandboxing](https://github.com/gpambrozio/ClaudeDocs/blob/ae60f34c65b80d9abe1c2852641c85a9340905a1/docs-md/claude-code/sandboxing.md) [[Source](https://code.claude.com/docs/en/sandboxing)]

* Sandbox `mask` entries, `network.tlsTerminate`, and `credentials.allowPlaintextInject` delivered via server-managed settings now count as settings needing developer approval. [[line 489](https://github.com/gpambrozio/ClaudeDocs/blob/ae60f34c65b80d9abe1c2852641c85a9340905a1/docs-md/claude-code/sandboxing.md?plain=1#L489)] [[Source](https://code.claude.com/docs/en/sandboxing#mask-credentials)]

#### [server-managed-settings](https://github.com/gpambrozio/ClaudeDocs/blob/ae60f34c65b80d9abe1c2852641c85a9340905a1/docs-md/claude-code/server-managed-settings.md) [[Source](https://code.claude.com/docs/en/server-managed-settings)]

* New "Sandbox network and isolation settings" category requiring developer approval: settings that let the sandbox proxy read, reroute, or authenticate traffic, or that weaken isolation (`sandbox.network.tlsTerminate`, the proxy port settings, `sandbox.credentials`, `sandbox.allowAppleEvents`, `sandbox.enableWeakerNestedSandbox`, `sandbox.enableWeakerNetworkIsolation`, `sandbox.filesystem.disabled`, and the Unix-socket/Mach-lookup settings). Before v2.1.251 Claude Code applied these without approval. [[line 197](https://github.com/gpambrozio/ClaudeDocs/blob/ae60f34c65b80d9abe1c2852641c85a9340905a1/docs-md/claude-code/server-managed-settings.md?plain=1#L197)] [[Source](https://code.claude.com/docs/en/server-managed-settings#security-approval-dialogs)]
* Approval for a Claude apps gateway sign-in is now scoped per gateway and tied to its pinned certificate, rather than following the generic "any other credential" rule. [[line 209](https://github.com/gpambrozio/ClaudeDocs/blob/ae60f34c65b80d9abe1c2852641c85a9340905a1/docs-md/claude-code/server-managed-settings.md?plain=1#L209)] [[Source](https://code.claude.com/docs/en/server-managed-settings#security-approval-dialogs)]
* Documented exactly which `ANTHROPIC_CUSTOM_HEADERS` values require approval based on their content (credential, org/tenant, routing, or API-behavior headers) as of v2.1.251; previously any value applied without approval. [[line 239](https://github.com/gpambrozio/ClaudeDocs/blob/ae60f34c65b80d9abe1c2852641c85a9340905a1/docs-md/claude-code/server-managed-settings.md?plain=1#L239)] [[Source](https://code.claude.com/docs/en/server-managed-settings#security-approval-dialogs)]

#### [sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/ae60f34c65b80d9abe1c2852641c85a9340905a1/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* `/tasks` now shows which model a subagent is running on, plus its effort level when the subagent's definition (or the skill it forked from) sets one. Requires Claude Code v2.1.242 or later. [[line 312](https://github.com/gpambrozio/ClaudeDocs/blob/ae60f34c65b80d9abe1c2852641c85a9340905a1/docs-md/claude-code/sub-agents.md?plain=1#L312)] [[Source](https://code.claude.com/docs/en/sub-agents#choose-a-model)]
* Claude Code now shows a startup warning when subagents' combined descriptions pass a 15,000-token limit; every subagent still loads. [[line 684](https://github.com/gpambrozio/ClaudeDocs/blob/ae60f34c65b80d9abe1c2852641c85a9340905a1/docs-md/claude-code/sub-agents.md?plain=1#L684)] [[Source](https://code.claude.com/docs/en/sub-agents#understand-automatic-delegation)]

-----

## API changes

### Changed documents

#### [agents-and-tools/agent-skills/enterprise](https://github.com/gpambrozio/ClaudeDocs/blob/ae60f34c65b80d9abe1c2852641c85a9340905a1/docs-md/api/agents-and-tools/agent-skills/enterprise.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/enterprise)]

* Skill content scanning for Claude Enterprise organizations is no longer marked as a beta feature. [[lines 43-45](https://github.com/gpambrozio/ClaudeDocs/blob/ae60f34c65b80d9abe1c2852641c85a9340905a1/docs-md/api/agents-and-tools/agent-skills/enterprise.md?plain=1#L43-L45)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/enterprise#skill-content-scanning)]

#### [agents-and-tools/tool-use/code-execution-tool](https://github.com/gpambrozio/ClaudeDocs/blob/ae60f34c65b80d9abe1c2852641c85a9340905a1/docs-md/api/agents-and-tools/tool-use/code-execution-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool)]

* The code execution tool's compatibility table now lists Claude Fable 5 and Claude Mythos 5 as supported models, and notes that Claude Mythos Preview supports it on the Claude API and Microsoft Foundry. [[lines 622-632](https://github.com/gpambrozio/ClaudeDocs/blob/ae60f34c65b80d9abe1c2852641c85a9340905a1/docs-md/api/agents-and-tools/tool-use/code-execution-tool.md?plain=1#L622-L632)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool#compatibility)]

#### [agents-and-tools/tool-use/programmatic-tool-calling](https://github.com/gpambrozio/ClaudeDocs/blob/ae60f34c65b80d9abe1c2852641c85a9340905a1/docs-md/api/agents-and-tools/tool-use/programmatic-tool-calling.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling)]

* The compatibility table now lists Claude Fable 5 and Claude Mythos 5 as supported models, and notes that Claude Haiku 4.5 accepts the required tool version but doesn't support programmatic tool calling. [[lines 736-746](https://github.com/gpambrozio/ClaudeDocs/blob/ae60f34c65b80d9abe1c2852641c85a9340905a1/docs-md/api/agents-and-tools/tool-use/programmatic-tool-calling.md?plain=1#L736-L746)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling#compatibility)]

#### [build-with-claude/token-counting](https://github.com/gpambrozio/ClaudeDocs/blob/ae60f34c65b80d9abe1c2852641c85a9340905a1/docs-md/api/build-with-claude/token-counting.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/token-counting)]

* Token-counting endpoint rate limits raised across all usage tiers: Start 2,000 → 5,000 RPM, Build 4,000 → 10,000 RPM, Scale 8,000 → 20,000 RPM. [[lines 242-246](https://github.com/gpambrozio/ClaudeDocs/blob/ae60f34c65b80d9abe1c2852641c85a9340905a1/docs-md/api/build-with-claude/token-counting.md?plain=1#L242-L246)] [[Source](https://platform.claude.com/docs/en/build-with-claude/token-counting#pricing-and-rate-limits)]

#### [manage-claude/cmek-aws-kms](https://github.com/gpambrozio/ClaudeDocs/blob/ae60f34c65b80d9abe1c2852641c85a9340905a1/docs-md/api/manage-claude/cmek-aws-kms.md) [[Source](https://platform.claude.com/docs/en/manage-claude/cmek-aws-kms)]

* Cross-account KMS keys are no longer supported for Claude Platform on AWS: the key must now be in the AWS account that hosts your organization, checked at registration time. [[line 211](https://github.com/gpambrozio/ClaudeDocs/blob/ae60f34c65b80d9abe1c2852641c85a9340905a1/docs-md/api/manage-claude/cmek-aws-kms.md?plain=1#L211)] [[Source](https://platform.claude.com/docs/en/manage-claude/cmek-aws-kms)]

#### [manage-claude/inference-hooks-endpoint](https://github.com/gpambrozio/ClaudeDocs/blob/ae60f34c65b80d9abe1c2852641c85a9340905a1/docs-md/api/manage-claude/inference-hooks-endpoint.md) [[Source](https://platform.claude.com/docs/en/manage-claude/inference-hooks-endpoint)]

* Documented circuit-breaker auto-recovery: starting 10 minutes after a trip, Anthropic sends about one test request per minute to your AI security server, and a valid verdict automatically resets the breaker (an admin can still reset it manually at any time). [[lines 263-267](https://github.com/gpambrozio/ClaudeDocs/blob/ae60f34c65b80d9abe1c2852641c85a9340905a1/docs-md/api/manage-claude/inference-hooks-endpoint.md?plain=1#L263-L267)] [[Source](https://platform.claude.com/docs/en/manage-claude/inference-hooks-endpoint#circuit-breaker)]

*Note: several `manage-claude` pages (`admin-api-keys`, `api-and-data-retention`, `compliance-api-access`, `compliance-sessions`, `inference-hooks`) broadened their wording from "Cowork and Claude Code sessions" to "sessions" / "apps such as Cowork and Claude Code," suggesting the Compliance API's session capture now covers more apps than before; no other content changed on those pages, so they're summarized here rather than listed individually.*

PENDING: awaiting remaining background analysis of docs-md/api/api/compliance, docs-md/api/api top-level, docs-md/api/about-claude.
