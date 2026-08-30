# [Claude docs changes for August 30th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/055e5fae764af32ba2413510c48eae7e3f8763fb) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/055e5fae764af32ba2413510c48eae7e3f8763fb)]

## Executive Summary
- New `PreModelSwitch` and `PostModelSwitch` hooks let you block or confirm model switches before they happen, see their cache/cost impact, and inject model-specific guidance after a switch — documented across the hooks reference, hooks guide, and Agent SDK types.
- Cloud environments now support **API credentials**: keys or tokens an org admin stores on an environment that Anthropic's agent proxy attaches to matching requests without ever exposing them to Claude or the session's environment variables.
- A new `desktopSessionCleanupPeriodDays` setting lets you cap how long Claude Desktop and Cowork session transcripts are kept; previously they were retained indefinitely.
- Managed settings gained a documented recipe for turning off Anthropic telemetry org-wide via `DISABLE_TELEMETRY`, including why it's needed even under customer-managed encryption keys.
- Auto mode now turns off immediately in a running session when an admin-deployed policy disables it, instead of waiting until the session ends.

-----

## Claude Code changes

### Changed documents

#### [admin-setup](https://github.com/gpambrozio/ClaudeDocs/blob/055e5fae764af32ba2413510c48eae7e3f8763fb/docs-md/claude-code/admin-setup.md) [[Source](https://code.claude.com/docs/en/admin-setup)]

* Server-managed settings are now fetched at session **startup**, not just at authentication time, in addition to the hourly refresh. [[line 43](https://github.com/gpambrozio/ClaudeDocs/blob/055e5fae764af32ba2413510c48eae7e3f8763fb/docs-md/claude-code/admin-setup.md?plain=1#L43)] [[Source](https://code.claude.com/docs/en/admin-setup#decide-how-settings-reach-devices)]
* Clarified what the WSL `/status` "Setting sources" line actually tells you: it always shows "Enterprise managed settings (remote)" once any server-managed keys arrive, so it doesn't confirm a Windows registry/file deployment in that case — only in sessions that aren't fetching server-managed settings. [[lines 62-65](https://github.com/gpambrozio/ClaudeDocs/blob/055e5fae764af32ba2413510c48eae7e3f8763fb/docs-md/claude-code/admin-setup.md?plain=1#L62-L65)] [[Source](https://code.claude.com/docs/en/admin-setup#wsl-sessions-in-claude-code-desktop)]

#### [agent-sdk/hooks](https://github.com/gpambrozio/ClaudeDocs/blob/055e5fae764af32ba2413510c48eae7e3f8763fb/docs-md/claude-code/agent-sdk/hooks.md) [[Source](https://code.claude.com/docs/en/agent-sdk/hooks)]

* Added `PreModelSwitch` and `PostModelSwitch` to the SDK hooks table, along with their timeout defaults (30 seconds) and blocking behavior. [[line 163](https://github.com/gpambrozio/ClaudeDocs/blob/055e5fae764af32ba2413510c48eae7e3f8763fb/docs-md/claude-code/agent-sdk/hooks.md?plain=1#L163)] [[Source](https://code.claude.com/docs/en/agent-sdk/hooks#available-hooks)]

#### [agent-sdk/modifying-system-prompts](https://github.com/gpambrozio/ClaudeDocs/blob/055e5fae764af32ba2413510c48eae7e3f8763fb/docs-md/claude-code/agent-sdk/modifying-system-prompts.md) [[Source](https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts)]

* Clarified that `keep-coding-instructions` in an output style's frontmatter only has an effect on Claude Code's full system prompt — it does nothing when a session uses the shorter system prompt via `CLAUDE_CODE_SIMPLE_SYSTEM_PROMPT`. [[line 106](https://github.com/gpambrozio/ClaudeDocs/blob/055e5fae764af32ba2413510c48eae7e3f8763fb/docs-md/claude-code/agent-sdk/modifying-system-prompts.md?plain=1#L106)] [[Source](https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts#create-an-output-style)]

#### [agent-sdk/typescript](https://github.com/gpambrozio/ClaudeDocs/blob/055e5fae764af32ba2413510c48eae7e3f8763fb/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* Added `PreModelSwitchHookInput` and `PostModelSwitchHookInput` types, plus the new `"PreModelSwitch"`/`"PostModelSwitch"` hook event names and their `SyncHookJSONOutput` variants (`permissionDecision` for pre-switch, `additionalContext` for post-switch). [[lines 1645-1966](https://github.com/gpambrozio/ClaudeDocs/blob/055e5fae764af32ba2413510c48eae7e3f8763fb/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L1645-L1966)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#hookevent)]

#### [claude-code-on-the-web](https://github.com/gpambrozio/ClaudeDocs/blob/055e5fae764af32ba2413510c48eae7e3f8763fb/docs-md/claude-code/claude-code-on-the-web.md) [[Source](https://code.claude.com/docs/en/claude-code-on-the-web)]

* Split the "Credential protection" bullet into two: one for git/signing credentials, and a new one describing the cloud environment **API credentials** feature, which keeps API keys outside the sandbox and attaches them to matching requests via a proxy. [[lines 265-266](https://github.com/gpambrozio/ClaudeDocs/blob/055e5fae764af32ba2413510c48eae7e3f8763fb/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L265-L266)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#security-and-isolation)]

#### [claude-directory](https://github.com/gpambrozio/ClaudeDocs/blob/055e5fae764af32ba2413510c48eae7e3f8763fb/docs-md/claude-code/claude-directory.md) [[Source](https://code.claude.com/docs/en/claude-directory)]

* Documented that Claude Desktop and Cowork session transcripts are kept indefinitely by default, with a new `desktopSessionCleanupPeriodDays` setting to give them an age limit (requires v2.1.248+). Previously these transcripts had no special-cased retention rule described here. [[lines 205-209](https://github.com/gpambrozio/ClaudeDocs/blob/055e5fae764af32ba2413510c48eae7e3f8763fb/docs-md/claude-code/claude-directory.md?plain=1#L205-L209)] [[Source](https://code.claude.com/docs/en/claude-directory#cleaned-up-automatically)]
* The retention-sweep pause condition now also triggers when `desktopSessionCleanupPeriodDays` is explicitly set and settings have validation errors. [[line 234](https://github.com/gpambrozio/ClaudeDocs/blob/055e5fae764af32ba2413510c48eae7e3f8763fb/docs-md/claude-code/claude-directory.md?plain=1#L234)] [[Source](https://code.claude.com/docs/en/claude-directory#plaintext-storage)]
* Added `desktopSessionCleanupPeriodDays` to the list of ways to reduce credential-exposure risk from unencrypted transcripts. [[line 235](https://github.com/gpambrozio/ClaudeDocs/blob/055e5fae764af32ba2413510c48eae7e3f8763fb/docs-md/claude-code/claude-directory.md?plain=1#L235)] [[Source](https://code.claude.com/docs/en/claude-directory#plaintext-storage)]

#### [cloud-environments](https://github.com/gpambrozio/ClaudeDocs/blob/055e5fae764af32ba2413510c48eae7e3f8763fb/docs-md/claude-code/cloud-environments.md) [[Source](https://code.claude.com/docs/en/cloud-environments)]

* New **Add API credentials** section: org admins can store an API key/token (Bearer or other auth type) on a cloud environment, scoped to specific hosts; Anthropic's agent proxy attaches it to matching requests after they leave the session's VM, so Claude and its commands never see the value. Covers requirements (admin role, Anthropic-hosted environment, no customer-managed encryption keys), how to add one, and the requests that never get a credential (GitHub, the Anthropic API, and public package registries). [[lines 36-91](https://github.com/gpambrozio/ClaudeDocs/blob/055e5fae764af32ba2413510c48eae7e3f8763fb/docs-md/claude-code/cloud-environments.md?plain=1#L36-L91)] [[Source](https://code.claude.com/docs/en/cloud-environments#configure-your-environment)]
* API-credential hosts are now reachable regardless of the environment's network access level, alongside GitHub and MCP connector traffic. [[lines 169-174](https://github.com/gpambrozio/ClaudeDocs/blob/055e5fae764af32ba2413510c48eae7e3f8763fb/docs-md/claude-code/cloud-environments.md?plain=1#L169-L174)] [[Source](https://code.claude.com/docs/en/cloud-environments#access-levels)]
* The "what carries over" table now says static API keys/tokens *are* supported, via API credentials, reversing the previous "no dedicated secrets store" guidance. [[line 235](https://github.com/gpambrozio/ClaudeDocs/blob/055e5fae764af32ba2413510c48eae7e3f8763fb/docs-md/claude-code/cloud-environments.md?plain=1#L235)] [[Source](https://code.claude.com/docs/en/cloud-environments#what-carries-over-from-your-setup)]
* Shared (org-wide) environments can now also be edited from the environment selector at claude.ai/code by an Admin or Owner, not only from the admin **Cloud environments** page. [[line 108](https://github.com/gpambrozio/ClaudeDocs/blob/055e5fae764af32ba2413510c48eae7e3f8763fb/docs-md/claude-code/cloud-environments.md?plain=1#L108)] [[Source](https://code.claude.com/docs/en/cloud-environments#add-a-credential)]

#### [commands](https://github.com/gpambrozio/ClaudeDocs/blob/055e5fae764af32ba2413510c48eae7e3f8763fb/docs-md/claude-code/commands.md) [[Source](https://code.claude.com/docs/en/commands)]

* Expanded the `/terminal-setup` description: it now also covers enabling Option+Enter and disabling the audible bell in Apple Terminal, and enabling clipboard access for `/copy` in iTerm2. [[line 130](https://github.com/gpambrozio/ClaudeDocs/blob/055e5fae764af32ba2413510c48eae7e3f8763fb/docs-md/claude-code/commands.md?plain=1#L130)] [[Source](https://code.claude.com/docs/en/commands#all-commands)]

#### [data-usage](https://github.com/gpambrozio/ClaudeDocs/blob/055e5fae764af32ba2413510c48eae7e3f8763fb/docs-md/claude-code/data-usage.md) [[Source](https://code.claude.com/docs/en/data-usage)]

* Noted that Claude Desktop/Cowork transcripts are exempt from the 30-day local caching limit by default. [[line 44](https://github.com/gpambrozio/ClaudeDocs/blob/055e5fae764af32ba2413510c48eae7e3f8763fb/docs-md/claude-code/data-usage.md?plain=1#L44)] [[Source](https://code.claude.com/docs/en/data-usage#data-retention)]

#### [discover-plugins](https://github.com/gpambrozio/ClaudeDocs/blob/055e5fae764af32ba2413510c48eae7e3f8763fb/docs-md/claude-code/discover-plugins.md) [[Source](https://code.claude.com/docs/en/discover-plugins)]

* Clarified that in cloud sessions, Claude Code doesn't start plugin language servers, so the LSP tool isn't available there even with a code-intelligence plugin installed. [[line 44](https://github.com/gpambrozio/ClaudeDocs/blob/055e5fae764af32ba2413510c48eae7e3f8763fb/docs-md/claude-code/discover-plugins.md?plain=1#L44)] [[Source](https://code.claude.com/docs/en/discover-plugins#code-intelligence)]

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/055e5fae764af32ba2413510c48eae7e3f8763fb/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* `DISABLE_TELEMETRY` entry now links to the new "Turn telemetry off for your organization" section in managed settings. [[line 397](https://github.com/gpambrozio/ClaudeDocs/blob/055e5fae764af32ba2413510c48eae7e3f8763fb/docs-md/claude-code/env-vars.md?plain=1#L397)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]

#### [glossary](https://github.com/gpambrozio/ClaudeDocs/blob/055e5fae764af32ba2413510c48eae7e3f8763fb/docs-md/claude-code/glossary.md) [[Source](https://code.claude.com/docs/en/glossary)]

* Trimmed the "Output style" entry to drop the detail about which built-in styles keep coding instructions by default, now covered on the dedicated output-styles/system-prompts pages. [[line 163](https://github.com/gpambrozio/ClaudeDocs/blob/055e5fae764af32ba2413510c48eae7e3f8763fb/docs-md/claude-code/glossary.md?plain=1#L163)] [[Source](https://code.claude.com/docs/en/glossary#output-style)]

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/055e5fae764af32ba2413510c48eae7e3f8763fb/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* Full reference sections added for the new **`PreModelSwitch`** and **`PostModelSwitch`** hook events (requires v2.1.251+): what triggers each, matcher rules against the target model's canonical name, input schema (`from_model`, `to_model`, `requested_model`, `source`, `context_tokens`, `prompt_cache_warm`, `cache_ttl`, `estimated_cache_write_usd`, `pricing`), and decision control — `PreModelSwitch` can `allow`/`deny`/`ask` (with `ask` only honored by an interactive `/model`), and a timed-out `PreModelSwitch` hook blocks the switch by default (unlike most other events). `PostModelSwitch` can only add `additionalContext` for Claude's next request. [[lines 173-363](https://github.com/gpambrozio/ClaudeDocs/blob/055e5fae764af32ba2413510c48eae7e3f8763fb/docs-md/claude-code/hooks.md?plain=1#L173-L363)] [[Source](https://code.claude.com/docs/en/hooks#how-a-hook-resolves)]
* Added `PreModelSwitch`/`PostModelSwitch` to the lifecycle diagram, event summary table, matcher-value table, timeout-default text, exit-code-0 exceptions, exit-code-2 table, and the command/http/mcp_tool-only hook-type list. [[lines 15-134](https://github.com/gpambrozio/ClaudeDocs/blob/055e5fae764af32ba2413510c48eae7e3f8763fb/docs-md/claude-code/hooks.md?plain=1#L15-L134)] [[Source](https://code.claude.com/docs/en/hooks#hook-lifecycle)]
* `SessionStart` hooks resuming or forking a transcript with at least one prior response now also receive `seconds_since_last_response`, `context_tokens`, `prompt_cache_likely_expired`, and `estimated_cache_write_usd`, letting a hook report the cost of resuming a stale conversation (requires v2.1.251+). [[lines 141-166](https://github.com/gpambrozio/ClaudeDocs/blob/055e5fae764af32ba2413510c48eae7e3f8763fb/docs-md/claude-code/hooks.md?plain=1#L141-L166)] [[Source](https://code.claude.com/docs/en/hooks#how-a-hook-resolves)]

#### [hooks-guide](https://github.com/gpambrozio/ClaudeDocs/blob/055e5fae764af32ba2413510c48eae7e3f8763fb/docs-md/claude-code/hooks-guide.md) [[Source](https://code.claude.com/docs/en/hooks-guide)]

* Added `PreModelSwitch`/`PostModelSwitch` to the event list, the exit-code-0 context-injection list, the matcher-field table, and the timeout-defaults text; also summarized `PreModelSwitch`'s `permissionDecision` semantics. [[lines 479-889](https://github.com/gpambrozio/ClaudeDocs/blob/055e5fae764af32ba2413510c48eae7e3f8763fb/docs-md/claude-code/hooks-guide.md?plain=1#L479-L889)] [[Source](https://code.claude.com/docs/en/hooks-guide#how-hooks-work)]

#### [managed-settings](https://github.com/gpambrozio/ClaudeDocs/blob/055e5fae764af32ba2413510c48eae7e3f8763fb/docs-md/claude-code/managed-settings.md) [[Source](https://code.claude.com/docs/en/managed-settings)]

* New "Turn telemetry off for your organization" section: deliver `DISABLE_TELEMETRY: "1"` through the managed `env` block to disable telemetry org-wide without relying on each developer's shell; explains it's applied without the approval dialog and also disables feature-flag fetching (Remote Control, default auto mode, etc.). [[lines 298-311](https://github.com/gpambrozio/ClaudeDocs/blob/055e5fae764af32ba2413510c48eae7e3f8763fb/docs-md/claude-code/managed-settings.md?plain=1#L298-L311)] [[Source](https://code.claude.com/docs/en/managed-settings#turn-telemetry-off-for-your-organization)]

#### [monitoring-usage](https://github.com/gpambrozio/ClaudeDocs/blob/055e5fae764af32ba2413510c48eae7e3f8763fb/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* Added `transcripts_exempted_desktop` to the `retention_sweep` event fields, counting transcripts kept under the new Claude Desktop/Cowork retention rule (requires v2.1.248+). [[line 1051](https://github.com/gpambrozio/ClaudeDocs/blob/055e5fae764af32ba2413510c48eae7e3f8763fb/docs-md/claude-code/monitoring-usage.md?plain=1#L1051)] [[Source](https://code.claude.com/docs/en/monitoring-usage#retention-sweep-event)]

#### [permission-modes](https://github.com/gpambrozio/ClaudeDocs/blob/055e5fae764af32ba2413510c48eae7e3f8763fb/docs-md/claude-code/permission-modes.md) [[Source](https://code.claude.com/docs/en/permission-modes)]

* A running session now exits auto mode immediately once an admin-deployed `disableAutoMode` policy reaches it, showing "auto mode disabled by settings"; before v2.1.251, a running session kept auto mode until it ended. [[line 233](https://github.com/gpambrozio/ClaudeDocs/blob/055e5fae764af32ba2413510c48eae7e3f8763fb/docs-md/claude-code/permission-modes.md?plain=1#L233)] [[Source](https://code.claude.com/docs/en/permission-modes#enable-auto-mode-on-bedrock-agent-platform-or-foundry)]

#### [plugins-reference](https://github.com/gpambrozio/ClaudeDocs/blob/055e5fae764af32ba2413510c48eae7e3f8763fb/docs-md/claude-code/plugins-reference.md) [[Source](https://code.claude.com/docs/en/plugins-reference)]

* Added `PreModelSwitch`/`PostModelSwitch` to the plugin hooks lifecycle-event table. [[line 123](https://github.com/gpambrozio/ClaudeDocs/blob/055e5fae764af32ba2413510c48eae7e3f8763fb/docs-md/claude-code/plugins-reference.md?plain=1#L123)] [[Source](https://code.claude.com/docs/en/plugins-reference#hooks)]

#### [prompt-caching](https://github.com/gpambrozio/ClaudeDocs/blob/055e5fae764af32ba2413510c48eae7e3f8763fb/docs-md/claude-code/prompt-caching.md) [[Source](https://code.claude.com/docs/en/prompt-caching)]

* Noted that a `PreModelSwitch` hook can require or skip the `/model` cache-warm confirmation prompt. [[line 66](https://github.com/gpambrozio/ClaudeDocs/blob/055e5fae764af32ba2413510c48eae7e3f8763fb/docs-md/claude-code/prompt-caching.md?plain=1#L66)] [[Source](https://code.claude.com/docs/en/prompt-caching#switching-models)]
* Removed the description of the LSP tool being "sticky" for the rest of a session once a language server becomes available (the tools-reference page now describes simpler behavior). [[lines 103-107](https://github.com/gpambrozio/ClaudeDocs/blob/055e5fae764af32ba2413510c48eae7e3f8763fb/docs-md/claude-code/prompt-caching.md?plain=1#L103-L107)] [[Source](https://code.claude.com/docs/en/prompt-caching#plugins-that-provide-mcp-servers)]

#### [routines](https://github.com/gpambrozio/ClaudeDocs/blob/055e5fae764af32ba2413510c48eae7e3f8763fb/docs-md/claude-code/routines.md) [[Source](https://code.claude.com/docs/en/routines)]

* Routines no longer require "Claude Code on the web" to be separately enabled — available to all Pro/Max/Team/Enterprise users. [[line 13](https://github.com/gpambrozio/ClaudeDocs/blob/055e5fae764af32ba2413510c48eae7e3f8763fb/docs-md/claude-code/routines.md?plain=1#L13)] [[Source](https://code.claude.com/docs/en/routines)]
* Routine environment variables guidance now points to the new API credentials feature instead of just warning not to add secrets. [[line 61](https://github.com/gpambrozio/ClaudeDocs/blob/055e5fae764af32ba2413510c48eae7e3f8763fb/docs-md/claude-code/routines.md?plain=1#L61)] [[Source](https://code.claude.com/docs/en/routines#create-from-the-web)]

#### [server-managed-settings](https://github.com/gpambrozio/ClaudeDocs/blob/055e5fae764af32ba2413510c48eae7e3f8763fb/docs-md/claude-code/server-managed-settings.md) [[Source](https://code.claude.com/docs/en/server-managed-settings)]

* Invalid `cleanupPeriodDays` and `desktopSessionCleanupPeriodDays` values are now kept in the cached remote-settings copy (but never applied) rather than stripped, and a payload consisting only of those invalid retention keys no longer causes a full payload rejection. [[line 168](https://github.com/gpambrozio/ClaudeDocs/blob/055e5fae764af32ba2413510c48eae7e3f8763fb/docs-md/claude-code/server-managed-settings.md?plain=1#L168)] [[Source](https://code.claude.com/docs/en/server-managed-settings#invalid-entries-in-delivered-settings)]

#### [sessions](https://github.com/gpambrozio/ClaudeDocs/blob/055e5fae764af32ba2413510c48eae7e3f8763fb/docs-md/claude-code/sessions.md) [[Source](https://code.claude.com/docs/en/sessions)]

* `/clear` can now take a name argument (e.g. `/clear release-prep`) to name the conversation you're leaving instead of carrying its name to the new one. [[line 171](https://github.com/gpambrozio/ClaudeDocs/blob/055e5fae764af32ba2413510c48eae7e3f8763fb/docs-md/claude-code/sessions.md?plain=1#L171)] [[Source](https://code.claude.com/docs/en/sessions#manage-context-within-a-session)]
* Added `desktopSessionCleanupPeriodDays` to the storage-configuration table. [[line 207](https://github.com/gpambrozio/ClaudeDocs/blob/055e5fae764af32ba2413510c48eae7e3f8763fb/docs-md/claude-code/sessions.md?plain=1#L207)] [[Source](https://code.claude.com/docs/en/sessions#where-transcripts-are-stored)]

#### [settings-reference](https://github.com/gpambrozio/ClaudeDocs/blob/055e5fae764af32ba2413510c48eae7e3f8763fb/docs-md/claude-code/settings-reference.md) [[Source](https://code.claude.com/docs/en/settings-reference)]

* Documented the new `desktopSessionCleanupPeriodDays` setting (user or managed scope, default `0` = no age limit; ignored when managed `cleanupPeriodDays` is set; requires v2.1.248+). [[lines 5021-5036](https://github.com/gpambrozio/ClaudeDocs/blob/055e5fae764af32ba2413510c48eae7e3f8763fb/docs-md/claude-code/settings-reference.md?plain=1#L5021-L5036)] [[Source](https://code.claude.com/docs/en/settings-reference#desktopsessioncleanupperioddays)]
* Page now describes an interactive filter/sort UI (topic and scope dropdowns, sort-by control, settings count) above the settings table. [[lines 3-11](https://github.com/gpambrozio/ClaudeDocs/blob/055e5fae764af32ba2413510c48eae7e3f8763fb/docs-md/claude-code/settings-reference.md?plain=1#L3-L11)] [[Source](https://code.claude.com/docs/en/settings-reference)]

#### [skills](https://github.com/gpambrozio/ClaudeDocs/blob/055e5fae764af32ba2413510c48eae7e3f8763fb/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)]

* The `/skills` menu now saves a skill-visibility override with `Esc`, not `Enter`. [[line 685](https://github.com/gpambrozio/ClaudeDocs/blob/055e5fae764af32ba2413510c48eae7e3f8763fb/docs-md/claude-code/skills.md?plain=1#L685)] [[Source](https://code.claude.com/docs/en/skills#override-skill-visibility-from-settings)]

#### [third-party-integrations](https://github.com/gpambrozio/ClaudeDocs/blob/055e5fae764af32ba2413510c48eae7e3f8763fb/docs-md/claude-code/third-party-integrations.md) [[Source](https://code.claude.com/docs/en/third-party-integrations)]

* New note: customer-managed encryption keys (CMEK) don't cover Claude Code's operational telemetry when routing through an LLM gateway or custom `ANTHROPIC_BASE_URL`, so those orgs should use `DISABLE_TELEMETRY` via managed settings if they want it off. [[line 50](https://github.com/gpambrozio/ClaudeDocs/blob/055e5fae764af32ba2413510c48eae7e3f8763fb/docs-md/claude-code/third-party-integrations.md?plain=1#L50)] [[Source](https://code.claude.com/docs/en/third-party-integrations#configure-proxies-and-gateways)]

#### [tools-reference](https://github.com/gpambrozio/ClaudeDocs/blob/055e5fae764af32ba2413510c48eae7e3f8763fb/docs-md/claude-code/tools-reference.md) [[Source](https://code.claude.com/docs/en/tools-reference)]

* Simplified the LSP tool's activation behavior description and added that it stays inactive in cloud sessions, since plugin language servers don't start there. [[lines 268-269](https://github.com/gpambrozio/ClaudeDocs/blob/055e5fae764af32ba2413510c48eae7e3f8763fb/docs-md/claude-code/tools-reference.md?plain=1#L268-L269)] [[Source](https://code.claude.com/docs/en/tools-reference#lsp-tool-behavior)]

#### [web-quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/055e5fae764af32ba2413510c48eae7e3f8763fb/docs-md/claude-code/web-quickstart.md) [[Source](https://code.claude.com/docs/en/web-quickstart)]

* New troubleshooting entry: if `/web-setup` warns your GitHub CLI token lacks the `workflow` scope, some pushes (e.g. to GitHub Actions workflow files) may be rejected; fix with `gh auth refresh -s workflow`. [[lines 203-205](https://github.com/gpambrozio/ClaudeDocs/blob/055e5fae764af32ba2413510c48eae7e3f8763fb/docs-md/claude-code/web-quickstart.md?plain=1#L203-L205)] [[Source](https://code.claude.com/docs/en/web-quickstart#/web-setup-warns-that-your-token-doesn’t-have-the-workflow-scope)]

-----

## API changes

No changes to the Claude API documentation today.
