# [Claude docs changes for September 22nd, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/c6428bfb1a061b27bd6045cd7cafa761c83cb718) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/c6428bfb1a061b27bd6045cd7cafa761c83cb718)]

## Executive Summary
- Pasted prompt text is now marked to Claude as untrusted content, and invisible/steganographic Unicode characters are stripped from prompts before sending — two new prompt-injection defenses in Claude Code.
- Plugins declared in a repository's `.claude/settings.json` no longer install automatically in cloud sessions (Projects threads, `claude-code-on-the-web`, routines) — only plugins synced from your claude.ai account load there now.
- `sandbox.excludedCommands` got much stricter: an entry only takes a Bash call out of the sandbox when it covers every command in it, and shapes like `sudo`, `eval`, `cd`, subshells, and non-fd redirections always stay sandboxed regardless of the list.
- New Claude API capability: on accounts where the prefix-binding check isn't enforced yet, sending the `thinking-binding-controls-2026-08-01` beta header now surfaces a `thinking_mismatch_allowed` entry in `input_transformations` so you can find history edits in production before opting into enforcement.
- The Claude API's Compaction guide was split into five focused pages (on-demand, threshold, keep-recent-turns, background, and preserved-thinking interactions), and Claude Code's VS Code extension picked up a large batch of editor and accessibility features (per-change diff review, memory/instructions editors, background-task view, copy-response button).

-----

## Claude Code changes

### Changed documents

#### [advisor](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/advisor.md) [[Source](https://code.claude.com/docs/en/advisor)]

* A saved advisor that the API has already refused in the current conversation now stays off until `/clear` or `/compact`, even after you switch main models. [[line 47](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/advisor.md?plain=1#L47)] [[Source](https://code.claude.com/docs/en/advisor#use-the-advisor-command)]
* When the API refuses a mismatched advisor/model pairing, Claude Code now silently resends the request without the advisor instead of failing every request with an error message. [[lines 101-104](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/advisor.md?plain=1#L101-L104)] [[Source](https://code.claude.com/docs/en/advisor#choose-an-advisor-model)]

#### [agent-sdk/configuration](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/agent-sdk/configuration.md) [[Source](https://code.claude.com/docs/en/agent-sdk/configuration)]

* `updateSettings()` gained a `"userSettings"` destination that saves `effortLevel` as the default effort for the session's current model, alongside the existing `"localSettings"` destination. [[lines 163-171](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/agent-sdk/configuration.md?plain=1#L163-L171)] [[Source](https://code.claude.com/docs/en/agent-sdk/configuration#change-configuration-mid-session)]

#### [agent-sdk/cost-tracking](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/agent-sdk/cost-tracking.md) [[Source](https://code.claude.com/docs/en/agent-sdk/cost-tracking)]

* A `query()` call that resumes a session now reports the session's whole spend (earlier calls included), not just that call's own cost; `maxBudgetUsd`/`max_budget_usd` still counts only the call's own spend. Requires Claude Code v2.1.277 or later — earlier versions started resumed totals at zero. [[lines 29-83](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/agent-sdk/cost-tracking.md?plain=1#L29-L83)] [[Source](https://code.claude.com/docs/en/agent-sdk/cost-tracking#understand-token-usage)]

#### [agent-sdk/modifying-system-prompts](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/agent-sdk/modifying-system-prompts.md) [[Source](https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts)]

* CLI-only custom system prompts (`--system-prompt`/`--system-prompt-file`) can now split into a cached static part and a dynamic part with a literal `__SYSTEM_PROMPT_DYNAMIC_BOUNDARY__` line, mirroring the SDK's array marker. Requires Claude Code v2.1.275 or later. [[lines 339-345](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/agent-sdk/modifying-system-prompts.md?plain=1#L339-L345)] [[Source](https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts#cache-the-static-part-of-a-custom-prompt)]

#### [agent-sdk/python](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/agent-sdk/python.md) [[Source](https://code.claude.com/docs/en/agent-sdk/python)]

* The Monitor tool's `persistent` option is gone — every watch now has a deadline, capped at 30 minutes (1,800,000 ms) even if a longer `timeout_ms` is requested. [[lines 2593-2609](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/agent-sdk/python.md?plain=1#L2593-L2609)] [[Source](https://code.claude.com/docs/en/agent-sdk/python#monitor)]
* `TaskOutput` was removed in v2.1.277 (superseded by reading a background task's output file with `Read`); its schema no longer appears in the SDK reference. [[lines 2989-2997](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/agent-sdk/python.md?plain=1#L2989-L2997)] [[Source](https://code.claude.com/docs/en/agent-sdk/python#tasklist)]
* `sandbox.excludedCommands` entries no longer unconditionally take a whole compound command out of the sandbox — see the `settings-reference` entry below for the full new rule. [[lines 3228-3238](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/agent-sdk/python.md?plain=1#L3228-L3238)] [[Source](https://code.claude.com/docs/en/agent-sdk/python#sandboxsettings)]

#### [artifacts](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/artifacts.md) [[Source](https://code.claude.com/docs/en/artifacts)]

* Artifacts can now load JavaScript libraries from `unpkg.com`, a fifth allowlisted CDN alongside cdnjs, jsDelivr, the Tailwind CDN, and the jQuery CDN. [[lines 249, 346](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/artifacts.md?plain=1#L346)]

#### [claude-apps-gateway](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/claude-apps-gateway.md) [[Source](https://code.claude.com/docs/en/claude-apps-gateway)]

* A gateway can now return an `email` field in its token response; Claude Code has the developer confirm the account before saving the credential, and `/status` then shows it. Requires Claude Code v2.1.275 or later on the client. [[lines 247-253](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/claude-apps-gateway.md?plain=1#L247-L253)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway#connect-developers)]
* `/logout` now sends a revocation request to the gateway's `revocation_endpoint`, when advertised, so the gateway can end the session server-side too (best effort). Requires v2.1.275 or later. [[lines 458-464](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/claude-apps-gateway.md?plain=1#L458-L464)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway#availability-and-limitations)]

#### [claude-directory](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/claude-directory.md) [[Source](https://code.claude.com/docs/en/claude-directory)]

* Pasted/attached images are no longer stored under `~/.claude/image-cache/`. Since v2.1.275 they save outside `~/.claude`, under the `CLAUDE_CODE_TMPDIR` temp directory, so `claude project purge` no longer removes them (the retention sweep still does). [[lines 1305, 1369](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/claude-directory.md?plain=1#L1369)]
* `~/.claude/plugins/` now also holds an `installed_plugins.json` install record, and plugins synced from your claude.ai account download into `~/.claude/plugins/synced/`. [[line 1228](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/claude-directory.md?plain=1#L1228)] [[Source](https://code.claude.com/docs/en/claude-directory#whats-not-shown)]

#### [claude-md](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/claude-md.md) [[Source](https://code.claude.com/docs/en/claude-md)] / [memory](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/memory.md)

* Corrected: user-level rules loading before project rules doesn't mean they take priority — when a user rule and a project rule conflict, Claude may follow either, so keep the two consistent. [[line 265](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/memory.md?plain=1#L265)] [[Source](https://code.claude.com/docs/en/memory#deploy-organization-wide-claudemd)]

#### [claude-projects](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/claude-projects.md) [[Source](https://code.claude.com/docs/en/claude-projects)]

* Plugins declared in a repository's `.claude/settings.json` no longer load into Projects threads; add the plugin under **Project settings > Plugins** instead. [[lines 178-209](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/claude-projects.md?plain=1#L178-L209)] [[Source](https://code.claude.com/docs/en/claude-projects#see-what-needs-you-in-overview)]

#### [cli-reference](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* `--forward-subagent-text` now also forwards messages from subagents that a forked skill spawns, and from nested forked skills, requiring Claude Code v2.1.275 or later. [[line 88](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/cli-reference.md?plain=1#L88)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-flags)]
* `--max-budget-usd`: totals restored when you `--continue` or `--resume` a conversation no longer count toward the cap. [[line 91](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/cli-reference.md?plain=1#L91)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-flags)]
* New `__SYSTEM_PROMPT_DYNAMIC_BOUNDARY__` marker line for splitting a custom `--system-prompt`/`--system-prompt-file` into a cached static part and a dynamic part. Requires v2.1.275 or later. [[line 150](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/cli-reference.md?plain=1#L150)] [[Source](https://code.claude.com/docs/en/cli-reference#system-prompt-flags)]

#### [cloud-environments](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/cloud-environments.md) [[Source](https://code.claude.com/docs/en/cloud-environments)]

* Plugins and marketplaces declared in a repo's `.claude/settings.json` no longer install in cloud sessions at all; enable the plugin for your claude.ai account instead so it loads as a synced plugin. [[lines 245-267](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/cloud-environments.md?plain=1#L245-L267)] [[Source](https://code.claude.com/docs/en/cloud-environments#what-carries-over-from-your-setup)]

#### [commands](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/commands.md) [[Source](https://code.claude.com/docs/en/commands)]

* New bundled slash command: `/update-config [request]` — describe a settings change and Claude edits the matching `settings.json`. [[line 299](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/commands.md?plain=1#L299)] [[Source](https://code.claude.com/docs/en/commands#see-also)]
* `/code-review`'s cleanup-opportunity coverage is now conditional on the model and effort level rather than always included. [[line 288](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/commands.md?plain=1#L288)] [[Source](https://code.claude.com/docs/en/commands#see-also)]
* `/ultrareview` can now take a commit ID or tag, not just a branch name, as the comparison base. [[line 297](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/commands.md?plain=1#L297)] [[Source](https://code.claude.com/docs/en/commands#see-also)]

#### [context-window](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/context-window.md) [[Source](https://code.claude.com/docs/en/context-window)]

* Added the git status snapshot to the "what survives compaction" table: Claude Code reads a fresh one from your repository after `/compact`. [[line 1155](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/context-window.md?plain=1#L1155)] [[Source](https://code.claude.com/docs/en/context-window#what-survives-compaction)]

#### [costs](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/costs.md) [[Source](https://code.claude.com/docs/en/costs)]

* Clarified that the 1.1× data-residency multiplier on the session cost figure also counts toward `--max-budget-usd`, not just the reported total. [[line 29](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/costs.md?plain=1#L29)] [[Source](https://code.claude.com/docs/en/costs#using-the-usage-command)]

#### [desktop](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)] / [desktop-changelog](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/desktop-changelog.md)

* Plugins declared in a repository's `.claude/settings.json` no longer install in cloud sessions; only claude.ai-synced plugins do. [[lines 20-23](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/desktop.md?plain=1#L20-L23)] [[Source](https://code.claude.com/docs/en/desktop#desktop-application)]
* Same fifth-CDN (`unpkg.com`) addition for artifacts as noted above. [[line 65](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/desktop.md?plain=1#L65)] [[Source](https://code.claude.com/docs/en/desktop#choose-a-permission-mode)]

#### [discover-plugins](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/discover-plugins.md) [[Source](https://code.claude.com/docs/en/discover-plugins)]

* Added the VS Code extension's **Manage plugins** dialog as an install path when `/plugin` isn't available, and cloud sessions now point only at claude.ai-synced plugins. [[lines 75-84](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/discover-plugins.md?plain=1#L75-L84)] [[Source](https://code.claude.com/docs/en/discover-plugins#what-claude-gains-from-code-intelligence-plugins)]
* Adding a plugin by URL now skips the marketplace-source confirmation dialog when the source matches a marketplace you've already added. [[line 102](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/discover-plugins.md?plain=1#L102)] [[Source](https://code.claude.com/docs/en/discover-plugins#development-workflows)]

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* New `CLAUDE_CODE_GATEWAY_HINT_HEADERS` variable to turn the new gateway hint headers on or off per connection (requires v2.1.273+). [[line 141](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/env-vars.md?plain=1#L141)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* New `OTEL_LOG_MANAGED_SETTINGS` variable to add redacted managed settings and a SHA-256 digest to the new `managed_settings_resolved` telemetry event (requires v2.1.274+). [[line 158](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/env-vars.md?plain=1#L158)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* `TASK_MAX_OUTPUT_LENGTH` is now a no-op, removed alongside the `TaskOutput` tool in v2.1.277. [[line 167](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/env-vars.md?plain=1#L167)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* With fetching off, Claude no longer receives pasted text marked as pasted (see terminal-config below) — it arrives unmarked instead. [[line 175](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/env-vars.md?plain=1#L175)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* Documented several new error/message lookups: `Artifacts need a claude.ai login`, `Sign-in timed out while waiting for you to continue`, new 400s for `orphaned tool_result` and `duplicate tool_use ID` in conversation history, `Couldn't open Claude Desktop`, a marketplace-source-conflict error, a "plugin required by your organization" error, worktree-isolation refusal messages, and an `otelHeadersHelper failed` telemetry warning. [[lines 66, 84, 145-146, 198, 218, 232, 240-241]](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/errors.md?plain=1#L145-L146)

#### [fast-mode](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/fast-mode.md) [[Source](https://code.claude.com/docs/en/fast-mode)]

* Two more organization settings can now block turning on fast mode with `/fast`: managed `fastMode: false`, and `fastModePerSessionOptIn: true` outside an interactive terminal session. [[lines 23-29, 177](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/fast-mode.md?plain=1#L23-L29)]

#### [headless](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/headless.md) [[Source](https://code.claude.com/docs/en/headless)]

* `--output-format json`'s `total_cost_usd` now includes earlier runs' spend when you `--continue`/`--resume` a conversation. [[line 62](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/headless.md?plain=1#L62)] [[Source](https://code.claude.com/docs/en/headless#background-tasks-at-exit)]

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* `UserPromptSubmit`'s `prompt` field now delivers expanded pasted content wrapped in `<pasted_content id="…">` tags when Claude Code marks pasted text — hooks that parse the prompt need to account for those lines. [[line 93](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/hooks.md?plain=1#L93)] [[Source](https://code.claude.com/docs/en/hooks#how-a-hook-resolves)]
* `SubagentStop` now also fires for Claude Code's own internal agents (prompt suggestions, `/btw` side questions), with an empty `agent_type` that a named matcher won't match unless the matcher is empty, `"*"`, or a regex matching the empty string. [[lines 2349-2352](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/hooks.md?plain=1#L2349-L2352)] [[Source](https://code.claude.com/docs/en/hooks#subagentstop-input)]

#### [ide-integrations](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/ide-integrations.md) [[Source](https://code.claude.com/docs/en/ide-integrations)] / [vs-code](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/vs-code.md)

* Per-change diff review: **Accept this change** / **Reject this change** buttons under each hunk, plus context-menu and Command Palette actions, for diffs with 100 or fewer changes. Requires v2.1.275+. [[lines 167-169](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/ide-integrations.md?plain=1#L167-L169)] [[Source](https://code.claude.com/docs/en/ide-integrations#resume-past-conversations)]
* Customize menu gained **Memory** (view/edit/delete auto memories, v2.1.274-275) and **Instructions** (edit CLAUDE.md files, v2.1.274) panels, plus a **Sign out** action (v2.1.277). [[lines 193-203](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/ide-integrations.md?plain=1#L193-L203)] [[Source](https://code.claude.com/docs/en/ide-integrations#resume-cloud-sessions-from-claudeai)]
* New **Copy response** button and `/copy [n]` command (v2.1.277); the agent map now also lists background tasks like shell commands and monitors, and `/tasks` opens it even with no subagents running (v2.1.277). [[lines 208-219](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/ide-integrations.md?plain=1#L208-L219)] [[Source](https://code.claude.com/docs/en/ide-integrations#check-account-and-usage)]
* Picking a non-`max` effort level in the model picker now saves it as your default for that model; the effort picker in the model picker previously changed only the current session. [[line 182](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/ide-integrations.md?plain=1#L182)] [[Source](https://code.claude.com/docs/en/ide-integrations#resume-past-conversations)]
* Account & Usage dialog now shows session cost/tokens for third-party-provider and API-key sign-ins that don't have plan usage bars (v2.1.277). [[line 262](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/ide-integrations.md?plain=1#L262)] [[Source](https://code.claude.com/docs/en/ide-integrations#switch-to-terminal-mode)]
* New `lockEditorGroups` (v2.1.274) and `continueAfterReload` (v2.1.274) settings: Claude's editor tab now locks its group by default, and a step interrupted by a window reload resumes automatically.  [[lines 273-284](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/ide-integrations.md?plain=1#L273-L284)] [[Source](https://code.claude.com/docs/en/ide-integrations#install-plugins)]
* Selected text is now withheld from files matched by `files.exclude`/`search.exclude` or gitignored (respecting `respectGitIgnore`) — only the file path reaches Claude for those. [[line 227](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/ide-integrations.md?plain=1#L227)] [[Source](https://code.claude.com/docs/en/ide-integrations#choose-where-claude-lives)]
* Accessibility: new **Focus last message** command (v2.1.268), per-message screen-reader announcements ("You" / "Claude" / tool name / "Claude, thinking"), and arrow-key control over where a permission approval saves. [[lines 321, 363-376](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/ide-integrations.md?plain=1#L363-L376)]
* Restore-all-archived-sessions action added to the sessions list (v2.1.277). [[line 245](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/ide-integrations.md?plain=1#L245)] [[Source](https://code.claude.com/docs/en/ide-integrations#run-multiple-conversations)]

#### [interactive-mode](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* New `Ctrl+Enter` / `Ctrl+X Ctrl+S` shortcut to interrupt the current turn and send queued messages immediately, instead of waiting for the turn to end. Requires v2.1.275+. [[line 32](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/interactive-mode.md?plain=1#L32)] [[Source](https://code.claude.com/docs/en/interactive-mode#general-controls)]
* New security feature: Claude Code now strips invisible Unicode characters (tag characters, bidi controls, zero-width spaces) from a prompt when you press Enter, showing a notice and requiring a second Enter to send the cleaned text. [[lines 518-523](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/interactive-mode.md?plain=1#L518-L523)] [[Source](https://code.claude.com/docs/en/interactive-mode#invisible-characters-in-prompts)]
* Background-task memory-pressure termination now triggers only on *critical* memory pressure and logs why tasks were (or weren't) stopped in the debug log. [[lines 302-304](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/interactive-mode.md?plain=1#L302-L304)] [[Source](https://code.claude.com/docs/en/interactive-mode#how-backgrounding-works)]

#### [keybindings](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/keybindings.md) [[Source](https://code.claude.com/docs/en/keybindings)]

* New `chat:sendNow` action (default `Ctrl+Enter`, `Ctrl+X Ctrl+S`) for the immediate-send behavior above. Requires v2.1.275+. [[line 110](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/keybindings.md?plain=1#L110)] [[Source](https://code.claude.com/docs/en/keybindings#chat-actions)]

#### [llm-gateway-protocol](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/llm-gateway-protocol.md) [[Source](https://code.claude.com/docs/en/llm-gateway-protocol)]

* New feature: gateway hint headers. Claude Code can send `x-claude-code-request-class`, `x-claude-code-agent-type`, `x-claude-code-compaction`, `x-claude-code-context-compacted`, and `x-claude-code-prev-tool-durations` so a gateway can schedule, cache, or attribute requests. On by default on a direct Anthropic API connection; opt-in elsewhere via `CLAUDE_CODE_GATEWAY_HINT_HEADERS=1`. Requires v2.1.273+. [[lines 123-185](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/llm-gateway-protocol.md?plain=1#L123-L185)] [[Source](https://code.claude.com/docs/en/llm-gateway-protocol#gateway-hint-headers)]

#### [managed-settings](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/managed-settings.md) [[Source](https://code.claude.com/docs/en/managed-settings)]

* Documented invalid-value fallback behavior for three new managed keys — `strictKnownMarketplaces`, `disableSideloadFlags`, and `blockedMarketplaces` — and for `syncClaudeAiPlugins`. All four fallbacks require Claude Code v2.1.277 or later. [[lines 216-234](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/managed-settings.md?plain=1#L216-L234)] [[Source](https://code.claude.com/docs/en/managed-settings#let-an-embedding-host-add-policy)]

#### [model-config](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* On the Anthropic API, a Fable model now appears grayed out (with a reason) in the `/model` picker when your organization can't use it, instead of being hidden entirely. [[line 277](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/model-config.md?plain=1#L277)] [[Source](https://code.claude.com/docs/en/model-config#default-model-behavior)]

#### [monitoring-usage](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* New OpenTelemetry event: `managed_settings_resolved`, logged at session start, on managed-settings/policy-helper changes, and on startup refusals, so admins can find machines on unexpected managed sources or with a failing policy helper. Set `OTEL_LOG_MANAGED_SETTINGS=1` to include the redacted settings and a SHA-256 digest. Requires v2.1.274+. [[lines 1226-1281](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/monitoring-usage.md?plain=1#L1226-L1281)] [[Source](https://code.claude.com/docs/en/monitoring-usage#managed-settings-resolved-event)]
* New `effort` span attribute on LLM request spans (v2.1.274+); a new warning notification `otelHeadersHelper failed; telemetry is not being exported` appears once per session when the OTel headers helper first fails. [[lines 21, 28](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/monitoring-usage.md?plain=1#L28)]

#### [plugin-evals](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/plugin-evals.md) [[Source](https://code.claude.com/docs/en/plugin-evals)]

* `TaskOutput` removed from the default read-only tool allowlist for plugin evals, consistent with the tool's removal. [[line 341](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/plugin-evals.md?plain=1#L341)] [[Source](https://code.claude.com/docs/en/plugin-evals#command-options)]

#### [plugins-reference](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/plugins-reference.md) [[Source](https://code.claude.com/docs/en/plugins-reference)]

* New: plugin agent files can now live in subfolders of `agents/`, loading with colon-scoped names like `my-plugin:review:security`. [[lines 66-71](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/plugins-reference.md?plain=1#L66-L71)] [[Source](https://code.claude.com/docs/en/plugins-reference#agents)]

#### [permission-modes](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/permission-modes.md) [[Source](https://code.claude.com/docs/en/permission-modes)]

* New "Approvals you state in conversation" section documents how auto mode's classifier reads a verbal approval: it must name the action and its specifics, covers one action at a time, and can't clear every block. [[lines 257-263](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/permission-modes.md?plain=1#L257-L263)] [[Source](https://code.claude.com/docs/en/permission-modes#review-and-approve-a-plan)]
* A guarded shell-variable expansion, such as `rm -rf "${DIR:?}"/*`, now avoids the critical-path `rm -rf` prompt in `bypassPermissions` mode. [[lines 281-286](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/permission-modes.md?plain=1#L281-L286)] [[Source](https://code.claude.com/docs/en/permission-modes#set-plan-mode-as-the-default)]

#### [sandboxing](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/sandboxing.md) [[Source](https://code.claude.com/docs/en/sandboxing)]

* When your shell leaves `$TMPDIR` unset, an unsandboxed command that references it now gets `CLAUDE_CODE_TMPDIR` (or the OS default) instead of an empty string. [[lines 9-12](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/sandboxing.md?plain=1#L9-L12)] [[Source](https://code.claude.com/docs/en/sandboxing#get-started)]
* Clarified that adding a clipboard tool to `excludedCommands` doesn't take a piped-to call out of the sandbox on its own. [[lines 36-40](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/sandboxing.md?plain=1#L36-L40)] [[Source](https://code.claude.com/docs/en/sandboxing#get-started)]

#### [security-guidance](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/security-guidance.md) [[Source](https://code.claude.com/docs/en/security-guidance)]

* Cloud sessions no longer pick up this plugin via `.claude/settings.json`; the "Enable in cloud sessions and shared repositories" section was replaced with claude.ai-sync guidance, and a VS Code install path was added. [[lines 52-70](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/security-guidance.md?plain=1#L52-L70)] [[Source](https://code.claude.com/docs/en/security-guidance#enable-for-your-team-in-local-sessions)]

#### [self-hosted-environments-deploy](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/self-hosted-environments-deploy.md) [[Source](https://code.claude.com/docs/en/self-hosted-environments-deploy)]

* `--use-anthropic-git-proxy`'s opt-in reporting to Anthropic requires Claude Code v2.1.267 or later; earlier versions accept the flag silently without reporting it. Recommended runner image version bumped to 2.1.267. [[lines 104, 113](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/self-hosted-environments-deploy.md?plain=1#L104)]

#### [server-managed-settings](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/server-managed-settings.md) [[Source](https://code.claude.com/docs/en/server-managed-settings)]

* `gatewayInternalNetworks` was added to the gateway sign-in keys that server-managed settings can never supply or hide. [[line 139](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/server-managed-settings.md?plain=1#L139)] [[Source](https://code.claude.com/docs/en/server-managed-settings#per-key-exceptions-across-managed-sources)]

#### [sessions](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/sessions.md) [[Source](https://code.claude.com/docs/en/sessions)]

* A `claude -p` run started directly from a shell or script no longer gets a generated session title. [[line 152](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/sessions.md?plain=1#L152)] [[Source](https://code.claude.com/docs/en/sessions#use-the-session-picker)]

#### [settings-reference](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/settings-reference.md) [[Source](https://code.claude.com/docs/en/settings-reference)]

* `sandbox.excludedCommands` is now much stricter: an entry only takes a Bash call out of the sandbox when it covers every command in the call, and shapes like `sudo`/`eval`/`xargs`, `cd`/`pushd`/`popd`, command substitution, subshells, control-flow blocks, non-fd redirections, and computed command names always stay sandboxed. [[lines 1697-1719](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/settings-reference.md?plain=1#L1697-L1719)] [[Source](https://code.claude.com/docs/en/settings-reference#sandboxexcludedcommands)]
* `taskOutputMaxChars` was removed in v2.1.277 alongside the `TaskOutput` tool. [[lines 2828-2833](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/settings-reference.md?plain=1#L2828-L2833)] [[Source](https://code.claude.com/docs/en/settings-reference#taskoutputmaxchars)]
* `attribution`: Claude Code now tells Claude that your own CLAUDE.md/memory instructions about attribution take precedence over the commit/PR lines, unless the line is set in managed settings. [[line 3656](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/settings-reference.md?plain=1#L3656)] [[Source](https://code.claude.com/docs/en/settings-reference#attribution)]
* `modelSettings` is now also written when you pick an effort level in the VS Code extension's model picker, not just the CLI's `/effort` or `/model`. [[line 1122](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/settings-reference.md?plain=1#L1122)] [[Source](https://code.claude.com/docs/en/settings-reference#modelsettings)]

#### [skills](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)]

* In a linked git worktree whose checkout has no `.claude/skills` at its root, Claude Code now loads the main checkout's project skills instead. Requires v2.1.277+. [[line 130](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/skills.md?plain=1#L130)] [[Source](https://code.claude.com/docs/en/skills#create-your-first-skill)]
* Clarified that synced skills are download-only: local edits under `~/.claude/skills/synced/` aren't uploaded and can be overwritten by the next sync. [[line 202](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/skills.md?plain=1#L202)] [[Source](https://code.claude.com/docs/en/skills#where-synced-skills-load)]

#### [statusline](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/statusline.md) [[Source](https://code.claude.com/docs/en/statusline)]

* `cost.total_duration_ms` now accumulates across session resumes and excludes time the session wasn't running, instead of measuring elapsed wall-clock time since start. [[line 19](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/statusline.md?plain=1#L19)] [[Source](https://code.claude.com/docs/en/statusline#customize-your-status-line)]

#### [sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* `tools`/`disallowedTools` frontmatter now also accepts a comma-separated string, such as `Read, Grep, Bash`, in addition to a YAML list. [[lines 49-52](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/sub-agents.md?plain=1#L49-L52)] [[Source](https://code.claude.com/docs/en/sub-agents#built-in-subagents)]
* A `opus`/`sonnet` family alias in a subagent's model now resolves to the main conversation's exact model (including its `[1m]` suffix) in two cases: when the main conversation is already in that family, or when Claude Code can't determine the main model's family on a non-Anthropic-API provider. [[lines 60-65](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/sub-agents.md?plain=1#L60-L65)] [[Source](https://code.claude.com/docs/en/sub-agents#built-in-subagents)]
* Security: a subagent's report now arrives under a header marking it as untrusted subagent output with no authority from you, and a background subagent's report arrives inside a notification marked as an automated event. [[lines 914-917](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/sub-agents.md?plain=1#L914-L917)] [[Source](https://code.claude.com/docs/en/sub-agents#subagent-output-scanning)]

#### [terminal-config](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/terminal-config.md) [[Source](https://code.claude.com/docs/en/terminal-config)]

* New security feature: submitted prompts now mark the content behind each `[Pasted text #N]` placeholder to Claude as pasted (untrusted) text, with instructions to only follow embedded instructions where your own message asked it to. [[lines 122-126](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/terminal-config.md?plain=1#L122-L126)] [[Source](https://code.claude.com/docs/en/terminal-config#fix-backspace-deleting-a-whole-word-on-windows)]

#### [third-party-integrations](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/third-party-integrations.md) [[Source](https://code.claude.com/docs/en/third-party-integrations)]

* Claude for Teams now includes SSO and server-managed settings (previously Enterprise-only); Claude for Enterprise's description was trimmed to domain capture, role-based permissions, and the compliance API. [[lines 153-156](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/third-party-integrations.md?plain=1#L153-L156)] [[Source](https://code.claude.com/docs/en/third-party-integrations#compare-deployment-options)]

#### [troubleshooting](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/troubleshooting.md) [[Source](https://code.claude.com/docs/en/troubleshooting)]

* New: a critical memory-usage warning now appears once a session's heap passes 2.5GB, with guidance to restart and `--continue`, or run `/compact`, to clear it. [[lines 36-38](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/troubleshooting.md?plain=1#L36-L38)] [[Source](https://code.claude.com/docs/en/troubleshooting#high-cpu-or-memory-usage)]

#### [ultrareview](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/ultrareview.md) [[Source](https://code.claude.com/docs/en/ultrareview)]

* A commit ID or tag now works as the comparison base, not just a branch name. [[line 43](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/ultrareview.md?plain=1#L43)] [[Source](https://code.claude.com/docs/en/ultrareview#review-against-a-different-base)]
* New: reviewing a repository's first commit (with confirmation), plus more specific refusal messages for "nothing to review" and "no merge base" cases. [[lines 232-241](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/ultrareview.md?plain=1#L232-L241)] [[Source](https://code.claude.com/docs/en/ultrareview#related-resources)]
* Security fix: the whole-repository fallback's consent now requires you to run the subcommand yourself — Claude running `claude ultrareview` for you via the Bash tool no longer counts as consent and is refused. [[line 250](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/ultrareview.md?plain=1#L250)] [[Source](https://code.claude.com/docs/en/ultrareview#related-resources)]

#### [workflows](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/workflows.md) [[Source](https://code.claude.com/docs/en/workflows)]

* In auto mode, a prompt that a workflow script computes and passes to `agent()` is now marked as script-computed text rather than a request from you, when the classifier reviews that subagent's actions. [[line 274](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/workflows.md?plain=1#L274)] [[Source](https://code.claude.com/docs/en/workflows#find-issues-until-the-list-stops-growing)]

#### [worktrees](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/worktrees.md) [[Source](https://code.claude.com/docs/en/worktrees)]

* Worktree cleanup now also checks checked-out submodules for changes before removing a worktree, and prompts instead of auto-removing when it can't verify the worktree's state. [[lines 286-291](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/worktrees.md?plain=1#L286-L291)] [[Source](https://code.claude.com/docs/en/worktrees#non-git-version-control)]
* The command-shape isolation check now also blocks expansions like `${!name}` or `${ command; }` that could run a command the text doesn't spell out. [[line 299](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/worktrees.md?plain=1#L299)] [[Source](https://code.claude.com/docs/en/worktrees#worktree-creation-fails-on-a-symlinked-path)]
* A worktree with no `.claude/skills` (and, on v2.1.277+, no local override) now reads through to the main checkout's skills, agents, and commands. [[lines 321-330](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/claude-code/worktrees.md?plain=1#L321-L330)] [[Source](https://code.claude.com/docs/en/worktrees#claude-code-refuses-to-use-a-worktree)]

-----

## API changes

### New Documents

#### [compaction-on-demand](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/api/build-with-claude/compaction-on-demand.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/compaction-on-demand)]

New guide covering the recommended compaction path: request a summary on demand with the `compact-2026-09-04` beta header and top-level `compaction` parameter, splitting the request that summarizes from your ordinary conversation turns.

#### [compaction-threshold](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/api/build-with-claude/compaction-threshold.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/compaction-threshold)]

New guide holding the original `compact_20260112` token-threshold compaction content that used to live on the main Compaction page: the API compacts automatically inside an ordinary request once input tokens reach your configured trigger.

#### [compaction-keep-recent-turns](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/api/build-with-claude/compaction-keep-recent-turns.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/compaction-keep-recent-turns)]

New guide on keeping the most recent turns word for word behind an on-demand compaction summary.

#### [compaction-background](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/api/build-with-claude/compaction-background.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/compaction-background)]

New guide on running on-demand compaction as a background request while the conversation keeps going, then swapping in the summary block when it arrives.

#### [compaction-thinking-blocks](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/api/build-with-claude/compaction-thinking-blocks.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/compaction-thinking-blocks)]

New guide on the conditions under which thinking blocks in turns kept behind an on-demand compaction summary stay valid, for models with preserved thinking.

### Changed documents

#### [build-with-claude/compaction](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/api/build-with-claude/compaction.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/compaction)]

* Rewritten from a full reference (3,800+ lines) into a short overview and decision page: a comparison table of on-demand vs. threshold vs. client-side compaction, and links out to the five new pages above for the details. [[lines 1-50](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/api/build-with-claude/compaction.md?plain=1#L1-L50)] [[Source](https://platform.claude.com/docs/en/build-with-claude/compaction#compaction)]

#### [build-with-claude/preserved-thinking](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/api/build-with-claude/preserved-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking)]

* New API capability: with the `thinking-binding-controls-2026-08-01` beta header, `input_transformations` now gains a `thinking_mismatch_allowed` entry type. It flags a thinking block that fails the prefix-binding check on a request where the API doesn't enforce that check by default (for example, an older account on Claude Fable 5.1 that leaves `prefix_mismatch_behavior` unset), without changing what the model receives — so you can find history edits in production traffic before opting into enforcement. [[lines 31, 368-380, 787-874](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/api/build-with-claude/preserved-thinking.md?plain=1#L368-L380)]

#### [release-notes/overview](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/api/release-notes/overview.md) [[Source](https://platform.claude.com/docs/en/release-notes/overview)]

* Added a September 14, 2026 entry documenting the new `thinking_mismatch_allowed` entry type described above. [[line 389](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/api/release-notes/overview.md?plain=1#L389)] [[Source](https://platform.claude.com/docs/en/release-notes/overview#january-5-2026)]

#### [models/fable-5-1/migration-guide](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/api/models/fable-5-1/migration-guide.md) [[Source](https://platform.claude.com/docs/en/models/fable-5-1/migration-guide)]

* Cross-references the new `thinking_mismatch_allowed` entries as a way to check an existing integration for history edits without opting into enforcement, and retargets its compaction links to the new `compaction-on-demand`/`compaction-threshold` pages. [[lines 349-368](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/api/models/fable-5-1/migration-guide.md?plain=1#L349-L368)] [[Source](https://platform.claude.com/docs/en/models/fable-5-1/migration-guide#breaking-changes)]

#### [manage-claude/user-management](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/api/manage-claude/user-management.md) [[Source](https://platform.claude.com/docs/en/manage-claude/user-management)]

* RBAC groups API: path parameters and response fields were renamed for clarity — `{group_id}` path segments are now `{rbac_group_id}`, a group's `roles` field is now `role_ids` (with `roles` kept as a deprecated alias), and a group member's `group_id` is now `rbac_group_id` (with `group_id` kept as a deprecated alias). [[lines 176-330](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/api/manage-claude/user-management.md?plain=1#L176-L330)] [[Source](https://platform.claude.com/docs/en/manage-claude/user-management#invites)]
* Usage and cost reports for Claude Enterprise are now available through the Claude Enterprise Analytics API, split out into their own table row. [[lines 181-184](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/api/manage-claude/user-management.md?plain=1#L181-L184)] [[Source](https://platform.claude.com/docs/en/manage-claude/user-management#create-an-invite)]

#### [manage-claude/compliance-activity-feed](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/api/manage-claude/compliance-activity-feed.md) [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-activity-feed)]

* New `system_actor` activity-feed actor type for automated background processing that Anthropic runs without a user or customer credential. Also notes that some Anthropic-run migrations (such as memory-store migrations) currently attribute to `user_actor` instead, with `ip_address: 0.0.0.0`. [[lines 160-163](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/api/manage-claude/compliance-activity-feed.md?plain=1#L160-L163)] [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-activity-feed#understand-the-activity-object)]

#### [manage-claude/cmek](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/api/manage-claude/cmek.md) [[Source](https://platform.claude.com/docs/en/manage-claude/cmek)]

* Clarified CMEK coverage: Claude Design, Claude Slides, and Claude Docs are now explicitly called out as unavailable under CMEK (Claude Code also can't publish artifacts), where "artifacts" was previously bundled generically under covered chat content. [[lines 130-139](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/api/manage-claude/cmek.md?plain=1#L130-L139)] [[Source](https://platform.claude.com/docs/en/manage-claude/cmek#feature-support)]

#### [about-claude/models/optimizing-for-cost-and-intelligence](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/api/about-claude/models/optimizing-for-cost-and-intelligence.md) [[Source](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence)]

* Corrected the cache-read pricing note: it no longer claims a fixed 0.025× multiplier for Claude Fable 5.1 and Claude Mythos 5.1, noting instead that "some models use a different multiplier." [[lines 36-118](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/api/about-claude/models/optimizing-for-cost-and-intelligence.md?plain=1#L36-L118)] [[Source](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#start-here)]
* Anthropic now says explicitly that Opus 4.7, Opus 4.8, and Opus 5 are priced identically per token (previously phrased as "the Opus line" generally). [[line 28](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/api/about-claude/models/optimizing-for-cost-and-intelligence.md?plain=1#L28)] [[Source](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#start-here)]

#### Managed Agents guides ([quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/api/managed-agents/quickstart.md), [tools](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/api/managed-agents/tools.md), [scheduled-deployments](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/api/managed-agents/scheduled-deployments.md), [permission-policies](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/api/managed-agents/permission-policies.md), [memory](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/api/managed-agents/memory.md), [build-with-claude/skills-guide](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/api/build-with-claude/skills-guide.md))

* The CLI examples across these guides switched from heredoc commands like `ant beta:agents create <<YAML` to a new declarative `ant apply <file>` workflow: point it at an agent/deployment/environment/memory-store/skill file (frontmatter plus body, or a plain YAML file), and it creates or updates the resource and records the resulting ID in `claude-lock.json`. For skills, `ant apply <dir>` uploads the directory directly instead of requiring a manual `zip` step first.

#### Beta API reference (all languages, e.g. [api/beta](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/api/api/beta.md))

* Cross-cutting documentation pass across the entire Beta API reference — repeated identically for every per-language SDK reference page (Python, TypeScript, Java, Go, PHP, Ruby, C#, and the CLI) — with no functional change: every `anthropic-workspace-id`/`workspace_id` header now explains that it selects the Workspace for multi-workspace credentials, and enum-valued fields (such as effort levels and dream statuses) gained a one-line description for each value. This is the reason for the unusually large size of today's diff; it isn't itemized file by file here.

#### Feature-compatibility metadata migration (dozens of API reference and guide pages, e.g. [agents-and-tools/mcp-connector](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/api/agents-and-tools/mcp-connector.md), [managed-agents/overview](https://github.com/gpambrozio/ClaudeDocs/blob/c6428bfb1a061b27bd6045cd7cafa761c83cb718/docs-md/api/managed-agents/overview.md))

* Anthropic moved each page's "Compatibility" section (beta status, beta header, ZDR eligibility, supported models/platforms) from in-body Markdown into page frontmatter (`featureMetadata`). This is a rendering/authoring change with no content difference, affecting most tool, guide, and managed-agents pages; also not itemized file by file here.
