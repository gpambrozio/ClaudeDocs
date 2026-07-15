# [Claude docs changes for July 15th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/07f074583747c34cd0d0915415b449247f23387d) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/07f074583747c34cd0d0915415b449247f23387d)]

## Executive Summary
- New Admin API endpoints for RBAC (role-based access control) groups and custom roles, plus a new Claude Enterprise user-management guide, let admins programmatically manage members, invites, and access control instead of relying on the claude.ai UI.
- Managed Agents API gains multiagent orchestration: a coordinator agent can now delegate work to a roster of other agents (or copies of itself), each running in its own isolated session thread.
- Claude Code 2.1.210 bundles several security hardening fixes — isolated worktree subagents could previously run git commands against the main repo, the Agent tool is now hardened against indirect prompt injection, and `Read` deny rules now also block the Edit tool on the same path.
- New `CLAUDE_CODE_PROCESS_WRAPPER` environment variable and corporate-launcher support let enterprises force every process Claude Code spawns through a mandatory security wrapper script.
- Claude Code 2.1.210 also fixes numerous background-session reliability issues: `claude attach` failures during session transitions, permanent worktree locks left behind by killed sessions, and hook-callback timeouts being misreported as user rejections.

## New Claude Code versions

### [2.1.210](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/versions/2.1.210.md)

#### New features

* Added a live elapsed-time counter to the collapsed tool summary line so long-running tool calls visibly tick instead of looking stuck
* Added a startup warning for `Write(path)`, `NotebookEdit(path)`, and `Glob(path)` permission rules — use `Edit(path)` or `Read(path)` instead

#### Existing feature improvements

* Improved the Bash/PowerShell tool message when a command hits its timeout and is auto-backgrounded, so the model can distinguish a hang from an explicit background request
* Improved auto mode: the permission classifier now defaults to Sonnet 5 for external sessions, validated on the session's first request and pinned for the session
* Improved the bundled dataviz skill's chart color validation with perceptual OKLab color difference and recalibrated color-blindness thresholds
* Screen reader mode now announces permission mode changes aloud when cycling modes with Shift+Tab
* The agents footer hint now shows how many background agents are waiting on your input, with a brief color emphasis when the count changes
* Agent view: the session you pressed ← from stays visibly marked even after mouse hover or arrow keys move the selection

#### Major bug fixes

* Fixed `isolation: 'worktree'` subagents being able to run git-mutating commands against the main repo checkout instead of their own isolated worktree
* Fixed the `ultracode` keyword opt-in firing on non-human-originated input such as webhook payloads and relayed PR comments
* Fixed paste markers leaking into external editors opened from Claude Code, which could appear as stray È/É characters around pasted text
* Fixed `claude attach` sometimes failing with "job not found" or "agent is still starting" errors during session transitions — attach now waits for the daemon to settle, and terminal resizes during a slow attach are applied once it completes
* Fixed a session crash when a tool's result renderer returned a numeric bigint value or plain text instead of a UI element
* Fixed a hook callback timeout being misreported to the model as a user rejection, which made unattended sessions stop and wait
* Fixed Claude assuming a `cd` took effect after its command was moved to the background; the tool result now states the working directory is unchanged
* Fixed plugin-provided MCP servers being torn down when MCP servers are re-synced mid-session
* Fixed plan approvals without edits being labeled "(edited by user)" and overwriting the plan file with a stale snapshot
* Fixed `/doctor` skipping its auto-mode-default proposal on Bedrock, Vertex, and Foundry, where auto mode no longer needs an opt-in
* Fixed Grep content mode claiming "No matches found" when paginating past the end of results
* Fixed unmatched `$1`/`$2` positional placeholders in skills and commands being silently stripped; they are now preserved verbatim
* Fixed plugin cache writes leaving temp files behind on failure and failing on locked-file renames on Windows and network filesystems
* Fixed background workers crash-looping when a client resets its connection to the background service
* Fixed `claude agents --effort ultracode` not reaching dispatched sessions; the value was silently dropped
* Fixed pressing ← to open the agents view dropping the task tracker when returning to the session
* Fixed the agents dashboard retaining pasted images from abandoned reply drafts after their session was deleted
* Fixed killed background sessions leaving a permanent `git worktree lock` behind; the periodic sweep now releases locks whose owning process is gone
* Fixed SDK MCP servers registered via an `initialize` control request waiting until the next turn to start connecting
* Fixed returning to the agents view from a session leaving overlapping ghost frames with `CLAUDE_CODE_DISABLE_ALTERNATE_SCREEN=1`
* Fixed late-appearing `.claude/*` symlinks not being reconciled into the sandbox deny-write list
* Hardened the Agent tool against indirect prompt injection via content a subagent read
* Memory writes that leave a MEMORY.md index over its read limit now produce an explicit error instead of silent truncation
* Fable temporarily shows as unavailable in the advisor picker while a server-side issue causing Fable advisor failures is fixed

-----

## Claude Code changes

### New Documents

#### [corporate-launcher](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/corporate-launcher.md) [[Source](https://code.claude.com/docs/en/corporate-launcher)]

Documents the new `CLAUDE_CODE_PROCESS_WRAPPER` environment variable (Claude Code v2.1.208+), which lets organizations force every process Claude Code spawns — the background service, agent view sessions, and self-update relaunches — to start through a mandatory corporate launcher script that applies sandboxing, network controls, or credential injection. It covers what the launcher does and doesn't cover (ignored on Windows, doesn't catch manually started terminal sessions or deep-link launches), the strict "launcher contract" a script must follow (must end in `exec "$@"`, must pass through all inherited env vars, must respond within ~3 seconds), setup via managed settings, and how it differs from the related `CLAUDE_CODE_SHELL_PREFIX` variable.

### Changed documents

#### [accessibility](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/accessibility.md) [[Source](https://code.claude.com/docs/en/accessibility)]

* Clarifies that when Claude Code relaunches itself (e.g., to finish installing an update), the new process inherits screen reader mode via the `CLAUDE_AX_SCREEN_READER` environment variable, so its confirmation line always reads "on via env" regardless of the original activation method. [[line 19](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/accessibility.md?plain=1#L19)] [[Source](https://code.claude.com/docs/en/accessibility#turn-on-screen-reader-mode)]

#### [admin-setup](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/admin-setup.md) [[Source](https://code.claude.com/docs/en/admin-setup)]

* Documents a new admin surface for Claude Code on the web: owners/admins can create organization-shared cloud environments (network access level, env vars, setup script) and set an org default environment. [[line 81](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/admin-setup.md?plain=1#L81)] [[Source](https://code.claude.com/docs/en/admin-setup#decide-what-to-enforce)]

#### [agent-sdk/hooks](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/agent-sdk/hooks.md) [[Source](https://code.claude.com/docs/en/agent-sdk/hooks)]

* New `UserPromptExpansion` hook documented: fires when a user-typed command expands into a prompt before reaching Claude. [[line 155](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/agent-sdk/hooks.md?plain=1#L155)] [[Source](https://code.claude.com/docs/en/agent-sdk/hooks#available-hooks)]
* Clarifies timeout/interrupt semantics for `UserPromptSubmit`/`UserPromptExpansion`: a timeout now blocks the prompt with a message instead of ending the query with `error_during_execution` (fixed in v2.1.208). [[line 775](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/agent-sdk/hooks.md?plain=1#L775)] [[Source](https://code.claude.com/docs/en/agent-sdk/hooks#hook-timeout)]

#### [agent-sdk/typescript](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* `setMaxThinkingTokens()` now documented to reset thinking to the session default when passed `null`. [[line 509](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L509)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#methods)]
* New `SDKThinkingTokensMessage` type emitted during thinking blocks with running token estimates (requires v2.1.153+). [[lines 974-3336](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L974-L3336)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#sdkmessage)]

#### [agent-view](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/agent-view.md) [[Source](https://code.claude.com/docs/en/agent-view)]

* New footer hint in a regular `claude` session shows a count of background agents waiting on you (e.g. `← 2 agents`), refreshing periodically; requires v2.1.205+. [[line 61](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/agent-view.md?plain=1#L61)] [[Source](https://code.claude.com/docs/en/agent-view#quick-start)]
* A reply to a background session that can't be delivered is now saved and sent as the session's next prompt when it restarts, instead of being discarded. [[line 162](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/agent-view.md?plain=1#L162)] [[Source](https://code.claude.com/docs/en/agent-view#peek-and-reply)]
* Background sessions now refuse `/install-github-app` and the `/mcp` settings list (including auth actions), directing users to a regular session; `/mcp reconnect|enable|disable` still work. [[line 170](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/agent-view.md?plain=1#L170)] [[Source](https://code.claude.com/docs/en/agent-view#attach-to-a-session)]
* Deleting a session no longer removes a worktree with unpushed commits or one claimed/locked by another session; both the worktree and session row are kept with a reason shown. [[lines 195-196](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/agent-view.md?plain=1#L195-L196)] [[Source](https://code.claude.com/docs/en/agent-view#organize-the-list)]
* `/model` behavior changed: picking from the picker or typing `/model <name>` now saves as the default for new sessions, unless `s` is pressed for a session-only switch. [[line 395](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/agent-view.md?plain=1#L395)] [[Source](https://code.claude.com/docs/en/agent-view#set-the-model)]
* If a running process's own binary was replaced by an update, it can still start the supervisor from another installed copy instead of failing. [[line 463](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/agent-view.md?plain=1#L463)] [[Source](https://code.claude.com/docs/en/agent-view#the-supervisor-process)]
* Supervisor version-restart logic now only ever moves sessions to a newer version, never restarting a session onto an older binary. [[line 487](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/agent-view.md?plain=1#L487)] [[Source](https://code.claude.com/docs/en/agent-view#the-supervisor-process)]
* Attaching to a stopped session's process now shows the last screenful of transcript with a "Session is starting" note instead of just the note. [[line 581](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/agent-view.md?plain=1#L581)] [[Source](https://code.claude.com/docs/en/agent-view#a-session-is-slow-to-respond-after-attaching)]

#### [agents](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/agents.md) [[Source](https://code.claude.com/docs/en/agents)]

* `/tasks` now also lists subagents that have finished, not just running ones. [[line 44](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/agents.md?plain=1#L44)] [[Source](https://code.claude.com/docs/en/agents#check-on-running-work)]

#### [amazon-bedrock](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/amazon-bedrock.md) [[Source](https://code.claude.com/docs/en/amazon-bedrock)]

* Clarifies IAM Identity Center `sso_region` handling and documents a v2.1.207 regression where the Bedrock region incorrectly overrode it, breaking auth. [[line 82](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/amazon-bedrock.md?plain=1#L82)] [[Source](https://code.claude.com/docs/en/amazon-bedrock#2-configure-aws-credentials)]
* New troubleshooting section for streaming errors caused by a gateway/proxy altering the event-stream content-type, including a new env var workaround. [[line 410](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/amazon-bedrock.md?plain=1#L410)] [[Source](https://code.claude.com/docs/en/amazon-bedrock#streaming-errors-behind-a-gateway-or-proxy)]

#### [authentication](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/authentication.md) [[Source](https://code.claude.com/docs/en/authentication)]

* `apiKeyHelper` failures now surface a specific error within 3 attempts instead of a generic 401 after ~10 silent retries (v2.1.208). [[line 133](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/authentication.md?plain=1#L133)] [[Source](https://code.claude.com/docs/en/authentication#credential-management)]

#### [auto-mode-config](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/auto-mode-config.md) [[Source](https://code.claude.com/docs/en/auto-mode-config)]

* New `--label <prefix>` flag for `claude auto-mode defaults` to print a specific rule's full wording (v2.1.208+). [[line 211](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/auto-mode-config.md?plain=1#L211)] [[Source](https://code.claude.com/docs/en/auto-mode-config#inspect-the-defaults-and-your-effective-config)]

#### [checkpointing](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/checkpointing.md) [[Source](https://code.claude.com/docs/en/checkpointing)]

* Documents a 100-checkpoint retention limit for file snapshots per session, with pruning behavior fixed in v2.1.208 (previously superseded snapshots weren't cleaned up until session cleanup). [[line 14](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/checkpointing.md?plain=1#L14)] [[Source](https://code.claude.com/docs/en/checkpointing#automatic-tracking)]

#### [claude-code-on-the-web](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/claude-code-on-the-web.md) [[Source](https://code.claude.com/docs/en/claude-code-on-the-web)]

* New "Organization-shared environments" feature for Team/Enterprise: shared cloud environments managed centrally by admins. [[lines 159-168](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L159-L168)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#organization-shared-environments)]
* Clarifies there's no org-level allowed-domains push mechanism. [[line 285](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L285)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#allow-specific-domains)]
* GitHub proxy now restricts API/release-asset requests to repos attached to the session, returning 403 otherwise. [[line 294](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L294)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#github-proxy)]

#### [claude-directory](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/claude-directory.md) [[Source](https://code.claude.com/docs/en/claude-directory)]

* Documents the 100-checkpoint snapshot retention/pruning behavior for `file-history/<session>/`. [[line 190](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/claude-directory.md?plain=1#L190)] [[Source](https://code.claude.com/docs/en/claude-directory#cleaned-up-automatically)]

#### [cli-reference](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* New `--label <prefix>` flag documented for `claude auto-mode defaults` (v2.1.208+). [[line 22](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/cli-reference.md?plain=1#L22)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-commands)]

#### [commands](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/commands.md) [[Source](https://code.claude.com/docs/en/commands)]

* Clarifies command queuing behavior: most commands queue until the current turn finishes, but `/status`, `/tasks`, `/usage` run immediately. [[line 6](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/commands.md?plain=1#L6)] [[Source](https://code.claude.com/docs/en/commands)]
* `/release-notes` no longer injects viewed notes into the conversation Claude sees (fixed v2.1.208 regression). [[line 93](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/commands.md?plain=1#L93)] [[Source](https://code.claude.com/docs/en/commands#all-commands)]
* `/resume` clarified: a still-running background session can't be resumed there; must attach via `claude agents` or stop it first. [[line 99](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/commands.md?plain=1#L99)] [[Source](https://code.claude.com/docs/en/commands#all-commands)]
* `/tasks` now includes finished subagents. [[line 117](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/commands.md?plain=1#L117)] [[Source](https://code.claude.com/docs/en/commands#all-commands)]
* `/upgrade` now shows a sign-in prompt instead of printing a URL when the browser fails to open. [[line 125](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/commands.md?plain=1#L125)] [[Source](https://code.claude.com/docs/en/commands#all-commands)]

#### [costs](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/costs.md) [[Source](https://code.claude.com/docs/en/costs)]

* `/usage` now shows last-known usage bars (within 60 min) with a retry option when the plan-limits request is rate limited, instead of always showing an error. [[line 23](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/costs.md?plain=1#L23)] [[Source](https://code.claude.com/docs/en/costs#using-the-/usage-command)]
* Typed `yes` confirmation now required for every usage-credit purchase/auto-reload change (not just above $1,000); spend-limit changes keep the $1,000 threshold. [[line 38](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/costs.md?plain=1#L38)] [[Source](https://code.claude.com/docs/en/costs#set-a-spend-limit-on-pro-and-max)]
* Amount fields now open prefilled (first digit replaces suggestion); usage-credits enable screen now defaults to Cancel selected. [[line 39](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/costs.md?plain=1#L39)] [[Source](https://code.claude.com/docs/en/costs#set-a-spend-limit-on-pro-and-max)]

#### [data-usage](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/data-usage.md) [[Source](https://code.claude.com/docs/en/data-usage)]

* Clarifies that Remote Control sessions store the transcript on Anthropic servers while connected, to sync across devices. [[line 50](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/data-usage.md?plain=1#L50)] [[Source](https://code.claude.com/docs/en/data-usage#data-access)]

#### [desktop-quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/desktop-quickstart.md) [[Source](https://code.claude.com/docs/en/desktop-quickstart)]

* Clarifies Cowork now distinguishes on-device VMs (run locally) from remote Cowork sessions (run on an Anthropic-managed VM). [[line 25](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/desktop-quickstart.md?plain=1#L25)] [[Source](https://code.claude.com/docs/en/desktop-quickstart)]

#### [discover-plugins](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/discover-plugins.md) [[Source](https://code.claude.com/docs/en/discover-plugins)]

* Clarifies plugin auto-update timing: checks run after session start with up to a 10-minute random delay, and updates only apply to the running session after `/reload-plugins` or on next launch. [[line 376](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/discover-plugins.md?plain=1#L376)] [[Source](https://code.claude.com/docs/en/discover-plugins#configure-auto-updates)]

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* Clarifies precedence: settings-file `env` block values override the same variable inherited from the shell. [[line 72](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/env-vars.md?plain=1#L72)] [[Source](https://code.claude.com/docs/en/env-vars#precedence)]
* New `CLAUDE_CODE_DISABLE_BEDROCK_CONTENT_TYPE_GUARD` env var to skip the Bedrock streaming content-type check (v2.1.208+). [[line 168](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/env-vars.md?plain=1#L168)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* New `CLAUDE_CODE_PROCESS_WRAPPER` env var to launch Claude Code's own spawned processes through a corporate launcher wrapper. [[line 247](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/env-vars.md?plain=1#L247)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* New "Your apiKeyHelper script is failing" error documented, replacing the previous generic 401 after ~10 retries (v2.1.208). [[lines 382-387](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/errors.md?plain=1#L382-L387)] [[Source](https://code.claude.com/docs/en/errors#your-apikeyhelper-script-is-failing)]
* New "Bedrock streaming response has an unexpected content-type" error, not retried, replacing the old "Truncated event message received" symptom. [[line 612](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/errors.md?plain=1#L612)] [[Source](https://code.claude.com/docs/en/errors#bedrock-streaming-response-has-an-unexpected-content-type)]
* New "Agent would be spawned with zero tools" error: Claude Code now refuses to launch a subagent whose `tools` list resolves to nothing, instead of launching it with no tools. [[lines 1087-1091](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/errors.md?plain=1#L1087-L1091)] [[Source](https://code.claude.com/docs/en/errors#tool-errors)]
* New "File is covered by a Read deny rule" error: Edit tool calls are now blocked by `Read` deny rules (Write/NotebookEdit unaffected), a behavior change from v2.1.208. [[line 1105](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/errors.md?plain=1#L1105)] [[Source](https://code.claude.com/docs/en/errors#file-is-covered-by-a-read-deny-rule)]
* New "Background session errors" section documenting commands refused in background sessions (`/install-github-app`, `/mcp` settings) and `CLAUDE_CODE_PROCESS_WRAPPER` launcher errors. [[lines 1118-1122](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/errors.md?plain=1#L1118-L1122)] [[Source](https://code.claude.com/docs/en/errors#background-session-errors)]

#### [fast-mode](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/fast-mode.md) [[Source](https://code.claude.com/docs/en/fast-mode)]

* Clarifies fast mode re-activation behavior when switching models, including interaction with per-session opt-in; fixes a v2.1.208 bug where fast mode stayed off after switching back to Opus. [[line 34](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/fast-mode.md?plain=1#L34)] [[Source](https://code.claude.com/docs/en/fast-mode#toggle-fast-mode)]

#### [fullscreen](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/fullscreen.md) [[Source](https://code.claude.com/docs/en/fullscreen)]

* New mouse interaction support for multi-select menus (toggle options, click submit) and free-text rows in multiple-choice questions (v2.1.208+). [[line 42](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/fullscreen.md?plain=1#L42)] [[Source](https://code.claude.com/docs/en/fullscreen#use-the-mouse)]

#### [headless](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/headless.md) [[Source](https://code.claude.com/docs/en/headless)]

* Documents that the last line of `stream-json` output is a `result` message with the final response text, cost, and session metadata; before v2.1.208, piping a large response could truncate the final line and omit that message. [[line 131](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/headless.md?plain=1#L131)] [[Source](https://code.claude.com/docs/en/headless#stream-responses)]

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* Distinguishes timeout behavior for `UserPromptSubmit` command/HTTP/MCP-tool hooks from Agent SDK callback hooks: a callback hook timeout on `UserPromptSubmit` now blocks the prompt with a message naming the hook instead of ending the turn with an execution error (before v2.1.208). [[lines 1030-1031](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/hooks.md?plain=1#L1030-L1031)] [[Source](https://code.claude.com/docs/en/hooks#userpromptsubmit)]

#### [interactive-mode](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* `Ctrl+O` transcript viewer now shows a timestamp and the model used on each assistant message. [[line 20](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/interactive-mode.md?plain=1#L20)] [[Source](https://code.claude.com/docs/en/interactive-mode#general-controls)]
* New `vimInsertModeRemaps` setting (v2.1.208+) maps a two-key INSERT-mode sequence like `jj` to Escape in vim editor mode; only read from user settings, `--settings`, or managed settings, not project/local settings. [[lines 116-130](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/interactive-mode.md?plain=1#L116-L130)] [[Source](https://code.claude.com/docs/en/interactive-mode#remap-insert-mode-key-sequences)]

#### [keybindings](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/keybindings.md) [[Source](https://code.claude.com/docs/en/keybindings)]

* Notes that vim keys aren't remappable via the keybindings file, and points to the new `vimInsertModeRemaps` setting for remapping a two-key INSERT-mode sequence to Escape. [[line 452](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/keybindings.md?plain=1#L452)] [[Source](https://code.claude.com/docs/en/keybindings#vim-mode-interaction)]

#### [llm-gateway-connect](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/llm-gateway-connect.md) [[Source](https://code.claude.com/docs/en/llm-gateway-connect)]

* New troubleshooting row for "Your apiKeyHelper script is failing", explaining that a failing/timing-out/empty-output `apiKeyHelper` command causes requests to carry a placeholder key. [[line 414](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/llm-gateway-connect.md?plain=1#L414)] [[Source](https://code.claude.com/docs/en/llm-gateway-connect#troubleshoot-gateway-errors)]

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* A remote MCP server with an empty `url` now shows as `not configured` in `/mcp`, `claude mcp list`, and `/plugin` rather than being reported as a configuration issue (before v2.1.208). [[line 152](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/mcp.md?plain=1#L152)] [[Source](https://code.claude.com/docs/en/mcp#managing-your-servers)]
* Replaces the generic `${CLAUDE_PLUGIN_ROOT}`/`${CLAUDE_PLUGIN_DATA}`/`${CLAUDE_PROJECT_DIR}` description with a table specifying exactly which fields substitute placeholders per transport (stdio vs. http/sse/ws), noting `headersHelper` didn't substitute placeholders before v2.1.195. [[line 234](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/mcp.md?plain=1#L234)] [[Source](https://code.claude.com/docs/en/mcp#plugin-provided-mcp-servers)]
* Clarifies the `headersHelper` command runs from the session's current working directory, so scripts should use an absolute path or one on `PATH`. [[line 670](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/mcp.md?plain=1#L670)] [[Source](https://code.claude.com/docs/en/mcp#use-dynamic-headers-for-custom-authentication)]

#### [model-config](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* `CLAUDE_CODE_SUBAGENT_MODEL` now also applies to the agents a dynamic workflow runs (previously just subagents/agent teams), and documents it accepts an alias or a full model name. [[line 496](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/model-config.md?plain=1#L496)] [[Source](https://code.claude.com/docs/en/model-config#environment-variables)]

#### [permission-modes](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/permission-modes.md) [[Source](https://code.claude.com/docs/en/permission-modes)]

* Auto mode now prompts for approval (instead of going to the classifier) for `rm -rf /` / `rm -rf ~`-style removals, including when wrapped in command/process substitution such as `echo "$(rm -rf ~)"` (before v2.1.208 these went to the classifier). [[line 148](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/permission-modes.md?plain=1#L148)] [[Source](https://code.claude.com/docs/en/permission-modes#eliminate-prompts-with-auto-mode)]
* `bypassPermissions` circuit breaker for root/home-directory removals is clarified to also catch command/process-substitution forms, and MCP tools requiring user interaction still prompt (requires v2.1.199+). [[lines 313-314](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/permission-modes.md?plain=1#L313-L314)] [[Source](https://code.claude.com/docs/en/permission-modes#skip-all-checks-with-bypasspermissions-mode)]

#### [permissions](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/permissions.md) [[Source](https://code.claude.com/docs/en/permissions)]

* `bypassPermissions` mode's circuit breaker against `rm -rf /`/`rm -rf ~` now also fires for commands that reach the removal through command or process substitution (v2.1.208 extends the existing plain-form check). [[line 45](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/permissions.md?plain=1#L45)] [[Source](https://code.claude.com/docs/en/permissions#permission-modes)]
* New behavior: a `Read` deny rule also blocks the Edit tool on the same path, including creating a new file there (Write/NotebookEdit aren't covered); requires v2.1.208+. [[line 213](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/permissions.md?plain=1#L213)] [[Source](https://code.claude.com/docs/en/permissions#read-and-edit)]

#### [plugin-marketplaces](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/plugin-marketplaces.md) [[Source](https://code.claude.com/docs/en/plugin-marketplaces)]

* Points plugin authors to the new substitution table in plugins-reference.md for which config fields substitute `${CLAUDE_PLUGIN_ROOT}` per server type. [[line 471](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/plugin-marketplaces.md?plain=1#L471)] [[Source](https://code.claude.com/docs/en/plugin-marketplaces#advanced-plugin-entries)]

#### [plugins-reference](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/plugins-reference.md) [[Source](https://code.claude.com/docs/en/plugins-reference)]

* Example MCP plugin config drops the `"cwd": "${CLAUDE_PLUGIN_ROOT}"` field. [[line 155](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/plugins-reference.md?plain=1#L155)] [[Source](https://code.claude.com/docs/en/plugins-reference#mcp-servers)]
* Clarifies monitor processes don't receive `CLAUDE_PLUGIN_OPTION_<KEY>` environment variables, so scripts must read values from a config file instead. [[line 292](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/plugins-reference.md?plain=1#L292)] [[Source](https://code.claude.com/docs/en/plugins-reference#monitors)]
* Adds a table of which fields reject `${user_config.*}` substitution (shell-form hook commands, monitor commands, MCP `headersHelper`) and the alternative way to pass each value. [[lines 525-533](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/plugins-reference.md?plain=1#L525-L533)] [[Source](https://code.claude.com/docs/en/plugins-reference#user-configuration)]
* Adds a table specifying exactly which fields substitute `${CLAUDE_PLUGIN_ROOT}`/`${CLAUDE_PLUGIN_DATA}`/`${CLAUDE_PROJECT_DIR}` per component (skills/agents, hooks/monitors, MCP stdio vs. http/sse/ws, and LSP servers). [[lines 610-616](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/plugins-reference.md?plain=1#L610-L616)] [[Source](https://code.claude.com/docs/en/plugins-reference#environment-variables)]

#### [remote-control](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/remote-control.md) [[Source](https://code.claude.com/docs/en/remote-control)]

* Connecting a new device now immediately shows subagents/workflows already running in the background (before v2.1.208 it waited for one to start or stop). [[line 103](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/remote-control.md?plain=1#L103)] [[Source](https://code.claude.com/docs/en/remote-control#connect-from-another-device)]
* New disclosure: while Remote Control is connected, the full session transcript (messages, responses, tool activity) is stored on Anthropic servers to sync across devices and support reconnection; documents the `disableRemoteControl` setting to turn the feature off, and that ZDR orgs can't enable it. [[lines 124-125](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/remote-control.md?plain=1#L124-L125)] [[Source](https://code.claude.com/docs/en/remote-control#connection-and-security)]

#### [security](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/security.md) [[Source](https://code.claude.com/docs/en/security)]

* Updates the Remote Control security description to disclose that the session transcript is stored on Anthropic servers to sync the conversation across devices. [[line 94](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/security.md?plain=1#L94)] [[Source](https://code.claude.com/docs/en/security#cloud-execution-security)]

#### [settings](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* New `fastMode` setting documented: turns fast mode on for eligible sessions, written by `/fast`. [[line 235](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/settings.md?plain=1#L235)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]
* New `vimInsertModeRemaps` setting documented (v2.1.208+), including its user/managed-settings-only scoping. [[line 293](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/settings.md?plain=1#L293)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]
* Notes that a `Read` deny rule also blocks the Edit tool on matching paths. [[line 429](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/settings.md?plain=1#L429)] [[Source](https://code.claude.com/docs/en/settings#sandbox-path-prefixes)]

#### [sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* If no entry in a subagent's `tools` list resolves to a real tool, the subagent now fails to launch with an error naming the entries, instead of launching with no tools (before v2.1.208). [[lines 229, 299](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/sub-agents.md?plain=1#L229)]
* A completed background subagent now stays listed in `/tasks` (marked done, sorted below running work) until session cleanup, with its detail view staying open; before v2.1.208 it disappeared immediately on completion. [[line 669](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/sub-agents.md?plain=1#L669)] [[Source](https://code.claude.com/docs/en/sub-agents#run-subagents-in-foreground-or-background)]

#### [terminal-config](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/terminal-config.md) [[Source](https://code.claude.com/docs/en/terminal-config)]

* Points to the new `vimInsertModeRemaps` setting as the way to map a two-key INSERT-mode sequence (e.g. `jj`) to Escape, since vim motions aren't remappable via the keybindings file. [[line 282](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/terminal-config.md?plain=1#L282)] [[Source](https://code.claude.com/docs/en/terminal-config#edit-prompts-with-vim-keybindings)]

#### [tools-reference](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/tools-reference.md) [[Source](https://code.claude.com/docs/en/tools-reference)]

* Documents that a subagent whose `tools` list resolves to no tools now fails to launch with an error, rather than launching with no tools (before v2.1.208). [[line 92](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/tools-reference.md?plain=1#L92)] [[Source](https://code.claude.com/docs/en/tools-reference#agent-tool-behavior)]
* Read-before-edit rules relaxed (v2.1.208+): newer models can edit an unread file when reading wouldn't need a permission prompt, and a path blocked by a `Read` deny rule is refused up front. [[line 122](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/tools-reference.md?plain=1#L122)] [[Source](https://code.claude.com/docs/en/tools-reference#edit-tool-behavior)]
* A file changed on disk since last read can now still be edited if `old_string` matches the current content exactly/unambiguously and the file is readable without a prompt (before v2.1.208, any on-disk change blocked the edit). [[line 128](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/tools-reference.md?plain=1#L128)] [[Source](https://code.claude.com/docs/en/tools-reference#edit-tool-behavior)]
* Glob now returns an explicit error for a `pattern`/`path` containing a null byte. [[line 142](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/tools-reference.md?plain=1#L142)] [[Source](https://code.claude.com/docs/en/tools-reference#glob-tool-behavior)]
* Grep now surfaces ripgrep's diagnostic as an error for a rejected pattern/glob/type instead of silently reporting `No files found` (before v2.1.208). [[line 148](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/tools-reference.md?plain=1#L148)] [[Source](https://code.claude.com/docs/en/tools-reference#grep-tool-behavior)]
* Grep's `count` mode now also reports a total across all matching files, even when `head_limit`/`offset` truncate the listed entries (before v2.1.208 the total only summed listed entries). [[line 153](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/tools-reference.md?plain=1#L153)] [[Source](https://code.claude.com/docs/en/tools-reference#grep-tool-behavior)]
* Read with an explicit `limit` now stops and errors as soon as selected lines exceed what could ever fit, instead of loading the whole range first (fixes a memory-exhaustion risk, before v2.1.208); also fixes empty-file reads to report an "empty" notice rather than a past-the-end notice. [[lines 267-268](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/tools-reference.md?plain=1#L267-L268)] [[Source](https://code.claude.com/docs/en/tools-reference#read-tool-behavior)]

#### [troubleshoot-install](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/troubleshoot-install.md) [[Source](https://code.claude.com/docs/en/troubleshoot-install)]

* Corrects install guidance for Windows certificate-revocation-check failures: the previously documented `--ssl-revoke-best-effort` curl flag doesn't actually fix the problem (it only covers the initial script download); recommends running the PowerShell installer (`irm https://claude.ai/install.ps1 | iex`) instead. [[line 381](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/troubleshoot-install.md?plain=1#L381)] [[Source](https://code.claude.com/docs/en/troubleshoot-install#tls-or-ssl-connection-errors)]

#### [troubleshooting](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/troubleshooting.md) [[Source](https://code.claude.com/docs/en/troubleshooting)]

* New section: Markdown tables over 200 rows now render only the first 200 with a "more rows not shown" note (full data still in the conversation and copyable); before v2.1.208 rendering every row could stall on resuming a session with a very large table. [[lines 35-37](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/troubleshooting.md?plain=1#L35-L37)] [[Source](https://code.claude.com/docs/en/troubleshooting#large-tables-are-cut-off-in-the-terminal)]

#### [workflows](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/workflows.md) [[Source](https://code.claude.com/docs/en/workflows)]

* Saved personal workflows now respect `CLAUDE_CONFIG_DIR`, and the save dialog shows the resolved path (before v2.1.208 it displayed the default path even when saved elsewhere). [[lines 158-160](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/workflows.md?plain=1#L158-L160)] [[Source](https://code.claude.com/docs/en/workflows#save-the-workflow-for-reuse)]
* Clarifies resume semantics: an agent still running when a workflow is stopped is not cached and restarts from scratch on resume, favoring workflows that fan out into many small agents. [[line 274](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/workflows.md?plain=1#L274)] [[Source](https://code.claude.com/docs/en/workflows#resume-after-a-pause)]
* Notes `CLAUDE_CODE_SUBAGENT_MODEL` overrides both the session model and per-stage script routing for workflow agents. [[line 287](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/workflows.md?plain=1#L287)] [[Source](https://code.claude.com/docs/en/workflows#cost)]

#### [worktrees](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/worktrees.md) [[Source](https://code.claude.com/docs/en/worktrees)]

* Worktree base-branch resolution now refreshes `origin/HEAD` with a capped 5-second fetch when nothing has fetched in the last 24 hours, falling back to the cached ref or local `HEAD` (requires v2.1.208+). [[lines 38-39](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/worktrees.md?plain=1#L38-L39)] [[Source](https://code.claude.com/docs/en/worktrees#choose-the-base-branch)]
* New "Reuse a worktree name" section: a resumed worktree (same name) now resets to the current base rather than resuming at its old tip, when it has no local/uncommitted changes, is still on its original branch, and was never committed or its PR was merged/branch deleted; before v2.1.208 a reused name always resumed at the old tip. [[lines 58-67](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/worktrees.md?plain=1#L58-L67)] [[Source](https://code.claude.com/docs/en/worktrees#reuse-a-worktree-name)]

#### [zero-data-retention](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/zero-data-retention.md) [[Source](https://code.claude.com/docs/en/zero-data-retention)]

* Adds Remote Control to the table of features blocked under Zero Data Retention, since it stores the session transcript on Anthropic servers. [[line 48](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/claude-code/zero-data-retention.md?plain=1#L48)] [[Source](https://code.claude.com/docs/en/zero-data-retention#features-disabled-under-zdr)]

-----

## API changes

### New Documents

#### [multiagent-orchestration](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/managed-agents/multiagent-orchestration.md) [[Source](https://platform.claude.com/docs/en/managed-agents/multiagent-orchestration)]

Introduces multiagent orchestration for the Managed Agents API, where a coordinator agent delegates work to a roster of other agents (or copies of itself), each running in an isolated session thread with its own model, tools, and MCP servers. Covers configuring `multiagent.agents` on a coordinator, per-agent MCP server scoping, thread limits (20 roster agents, 25 concurrent threads, one delegation level deep), and the primary-thread event types used to monitor and route tool permissions across threads.

#### [rbac_groups](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/rbac_groups.md) [[Source](https://platform.claude.com/docs/en/api/admin/rbac_groups)] / [rbac_roles](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/rbac_roles.md)

New Admin API endpoint reference for RBAC (role-based access control) Groups and Roles, covering the full CRUD surface for groups (list/get/create/rename/delete plus add/remove/list members) and read-only endpoints for custom roles and their permissions. These endpoints let Claude Enterprise admins programmatically manage groups (which can be `direct` or identity-provider-provisioned `scim`) and inspect which custom roles and permissions are attached, enabling automation of enterprise access-control workflows that previously required the claude.ai admin UI.

#### [user-management](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/manage-claude/user-management.md) [[Source](https://platform.claude.com/docs/en/manage-claude/user-management)]

A new beta guide for Claude Enterprise organizations covering programmatic management of members, invites, RBAC groups, and custom roles under the Admin API. Details the new `read:rbac_groups`/`write:rbac_groups` scopes, the required `anthropic-beta: ce-user-management-2026-07-13` header for group and role calls, organization roles (`user`, `managed`, `owner`, etc.), seat-pool behavior on invites, and example workflows like offboarding and group-membership auditing.

### Changed documents

#### [api/admin](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin.md) [[Source](https://platform.claude.com/docs/en/api/admin)]

* Documents new RBAC Groups and RBAC Roles endpoints (list/get/create/update/delete groups, group members, list/get roles, list role permissions). [[lines 51-102](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin.md?plain=1#L51-L102)] [[Source](https://platform.claude.com/docs/en/api/admin)]

#### [api/admin/analytics/chat_projects/list](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/analytics/chat_projects/list.md) [[Source](https://platform.claude.com/docs/en/api/admin/analytics/chat_projects/list)]

* Clarifies `order_by`: rankable metrics are no longer limited to date-range mode overall — only a few specific metrics are date-range-only, per each endpoint's documented orderable set. [[line 55](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/analytics/chat_projects/list.md?plain=1#L55)] [[Source](https://platform.claude.com/docs/en/api/admin/analytics/chat_projects/list)]

#### [api/admin/analytics/connectors/list](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/analytics/connectors/list.md) [[Source](https://platform.claude.com/docs/en/api/admin/analytics/connectors/list)]

* Same `order_by` semantics correction as above. [[line 57](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/analytics/connectors/list.md?plain=1#L57)] [[Source](https://platform.claude.com/docs/en/api/admin/analytics/connectors/list)]

#### [api/admin/analytics/cost](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/analytics/cost.md) [[Source](https://platform.claude.com/docs/en/api/admin/analytics/cost)]

* Adds a new `product` value "claude-in-slack" (Claude Tag) and documents a distinct legacy underscore-spelled value for the retiring v1 Slack chat bot. [[line 81](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/analytics/cost.md?plain=1#L81)] [[Source](https://platform.claude.com/docs/en/api/admin/analytics/cost)]

#### [api/admin/analytics/cost/list](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/analytics/cost/list.md) [[Source](https://platform.claude.com/docs/en/api/admin/analytics/cost/list)]

* Adds "claude-in-slack" product value to both the `products` filter and `product` response field, with legacy-value note. [[line 108](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/analytics/cost/list.md?plain=1#L108)] [[Source](https://platform.claude.com/docs/en/api/admin/analytics/cost/list)]

#### [api/admin/analytics/cost/list_by_user](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/analytics/cost/list_by_user.md) [[Source](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user)]

* Adds "claude-in-slack" product value to `products` filter and `product` field, with legacy-value note. [[line 139](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/analytics/cost/list_by_user.md?plain=1#L139)] [[Source](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user)]

#### [api/admin/analytics/plugins/list](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/analytics/plugins/list.md) [[Source](https://platform.claude.com/docs/en/api/admin/analytics/plugins/list)]

* Same `order_by` semantics correction. [[line 60](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/analytics/plugins/list.md?plain=1#L60)] [[Source](https://platform.claude.com/docs/en/api/admin/analytics/plugins/list)]

#### [api/admin/analytics/skills](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/analytics/skills.md) [[Source](https://platform.claude.com/docs/en/api/admin/analytics/skills)]

* `attributed_list_price` and `estimated_overage_spend`: clarifies null conditions and documents that grouped/filtered cuts can sum to less than the ungrouped total when a member-skill pair has spend but no counted usage that day. [[line 109](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/analytics/skills.md?plain=1#L109)] [[Source](https://platform.claude.com/docs/en/api/admin/analytics/skills)]
* `enable_count`: removes the "temporarily unavailable" null condition, narrowing documented null cases. [[line 119](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/analytics/skills.md?plain=1#L119)] [[Source](https://platform.claude.com/docs/en/api/admin/analytics/skills)]

#### [api/admin/analytics/skills/list](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/analytics/skills/list.md) [[Source](https://platform.claude.com/docs/en/api/admin/analytics/skills/list)]

* Same `order_by` semantics correction, plus the same `attributed_list_price`/`estimated_overage_spend`/`enable_count` null-condition and cross-cut-sum clarifications as skills.md. [[lines 55, 163-175](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/analytics/skills/list.md?plain=1#L55)]

#### [api/admin/analytics/usage](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/analytics/usage.md) [[Source](https://platform.claude.com/docs/en/api/admin/analytics/usage)]

* Adds "claude-in-slack" product value to `product` field, with legacy-value note. [[line 77](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/analytics/usage.md?plain=1#L77)] [[Source](https://platform.claude.com/docs/en/api/admin/analytics/usage)]

#### [api/admin/analytics/usage/list](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/analytics/usage/list.md) [[Source](https://platform.claude.com/docs/en/api/admin/analytics/usage/list)]

* Adds "claude-in-slack" product value to `products` filter and `product` field, with legacy-value note. [[line 104](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/analytics/usage/list.md?plain=1#L104)] [[Source](https://platform.claude.com/docs/en/api/admin/analytics/usage/list)]

#### [api/admin/analytics/usage/list_by_user](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/analytics/usage/list_by_user.md) [[Source](https://platform.claude.com/docs/en/api/admin/analytics/usage/list_by_user)]

* Adds "claude-in-slack" product value to `products` filter and `product` field, with legacy-value note. [[line 139](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/analytics/usage/list_by_user.md?plain=1#L139)] [[Source](https://platform.claude.com/docs/en/api/admin/analytics/usage/list_by_user)]

#### [api/admin/analytics/users/list](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/analytics/users/list.md) [[Source](https://platform.claude.com/docs/en/api/admin/analytics/users/list)]

* Same `order_by` semantics correction. [[line 55](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/analytics/users/list.md?plain=1#L55)] [[Source](https://platform.claude.com/docs/en/api/admin/analytics/users/list)]

#### [api/admin/api_keys/list](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/api_keys/list.md) [[Source](https://platform.claude.com/docs/en/api/admin/api_keys/list)]

* Adds new `principal` field to the APIKey object, identifying the user or service account the key acts as. [[lines 101-113](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/api_keys/list.md?plain=1#L101-L113)] [[Source](https://platform.claude.com/docs/en/api/admin/api_keys/list)]

#### [api/admin/api_keys/retrieve](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/api_keys/retrieve.md) [[Source](https://platform.claude.com/docs/en/api/admin/api_keys/retrieve)]

* Adds new `principal` field to the APIKey object. [[lines 61-73](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/api_keys/retrieve.md?plain=1#L61-L73)] [[Source](https://platform.claude.com/docs/en/api/admin/api_keys/retrieve)]

#### [api/admin/api_keys/update](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/api_keys/update.md) [[Source](https://platform.claude.com/docs/en/api/admin/api_keys/update)]

* Adds new `principal` field to the APIKey object. [[lines 81-93](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/api_keys/update.md?plain=1#L81-L93)] [[Source](https://platform.claude.com/docs/en/api/admin/api_keys/update)]

#### [api/admin/external_keys](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/external_keys.md) [[Source](https://platform.claude.com/docs/en/api/admin/external_keys)]

* Clarifies external key config `id` can be an AWS KMS key ARN (not just a tagged `ekey_` ID) for Claude Platform on AWS organizations. [[line 47](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/external_keys.md?plain=1#L47)] [[Source](https://platform.claude.com/docs/en/api/admin/external_keys)]
* Clarifies `vault_uri` must be a Key Vault data-plane URI with expected domain formats. [[line 111](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/external_keys.md?plain=1#L111)] [[Source](https://platform.claude.com/docs/en/api/admin/external_keys)]

#### [api/admin/external_keys/create](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/external_keys/create.md) [[Source](https://platform.claude.com/docs/en/api/admin/external_keys/create)]

* Same `id`/AWS KMS ARN and `vault_uri` data-plane clarifications, plus a new description for the Azure object as "Azure Key Vault provider configuration". [[lines 55, 69, 87](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/external_keys/create.md?plain=1#L55)]

#### [api/admin/external_keys/list](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/external_keys/list.md) [[Source](https://platform.claude.com/docs/en/api/admin/external_keys/list)]

* Same `id`/AWS KMS ARN and `vault_uri` data-plane clarifications. [[lines 34, 98](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/external_keys/list.md?plain=1#L34)]

#### [api/admin/external_keys/retrieve](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/external_keys/retrieve.md) [[Source](https://platform.claude.com/docs/en/api/admin/external_keys/retrieve)]

* Same `id`/AWS KMS ARN and `vault_uri` data-plane clarifications. [[lines 23, 87](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/external_keys/retrieve.md?plain=1#L23)]

#### [api/admin/external_keys/update](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/external_keys/update.md) [[Source](https://platform.claude.com/docs/en/api/admin/external_keys/update)]

* Same `id`/AWS KMS ARN and `vault_uri` data-plane clarifications, plus new Azure object description. [[lines 73, 87, 97, 161](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/external_keys/update.md?plain=1#L73)]

#### [api/admin/invites](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/invites.md) [[Source](https://platform.claude.com/docs/en/api/admin/invites)]

* Invite object gains `accepted_at` and `rbac_group_ids` fields, and `role` gains new values "managed", "membership_admin", "owner", "primary_owner" (Claude Enterprise). [[lines 63-77](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/invites.md?plain=1#L63-L77)] [[Source](https://platform.claude.com/docs/en/api/admin/invites)]

#### [api/admin/invites/create](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/invites/create.md) [[Source](https://platform.claude.com/docs/en/api/admin/invites/create)]

* Notes the endpoint is beta for Claude Enterprise orgs, and documents seat-consumption behavior: invite auto-consumes from the lowest available seat tier, failing with 400 if none is free (no seat-tier parameter). [[lines 11-13](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/invites/create.md?plain=1#L11-L13)] [[Source](https://platform.claude.com/docs/en/api/admin/invites/create)]
* `role` now accepts "managed" in addition to prior values, with accepted values now dependent on organization type (Console/API vs. Claude Enterprise). [[lines 27-37](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/invites/create.md?plain=1#L27-L37)] [[Source](https://platform.claude.com/docs/en/api/admin/invites/create)]
* Adds new `rbac_group_ids` request field (beta, requires `write:rbac_groups` scope) and response `accepted_at`/`rbac_group_ids` fields. [[lines 43, 73, 147-173](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/invites/create.md?plain=1#L43)]

#### [api/admin/invites/delete](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/invites/delete.md) [[Source](https://platform.claude.com/docs/en/api/admin/invites/delete)]

* Notes the endpoint's availability is in beta for Claude Enterprise organizations. [[line 11](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/invites/delete.md?plain=1#L11)] [[Source](https://platform.claude.com/docs/en/api/admin/invites/delete)]

#### [api/admin/invites/list](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/invites/list.md) [[Source](https://platform.claude.com/docs/en/api/admin/invites/list)]

* Beta note for Claude Enterprise orgs; Invite object gains `accepted_at`, `rbac_group_ids`, and new `role` values (managed, membership_admin, owner, primary_owner). [[lines 11, 63, 81, 146-179](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/invites/list.md?plain=1#L11)]

#### [api/admin/invites/retrieve](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/invites/retrieve.md) [[Source](https://platform.claude.com/docs/en/api/admin/invites/retrieve)]

* Beta note for Claude Enterprise orgs; Invite object gains `accepted_at`, `rbac_group_ids`, and new `role` values. [[lines 11, 47, 65, 116-142](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/invites/retrieve.md?plain=1#L11)]

#### [api/admin/usage_report](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/usage_report.md) [[Source](https://platform.claude.com/docs/en/api/admin/usage_report)]

* Renames response schema types `UserActor`→`ClaudeCodeUserActor` and `APIActor`→`ClaudeCodeAPIActor`. [[lines 39, 49](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/usage_report.md?plain=1#L39)]

#### [api/admin/usage_report/retrieve_claude_code](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/usage_report/retrieve_claude_code.md) [[Source](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_claude_code)]

* Same schema type renames. [[lines 50, 60](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/usage_report/retrieve_claude_code.md?plain=1#L50)]

#### [api/admin/users](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/users.md) [[Source](https://platform.claude.com/docs/en/api/admin/users)]

* `role` gains new values "managed", "membership_admin", "owner", "primary_owner" (Claude Enterprise). [[lines 63-69](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/users.md?plain=1#L63-L69)] [[Source](https://platform.claude.com/docs/en/api/admin/users)]

#### [api/admin/users/delete](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/users/delete.md) [[Source](https://platform.claude.com/docs/en/api/admin/users/delete)]

* Notes the endpoint's availability is in beta for Claude Enterprise organizations. [[line 11](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/users/delete.md?plain=1#L11)] [[Source](https://platform.claude.com/docs/en/api/admin/users/delete)]

#### [api/admin/users/list](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/users/list.md) [[Source](https://platform.claude.com/docs/en/api/admin/users/list)]

* Beta note for Claude Enterprise orgs; `role` gains new values. [[lines 11, 77](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/users/list.md?plain=1#L11)]

#### [api/admin/users/retrieve](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/users/retrieve.md) [[Source](https://platform.claude.com/docs/en/api/admin/users/retrieve)]

* Beta note for Claude Enterprise orgs; `role` gains new values. [[lines 11, 57](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/users/retrieve.md?plain=1#L11)]

#### [api/admin/users/update](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/users/update.md) [[Source](https://platform.claude.com/docs/en/api/admin/users/update)]

* Beta note for Claude Enterprise orgs; request `role` now accepts "managed" with org-type-dependent accepted values; response `role` gains new enterprise values. [[lines 11, 27-37, 79](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/users/update.md?plain=1#L11)]

#### [api/admin/workspaces/archive](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/workspaces/archive.md) [[Source](https://platform.claude.com/docs/en/api/admin/workspaces/archive)]

* Clarifies `compartment_id`/CMEK behavior differs by cloud: manual KMS key-policy binding needed on AWS only; GCP and Azure enforce the compartment binding automatically. [[line 34](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/workspaces/archive.md?plain=1#L34)] [[Source](https://platform.claude.com/docs/en/api/admin/workspaces/archive)]

#### [api/admin/workspaces/create](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/workspaces/create.md) [[Source](https://platform.claude.com/docs/en/api/admin/workspaces/create)]

* Same CMEK/compartment behavior clarification by cloud provider. [[line 86](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/workspaces/create.md?plain=1#L86)] [[Source](https://platform.claude.com/docs/en/api/admin/workspaces/create)]

#### [api/admin/workspaces/list](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/workspaces/list.md) [[Source](https://platform.claude.com/docs/en/api/admin/workspaces/list)]

* Same CMEK/compartment behavior clarification. [[line 56](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/workspaces/list.md?plain=1#L56)] [[Source](https://platform.claude.com/docs/en/api/admin/workspaces/list)]

#### [api/admin/workspaces/retrieve](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/workspaces/retrieve.md) [[Source](https://platform.claude.com/docs/en/api/admin/workspaces/retrieve)]

* Same CMEK/compartment behavior clarification. [[line 36](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/workspaces/retrieve.md?plain=1#L36)] [[Source](https://platform.claude.com/docs/en/api/admin/workspaces/retrieve)]

#### [api/admin/workspaces/update](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/workspaces/update.md) [[Source](https://platform.claude.com/docs/en/api/admin/workspaces/update)]

* Same CMEK/compartment behavior clarification. [[line 76](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/api/admin/workspaces/update.md?plain=1#L76)] [[Source](https://platform.claude.com/docs/en/api/admin/workspaces/update)]

#### [build-with-claude/citations](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/build-with-claude/citations.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/citations)]

* Removes the Claude Haiku 3 exception, now stating that all active models support citations. [[line 13](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/build-with-claude/citations.md?plain=1#L13)] [[Source](https://platform.claude.com/docs/en/build-with-claude/citations)]

#### [build-with-claude/claude-in-amazon-bedrock](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/build-with-claude/claude-in-amazon-bedrock.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock)]

* Title now clarifies this Messages API integration supports Claude Opus 4.7 and later, with the older ARN-based integration (renamed from "legacy" to "Opus 4.6 and earlier") covering prior models. [[line 1](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/build-with-claude/claude-in-amazon-bedrock.md?plain=1#L1)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock)]

#### [build-with-claude/claude-on-amazon-bedrock-legacy](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/build-with-claude/claude-on-amazon-bedrock-legacy.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy)]

* Renamed from "(legacy)" to "(Opus 4.6 and earlier)", clarifying this integration's model support boundary versus the newer Claude in Amazon Bedrock integration. [[line 1](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/build-with-claude/claude-on-amazon-bedrock-legacy.md?plain=1#L1)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy)]

#### [build-with-claude/claude-on-vertex-ai](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/build-with-claude/claude-on-vertex-ai.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai)]

* Install instructions drop the `google-cloud-aiplatform` dependency, now only requiring `anthropic[vertex]`. [[line 49](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/build-with-claude/claude-on-vertex-ai.md?plain=1#L49)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai)]
* Regional endpoint example changes from `us-east1`/`claude-opus-4-8` to `us-east5`/`claude-sonnet-4-6`, with a new note that specific regional endpoints only support Claude Sonnet 4.6 and earlier — newer models require global or multi-region endpoints. [[lines 263-279](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/build-with-claude/claude-on-vertex-ai.md?plain=1#L263-L279)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai)]

#### [manage-claude/admin-api](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/manage-claude/admin-api.md) [[Source](https://platform.claude.com/docs/en/manage-claude/admin-api)]

* Documents that Claude Enterprise organizations can now use the Admin API (in beta) with a scoped claude.ai API key, limited to members/invites plus Enterprise-only group and custom-role read endpoints and spend limits. [[line 24](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/manage-claude/admin-api.md?plain=1#L24)] [[Source](https://platform.claude.com/docs/en/manage-claude/admin-api)]

#### [manage-claude/admin-api-keys](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/manage-claude/admin-api-keys.md) [[Source](https://platform.claude.com/docs/en/manage-claude/admin-api-keys)]

* Adds five new Claude Enterprise API key scopes for the new (beta) Admin API user-management endpoints: `read:members`, `write:members`, `read:rbac_groups`, `write:rbac_groups`, and a combined read-only `read:org_audit` scope covering user-management and Compliance API reads. [[lines 72-83](https://github.com/gpambrozio/ClaudeDocs/blob/07f074583747c34cd0d0915415b449247f23387d/docs-md/api/manage-claude/admin-api-keys.md?plain=1#L72-L83)] [[Source](https://platform.claude.com/docs/en/manage-claude/admin-api-keys)]
