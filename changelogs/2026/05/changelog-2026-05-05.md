# [Claude docs changes for May 5th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/387ac4913cbc790d05bce4604e1ebf04f7b85603) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/387ac4913cbc790d05bce4604e1ebf04f7b85603)]

## Executive Summary
- **Workload Identity Federation** launched as a new API authentication method, letting production workloads authenticate using short-lived OIDC tokens from AWS, GCP, Azure, GitHub Actions, Kubernetes, and Okta — eliminating long-lived static API keys
- **Agent loop documentation** completely rewritten from a 500 error page into comprehensive coverage of turns, messages, tool execution, context management, sessions, and hooks
- **EnterWorktree critical fix**: the SDK's `EnterWorktree` was branching from `origin/<default-branch>` instead of local HEAD, silently dropping unpushed commits
- **Sub-agent prompt cache fix**: sub-agent progress summaries were missing prompt cache hits, causing ~3× excess `cache_creation` token usage
- **Extensive theme token additions** for terminal-config: 10+ new customization tokens including usage meter colors, speaker labels, hover states, and `ultrathink`/`ultraplan` rainbow gradient tokens

## New Claude Code versions

### [2.1.128](https://github.com/gpambrozio/ClaudeDocs/blob/387ac4913cbc790d05bce4604e1ebf04f7b85603/versions/2.1.128.md)

#### New features

* Bare `/color` (no args) now picks a random session color
* `/mcp` now shows the tool count for connected servers and flags servers that connected with 0 tools
* `--plugin-dir` now accepts `.zip` plugin archives in addition to directories
* `--channels` now works with console (API key) authentication — console orgs with managed settings must set `channelsEnabled: true` to enable

#### Existing feature improvements

* Updated `/model` picker: collapsed duplicate Opus 4.7 entries, and current Opus now shows as "Opus" instead of "Opus 4.7"
* Subprocesses (Bash, hooks, MCP, LSP) no longer inherit `OTEL_*` environment variables, so OTEL-instrumented apps run via the Bash tool no longer pick up the CLI's own OTLP endpoint
* Reconnecting MCP servers no longer flood the conversation with full tool-name lists on every reconnect — re-announced tools are summarized by server prefix
* SDK hosts receive a persistent `localSettings` suggestion for Bash permission prompts, so "Always allow" writes to `.claude/settings.local.json`
* `EnterWorktree` now creates the new branch from local HEAD as documented, instead of `origin/<default-branch>` — unpushed commits are no longer dropped
* Auto mode: when the classifier can't evaluate an action, the error now includes a hint (retry, `/compact`, or run with `--debug`)
* Headless `--output-format stream-json`: `init.plugin_errors` now includes `--plugin-dir` load failures in addition to dependency demotions

#### Major bug fixes

* Fixed crash loop when piping very large input (>10 MB) to `claude -p` via stdin
* Fixed Bedrock default model resolving to `global.*` instead of the region-appropriate prefix
* Fixed sub-agent progress summaries missing the prompt cache (~3× `cache_creation` reduction)
* Fixed MCP tool results dropping images when the server returns both structured content and content blocks
* Fixed sessions on 1M-context models with a smaller autocompact window being falsely blocked with "Prompt is too long" before reaching the actual API limit
* Fixed parallel shell tool calls: a failing read-only command (grep, git diff, ls) no longer cancels sibling calls
* Fixed `/plugin update` never detecting new versions of npm-sourced plugins
* Fixed MCP stdio servers receiving corrupted arguments when `CLAUDE_CODE_SHELL_PREFIX` is set and an argument contains spaces or shell metacharacters
* Fixed sub-agent summaries firing repeatedly while a sub-agent's transcript is static, capping worst-case token cost on idle sub-agents
* Fixed stale `installed_plugins.json` entries pointing at deleted cache directories polluting PATH
* Fixed markdown link labels being lost on terminals without OSC 8 hyperlink support — links now render as `label (url)` instead of just the URL
* Fixed vim mode: `Space` in NORMAL mode now moves the cursor right, matching standard vi/vim behavior
* Fixed terminal progress indicator (OSC 9;4) flickering off between tool calls — stays visible across the full turn

-----

## Claude Code changes

### New Documents

#### [agent-sdk/agent-loop](https://github.com/gpambrozio/ClaudeDocs/blob/387ac4913cbc790d05bce4604e1ebf04f7b85603/docs-md/claude-code/agent-sdk/agent-loop.md) [[Source](https://code.claude.com/docs/en/agent-sdk/agent-loop)]

Previously returned a 500 error; now contains comprehensive documentation of how the Agent SDK's agent loop works. Covers the full turn cycle (prompt → evaluate → tool execution → repeat), message types (`SystemMessage`, `AssistantMessage`, `UserMessage`, `StreamEvent`, `ResultMessage`), built-in tools and permissions, `max_turns`/`max_budget_usd` limits, effort levels, permission modes, context window management and automatic compaction, session continuity, result subtypes, and hooks. Includes Python and TypeScript code examples throughout.

### Changed documents

#### [features-overview](https://github.com/gpambrozio/ClaudeDocs/blob/387ac4913cbc790d05bce4604e1ebf04f7b85603/docs-md/claude-code/features-overview.md) [[Source](https://code.claude.com/docs/en/features-overview)]

* Added "Context window impact" row to the skills vs. subagents comparison table, clarifying that skills add to the main context window while subagents use a separate window with their own input/output token budget. [[line 80](https://github.com/gpambrozio/ClaudeDocs/blob/387ac4913cbc790d05bce4604e1ebf04f7b85603/docs-md/claude-code/features-overview.md?plain=1#L80)] [[Source](https://code.claude.com/docs/en/features-overview#compare-similar-features)]

#### [hooks-guide](https://github.com/gpambrozio/ClaudeDocs/blob/387ac4913cbc790d05bce4604e1ebf04f7b85603/docs-md/claude-code/hooks-guide.md) [[Source](https://code.claude.com/docs/en/hooks-guide)]

* Clarified the behavior of `ok: false` in LLM hooks per event type: `Stop`/`SubagentStop` feed the reason back to Claude; `PreToolUse` denies the tool and returns the reason as a tool error (so Claude can adjust and continue); `PostToolUse`, `PostToolBatch`, `UserPromptSubmit`, and `UserPromptExpansion` end the turn and show the reason as a warning. [[lines 701-704](https://github.com/gpambrozio/ClaudeDocs/blob/387ac4913cbc790d05bce4604e1ebf04f7b85603/docs-md/claude-code/hooks-guide.md?plain=1#L701-L704)] [[Source](https://code.claude.com/docs/en/hooks-guide#prompt-based-hooks)]

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/387ac4913cbc790d05bce4604e1ebf04f7b85603/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* Expanded the LLM hook `ok: false` reference to document behavior for all events, including `PostToolUseFailure`, `TaskCreated`, and `TaskCompleted` (reason returned as a tool error), and `PermissionRequest` (`ok: false` has no effect — use a command hook's `hookSpecificOutput.decision.behavior: "deny"` instead). [[lines 2318-2329](https://github.com/gpambrozio/ClaudeDocs/blob/387ac4913cbc790d05bce4604e1ebf04f7b85603/docs-md/claude-code/hooks.md?plain=1#L2318-L2329)] [[Source](https://code.claude.com/docs/en/hooks#response-schema)]

#### [monitoring-usage](https://github.com/gpambrozio/ClaudeDocs/blob/387ac4913cbc790d05bce4604e1ebf04f7b85603/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* Expanded the `source` field in the Tool decision event with full descriptions for each value (`"config"`, `"hook"`, `"user_permanent"`, `"user_temporary"`, `"user_abort"`, `"user_reject"`), explaining when each is emitted and whether it counts as accept or reject. [[lines 595-602](https://github.com/gpambrozio/ClaudeDocs/blob/387ac4913cbc790d05bce4604e1ebf04f7b85603/docs-md/claude-code/monitoring-usage.md?plain=1#L595-L602)] [[Source](https://code.claude.com/docs/en/monitoring-usage#tool-decision-event)]

#### [sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/387ac4913cbc790d05bce4604e1ebf04f7b85603/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* Fixed built-in agent name casing: "Claude Code Guide" corrected to `claude-code-guide`. [[line 70](https://github.com/gpambrozio/ClaudeDocs/blob/387ac4913cbc790d05bce4604e1ebf04f7b85603/docs-md/claude-code/sub-agents.md?plain=1#L70)] [[Source](https://code.claude.com/docs/en/sub-agents#built-in-subagents)]
* Added a Windows PowerShell tab for the `--agents` flag JSON example, showing the `@'...'@` here-string syntax needed on PowerShell. [[lines 181-213](https://github.com/gpambrozio/ClaudeDocs/blob/387ac4913cbc790d05bce4604e1ebf04f7b85603/docs-md/claude-code/sub-agents.md?plain=1#L181-L213)] [[Source](https://code.claude.com/docs/en/sub-agents#choose-the-subagent-scope)]
* Clarified session reload behavior: subagents added or edited directly on disk require a session restart, but subagents created through the `/agents` interface take effect immediately without a restart. [[line 227](https://github.com/gpambrozio/ClaudeDocs/blob/387ac4913cbc790d05bce4604e1ebf04f7b85603/docs-md/claude-code/sub-agents.md?plain=1#L227)] [[Source](https://code.claude.com/docs/en/sub-agents#write-subagent-files)]
* Added Windows PowerShell guidance for hook scripts in subagent definitions, linking to the hooks doc for the `shell: powershell` entry. [[line 486](https://github.com/gpambrozio/ClaudeDocs/blob/387ac4913cbc790d05bce4604e1ebf04f7b85603/docs-md/claude-code/sub-agents.md?plain=1#L486)] [[Source](https://code.claude.com/docs/en/sub-agents#conditional-rules-with-hooks)]

#### [terminal-config](https://github.com/gpambrozio/ClaudeDocs/blob/387ac4913cbc790d05bce4604e1ebf04f7b85603/docs-md/claude-code/terminal-config.md) [[Source](https://code.claude.com/docs/en/terminal-config)]

* Added new `suggestion` theme token for autocomplete suggestions and picker selection highlight. [[line 173](https://github.com/gpambrozio/ClaudeDocs/blob/387ac4913cbc790d05bce4604e1ebf04f7b85603/docs-md/claude-code/terminal-config.md?plain=1#L173)] [[Source](https://code.claude.com/docs/en/terminal-config#text-and-accent-colors)]
* Added new fullscreen-mode background tokens: `userMessageBackgroundHover`, `messageActionsBackground`, `bashMessageBackgroundColor`, and `memoryBackgroundColor`. [[lines 221-224](https://github.com/gpambrozio/ClaudeDocs/blob/387ac4913cbc790d05bce4604e1ebf04f7b85603/docs-md/claude-code/terminal-config.md?plain=1#L221-L224)] [[Source](https://code.claude.com/docs/en/terminal-config#fullscreen-mode)]
* Added new usage meter and speaker label tokens: `rate_limit_fill`, `rate_limit_empty`, `briefLabelYou`, and `briefLabelClaude`. [[lines 233-238](https://github.com/gpambrozio/ClaudeDocs/blob/387ac4913cbc790d05bce4604e1ebf04f7b85603/docs-md/claude-code/terminal-config.md?plain=1#L233-L238)] [[Source](https://code.claude.com/docs/en/terminal-config#usage-meter-and-speaker-labels)]
* Expanded the shimmer variants section with the full list of paired shimmer tokens (`claude`/`claudeShimmer`, `warning`/`warningShimmer`, `permission`/`permissionShimmer`, `promptBorder`/`promptBorderShimmer`, `inactive`/`inactiveShimmer`, `fastMode`/`fastModeShimmer`).
* Added documentation for `ultrathink`/`ultraplan` rainbow gradient tokens (`rainbow_<color>` and `rainbow_<color>_shimmer` for 7 colors). [[line 249](https://github.com/gpambrozio/ClaudeDocs/blob/387ac4913cbc790d05bce4604e1ebf04f7b85603/docs-md/claude-code/terminal-config.md?plain=1#L249)] [[Source](https://code.claude.com/docs/en/terminal-config#shimmer-variants-and-subagent-colors)]

#### [troubleshoot-install](https://github.com/gpambrozio/ClaudeDocs/blob/387ac4913cbc790d05bce4604e1ebf04f7b85603/docs-md/claude-code/troubleshoot-install.md) [[Source](https://code.claude.com/docs/en/troubleshoot-install)]

* Expanded the "Illegal instruction" section to explicitly cover VMs and VPS where the hypervisor does not pass AVX through to the guest, with a diagnostic command (`grep -m1 -ow avx /proc/cpuinfo`) to confirm AVX availability inside the VM. [[lines 547-549](https://github.com/gpambrozio/ClaudeDocs/blob/387ac4913cbc790d05bce4604e1ebf04f7b85603/docs-md/claude-code/troubleshoot-install.md?plain=1#L547-L549)] [[Source](https://code.claude.com/docs/en/troubleshoot-install#illegal-instruction)]

#### [voice-dictation](https://github.com/gpambrozio/ClaudeDocs/blob/387ac4913cbc790d05bce4604e1ebf04f7b85603/docs-md/claude-code/voice-dictation.md) [[Source](https://code.claude.com/docs/en/voice-dictation)]

* Added a note that some keys (such as `Caps Lock`) cannot be delivered to terminal applications and will show an error if bound, with a pointer to the keybindings reference for the full list of reserved shortcuts. [[line 135](https://github.com/gpambrozio/ClaudeDocs/blob/387ac4913cbc790d05bce4604e1ebf04f7b85603/docs-md/claude-code/voice-dictation.md?plain=1#L135)] [[Source](https://code.claude.com/docs/en/voice-dictation#rebind-the-dictation-key)]

#### [vs-code](https://github.com/gpambrozio/ClaudeDocs/blob/387ac4913cbc790d05bce4604e1ebf04f7b85603/docs-md/claude-code/vs-code.md) [[Source](https://code.claude.com/docs/en/vs-code)]

* Added a troubleshooting section for `Cmd+Esc` doing nothing on macOS Tahoe and later, where the system Game Overlay shortcut intercepts the keypress. Includes steps to disable Game Overlay in System Settings or rebind the extension to a different key. [[lines 432-442](https://github.com/gpambrozio/ClaudeDocs/blob/387ac4913cbc790d05bce4604e1ebf04f7b85603/docs-md/claude-code/vs-code.md?plain=1#L432-L442)] [[Source](https://code.claude.com/docs/en/vs-code#cmd+esc-does-nothing-on-macos)]

-----

## API changes

### New Documents

#### [api/authentication/overview](https://github.com/gpambrozio/ClaudeDocs/blob/387ac4913cbc790d05bce4604e1ebf04f7b85603/docs-md/api/api/authentication/overview.md) [[Source](https://platform.claude.com/docs/en/api/authentication/overview)]

New authentication overview covering the two supported methods: API keys (static `sk-ant-api...` secrets in the `x-api-key` header) and Workload Identity Federation (short-lived bearer tokens exchanged from an OIDC identity provider). Describes when to use each method and links to the full WIF setup walkthrough and provider guides.

#### [api/authentication/wif-reference](https://github.com/gpambrozio/ClaudeDocs/blob/387ac4913cbc790d05bce4604e1ebf04f7b85603/docs-md/api/api/authentication/wif-reference.md) [[Source](https://platform.claude.com/docs/en/api/authentication/wif-reference)]

WIF reference documentation covering environment variables (`ANTHROPIC_FEDERATION_RULE_ID`, `ANTHROPIC_ORGANIZATION_ID`, `ANTHROPIC_SERVICE_ACCOUNT_ID`, `ANTHROPIC_IDENTITY_TOKEN_FILE`), credential precedence table across all five tiers, profile file schema, OAuth scopes, token exchange request/response field reference, validation rules, and error codes.

#### [build-with-claude/wif-providers/aws](https://github.com/gpambrozio/ClaudeDocs/blob/387ac4913cbc790d05bce4604e1ebf04f7b85603/docs-md/api/build-with-claude/wif-providers/aws.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/wif-providers/aws)]

Step-by-step guide for authenticating AWS workloads (Lambda, EC2, ECS, EKS) to the Claude API without static API keys. Covers both the STS `GetWebIdentityToken` path (works anywhere the workload has AWS credentials) and the EKS projected service-account token path. Includes AWS IAM configuration, Anthropic Console setup, and SDK client construction examples.

#### [build-with-claude/wif-providers/azure](https://github.com/gpambrozio/ClaudeDocs/blob/387ac4913cbc790d05bce4604e1ebf04f7b85603/docs-md/api/build-with-claude/wif-providers/azure.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/wif-providers/azure)]

Guide for authenticating Azure workloads using Managed Identity (IMDS) or Entra Workload ID on AKS, with Azure-specific issuer configuration and SDK examples.

#### [build-with-claude/wif-providers/gcp](https://github.com/gpambrozio/ClaudeDocs/blob/387ac4913cbc790d05bce4604e1ebf04f7b85603/docs-md/api/build-with-claude/wif-providers/gcp.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/wif-providers/gcp)]

Guide for authenticating Google Cloud workloads using Google-signed identity tokens from the metadata server, with GCP-specific issuer URL patterns and SDK examples.

#### [build-with-claude/wif-providers/github-actions](https://github.com/gpambrozio/ClaudeDocs/blob/387ac4913cbc790d05bce4604e1ebf04f7b85603/docs-md/api/build-with-claude/wif-providers/github-actions.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/wif-providers/github-actions)]

Guide for keyless CI authentication in GitHub Actions using the Actions OIDC token, enabling workflows to call the Claude API without storing an API key as a secret.

#### [build-with-claude/wif-providers/kubernetes](https://github.com/gpambrozio/ClaudeDocs/blob/387ac4913cbc790d05bce4604e1ebf04f7b85603/docs-md/api/build-with-claude/wif-providers/kubernetes.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/wif-providers/kubernetes)]

Guide for self-managed and on-premises Kubernetes clusters using projected service-account tokens, including JWKS endpoint configuration for clusters not reachable from the public internet.

#### [build-with-claude/wif-providers/okta](https://github.com/gpambrozio/ClaudeDocs/blob/387ac4913cbc790d05bce4604e1ebf04f7b85603/docs-md/api/build-with-claude/wif-providers/okta.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/wif-providers/okta)]

Guide for Okta service applications using the client-credentials flow to obtain OIDC tokens for authenticating to the Claude API.

#### [build-with-claude/workload-identity-federation](https://github.com/gpambrozio/ClaudeDocs/blob/387ac4913cbc790d05bce4604e1ebf04f7b85603/docs-md/api/build-with-claude/workload-identity-federation.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/workload-identity-federation)]

Full setup guide for Workload Identity Federation. Explains the three-resource model (service accounts, federation issuers, and federation rules), how the JWT-to-Anthropic-token exchange works, SDK client construction, credential precedence across all five tiers, migration from static API keys, and token lifetime/refresh behavior. Supports AWS, Google Cloud, Azure, GitHub Actions, Kubernetes, and Okta identity providers.
