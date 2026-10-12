# [Claude docs changes for October 12th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/22cb5b5c8449f14e0c6d98a60c07b2deacafddff) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/22cb5b5c8449f14e0c6d98a60c07b2deacafddff)]

## Executive Summary
- Claude Desktop admins get a documented recipe to turn off local sessions and distribute SSH connections via `disableDesktopLocalSessions`, `sshConfigs` and `sshHostAllowlist`.
- WorktreeCreate/WorktreeRemove hook docs now list every case that triggers them (`EnterWorktree`, `ExitWorktree`, workflows, `claude remote-control`) and the cleanup caveats.
- Scheduled task timing is rewritten: `*/5 * * * *` (what `/loop 5m` creates) is no longer delayed, and other delays are explained per schedule shape.
- Agent SDK adds a `run_id` on task messages to tell apart multiple runs of the same background task.
- The sandbox docs explain that commands like `FOO=bar npm test`, `make CC=clang` and `eval "ls"` still go through the permission flow, and which allow rules stop the prompts.

## New Claude Code versions

No new Claude Code versions were added today.

-----

## Claude Code changes

### Changed documents

#### [agent-sdk/typescript](https://github.com/gpambrozio/ClaudeDocs/blob/22cb5b5c8449f14e0c6d98a60c07b2deacafddff/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* New `runId` on the `task-notification` message origin, matching the run it belongs to, so a late notification can be attributed to the right run. [[line 2211](https://github.com/gpambrozio/ClaudeDocs/blob/22cb5b5c8449f14e0c6d98a60c07b2deacafddff/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L2211)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#task-notification-subkinds)]
* New optional `run_id` field on `SDKTaskStartedMessage` and `SDKTaskNotificationMessage`. It identifies one run of a task that runs again under the same `task_id` (such as a resumed subagent). Requires Agent SDK v0.3.292 or later. [[line 5212](https://github.com/gpambrozio/ClaudeDocs/blob/22cb5b5c8449f14e0c6d98a60c07b2deacafddff/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L5212)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#sdktasknotificationmessage)]

#### [debug-your-config](https://github.com/gpambrozio/ClaudeDocs/blob/22cb5b5c8449f14e0c6d98a60c07b2deacafddff/docs-md/claude-code/debug-your-config.md) [[Source](https://code.claude.com/docs/en/debug-your-config)]

* The "clean session" procedure is now step by step. It uses an empty working directory, a fresh `CLAUDE_CONFIG_DIR` and `--setting-sources user`, with separate Bash/Zsh and PowerShell instructions. [[lines 85-131](https://github.com/gpambrozio/ClaudeDocs/blob/22cb5b5c8449f14e0c6d98a60c07b2deacafddff/docs-md/claude-code/debug-your-config.md?plain=1#L85-L131)] [[Source](https://code.claude.com/docs/en/debug-your-config#test-against-a-clean-configuration)]
* Added guidance on what to do whether the problem disappears or persists in the clean session (copy config files back one at a time, or check `/status` for managed settings and env vars). [[line 131](https://github.com/gpambrozio/ClaudeDocs/blob/22cb5b5c8449f14e0c6d98a60c07b2deacafddff/docs-md/claude-code/debug-your-config.md?plain=1#L131)] [[Source](https://code.claude.com/docs/en/debug-your-config#test-against-a-clean-configuration)]

#### [desktop](https://github.com/gpambrozio/ClaudeDocs/blob/22cb5b5c8449f14e0c6d98a60c07b2deacafddff/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)]

* New section "Turn off local sessions and distribute SSH connections". It shows a managed-settings example combining `disableDesktopLocalSessions` (requires Desktop v1.37937.0+), `sshConfigs` and `sshHostAllowlist`. It also covers what the keys don't affect (CLI, Cowork, cloud sessions) and how to verify. [[line 810](https://github.com/gpambrozio/ClaudeDocs/blob/22cb5b5c8449f14e0c6d98a60c07b2deacafddff/docs-md/claude-code/desktop.md?plain=1#L810)] [[Source](https://code.claude.com/docs/en/desktop#turn-off-local-sessions-and-distribute-ssh-connections)]
* If `user@` is omitted from `sshHost`, Desktop uses the `User` from the developer's `~/.ssh/config`, or their local username. [[line 788](https://github.com/gpambrozio/ClaudeDocs/blob/22cb5b5c8449f14e0c6d98a60c07b2deacafddff/docs-md/claude-code/desktop.md?plain=1#L788)] [[Source](https://code.claude.com/docs/en/desktop#pre-configure-ssh-connections-for-your-team)]

#### [desktop-changelog](https://github.com/gpambrozio/ClaudeDocs/blob/22cb5b5c8449f14e0c6d98a60c07b2deacafddff/docs-md/claude-code/desktop-changelog.md) [[Source](https://code.claude.com/docs/en/desktop-changelog)]

* Updated with the same Desktop SSH and local-session administration content (see `desktop`).

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/22cb5b5c8449f14e0c6d98a60c07b2deacafddff/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* New `Login expired · Run /login to sign in again, or re-authenticate your Anthropic profile` message in the index. The Anthropic profile login-expired section is reorganized around how the profile was found (`ANTHROPIC_PROFILE` versus discovered with `user_oauth`). [[lines 1394-1410](https://github.com/gpambrozio/ClaudeDocs/blob/22cb5b5c8449f14e0c6d98a60c07b2deacafddff/docs-md/claude-code/errors.md?plain=1#L1394-L1410)] [[Source](https://code.claude.com/docs/en/errors#anthropic-profile-login-expired)]
* New steps for renaming a marketplace declared inline with `"source": "settings"` before removing it, so its settings entry isn't lost (Claude Code v2.1.292+). [[lines 3827-3832](https://github.com/gpambrozio/ClaudeDocs/blob/22cb5b5c8449f14e0c6d98a60c07b2deacafddff/docs-md/claude-code/errors.md?plain=1#L3827-L3832)] [[Source](https://code.claude.com/docs/en/errors#marketplace-is-registered-from-an-untrusted-source)]

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/22cb5b5c8449f14e0c6d98a60c07b2deacafddff/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* WorktreeCreate now lists all triggers: `--worktree`, `EnterWorktree`, subagent isolation, workflow agents, background sessions and `claude remote-control` in `worktree` mode. A `git worktree add` run through Bash does not trigger it; use a `PreToolUse` hook instead. [[line 3022](https://github.com/gpambrozio/ClaudeDocs/blob/22cb5b5c8449f14e0c6d98a60c07b2deacafddff/docs-md/claude-code/hooks.md?plain=1#L3022)] [[Source](https://code.claude.com/docs/en/hooks#worktreecreate)]
* WorktreeRemove also runs for `ExitWorktree` and `claude remote-control` cleanup. Worktrees created for subagents or workflow agents are kept, and `ExitWorktree` needs `discard_changes: true` to remove a hook-created worktree. [[lines 3096-3102](https://github.com/gpambrozio/ClaudeDocs/blob/22cb5b5c8449f14e0c6d98a60c07b2deacafddff/docs-md/claude-code/hooks.md?plain=1#L3096-L3102)] [[Source](https://code.claude.com/docs/en/hooks#worktreeremove)]
* Without a WorktreeRemove hook, behavior differs by route. Exit and `ExitWorktree` fall back to git, while `remote-control` keeps the worktree and prints `worktree removal failed, kept: <path>`. [[lines 3108-3112](https://github.com/gpambrozio/ClaudeDocs/blob/22cb5b5c8449f14e0c6d98a60c07b2deacafddff/docs-md/claude-code/hooks.md?plain=1#L3108-L3112)] [[Source](https://code.claude.com/docs/en/hooks#worktreeremove)]

#### [plugins/mods/reference](https://github.com/gpambrozio/ClaudeDocs/blob/22cb5b5c8449f14e0c6d98a60c07b2deacafddff/docs-md/claude-code/plugins/mods/reference.md) [[Source](https://code.claude.com/docs/en/plugins/mods/reference)]

* New `prompt.autocomplete` mod event. It fires when a word ends at the cursor, and the hook can return `{ suggestions }` rows shown below Claude Code's own. [[line 73](https://github.com/gpambrozio/ClaudeDocs/blob/22cb5b5c8449f14e0c6d98a60c07b2deacafddff/docs-md/claude-code/plugins/mods/reference.md?plain=1#L73)] [[Source](https://code.claude.com/docs/en/plugins/mods/reference#prompts-and-what-claude-reads)]

#### [permissions](https://github.com/gpambrozio/ClaudeDocs/blob/22cb5b5c8449f14e0c6d98a60c07b2deacafddff/docs-md/claude-code/permissions.md) [[Source](https://code.claude.com/docs/en/permissions)]

* Notes that some sandboxed commands still go through the regular permission flow, linking to auto-allow mode. [[line 661](https://github.com/gpambrozio/ClaudeDocs/blob/22cb5b5c8449f14e0c6d98a60c07b2deacafddff/docs-md/claude-code/permissions.md?plain=1#L661)] [[Source](https://code.claude.com/docs/en/permissions#how-permissions-interact-with-sandboxing)]

#### [sandboxing](https://github.com/gpambrozio/ClaudeDocs/blob/22cb5b5c8449f14e0c6d98a60c07b2deacafddff/docs-md/claude-code/sandboxing.md) [[Source](https://code.claude.com/docs/en/sandboxing)]

* Explains that commands like `FOO=bar npm test`, `make CC=clang` and `eval "ls"` still go through the permission flow even when sandboxed. It gives allow-rule patterns to stop recurring prompts, and notes that a matching allow rule also approves the unsandboxed retry. [[line 180](https://github.com/gpambrozio/ClaudeDocs/blob/22cb5b5c8449f14e0c6d98a60c07b2deacafddff/docs-md/claude-code/sandboxing.md?plain=1#L180)] [[Source](https://code.claude.com/docs/en/sandboxing#auto-allow-mode)]

#### [scheduled-tasks](https://github.com/gpambrozio/ClaudeDocs/blob/22cb5b5c8449f14e0c6d98a60c07b2deacafddff/docs-md/claude-code/scheduled-tasks.md) [[Source](https://code.claude.com/docs/en/scheduled-tasks)]

* Rewrote the run-time jitter explanation. Recurring tasks run late by up to half the gap to the next run (max 30 minutes), and unevenly spaced schedules can vary per run. [[line 168](https://github.com/gpambrozio/ClaudeDocs/blob/22cb5b5c8449f14e0c6d98a60c07b2deacafddff/docs-md/claude-code/scheduled-tasks.md?plain=1#L168)] [[Source](https://code.claude.com/docs/en/scheduled-tasks#how-late-a-recurring-task-runs)]
* `*/5 * * * *` (what `/loop 5m` creates) is not delayed. Each run starts 4m45s after the previous one so it lands inside the 5-minute prompt cache TTL. [[lines 168-178](https://github.com/gpambrozio/ClaudeDocs/blob/22cb5b5c8449f14e0c6d98a60c07b2deacafddff/docs-md/claude-code/scheduled-tasks.md?plain=1#L168-L178)] [[Source](https://code.claude.com/docs/en/scheduled-tasks#how-late-a-recurring-task-runs)]

#### [workflows](https://github.com/gpambrozio/ClaudeDocs/blob/22cb5b5c8449f14e0c6d98a60c07b2deacafddff/docs-md/claude-code/workflows.md) [[Source](https://code.claude.com/docs/en/workflows)]

* New "Which agents run again" section on resuming a stopped or paused run. Completed agents return cached results until one differs or fails, and then it and every later agent reruns. Stopping the whole run doesn't count as a failure, but stopping a single agent does. [[line 370](https://github.com/gpambrozio/ClaudeDocs/blob/22cb5b5c8449f14e0c6d98a60c07b2deacafddff/docs-md/claude-code/workflows.md?plain=1#L370)] [[Source](https://code.claude.com/docs/en/workflows#which-agents-run-again)]

-----

## API changes

### Changed documents

#### [api/go/* (Go SDK reference)](https://github.com/gpambrozio/ClaudeDocs/blob/22cb5b5c8449f14e0c6d98a60c07b2deacafddff/docs-md/api/api/go/messages.md) [[Source](https://platform.claude.com/docs/en/api/go/messages)]

* Large regenerated diffs across the Go SDK reference pages (`beta`, `beta/agents`, `beta/deployments`, `beta/environments`, `beta/messages`, `beta/sessions`, `beta/vaults`, `messages`, and subpages). These are mostly mechanical regeneration changes rather than new concepts.

#### [manage-claude/api-and-data-retention](https://github.com/gpambrozio/ClaudeDocs/blob/22cb5b5c8449f14e0c6d98a60c07b2deacafddff/docs-md/api/manage-claude/api-and-data-retention.md) [[Source](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention)]

* The feature eligibility table's Endpoint column is reformatted, for example `/v1/messages with \`bash\` tool` replaces the parenthesized form. The ZDR/HIPAA eligibility values are unchanged. [[lines 160-197](https://github.com/gpambrozio/ClaudeDocs/blob/22cb5b5c8449f14e0c6d98a60c07b2deacafddff/docs-md/api/manage-claude/api-and-data-retention.md?plain=1#L160-L197)] [[Source](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention#feature-eligibility)]

#### [managed-agents/budgets](https://github.com/gpambrozio/ClaudeDocs/blob/22cb5b5c8449f14e0c6d98a60c07b2deacafddff/docs-md/api/managed-agents/budgets.md) [[Source](https://platform.claude.com/docs/en/managed-agents/budgets)]

* Field names are now annotated per SDK language (Java/PHP camelCase, C#/Go PascalCase). Removing a budget is documented per SDK, such as `budget=None` in Python and `param.NullStruct` in Go, and the PHP example sends an explicit null as an extra body parameter. [[line 146](https://github.com/gpambrozio/ClaudeDocs/blob/22cb5b5c8449f14e0c6d98a60c07b2deacafddff/docs-md/api/managed-agents/budgets.md?plain=1#L146)] [[Source](https://platform.claude.com/docs/en/managed-agents/budgets#set-a-budget-at-session-creation)]

#### [managed-agents/scheduled-deployments](https://github.com/gpambrozio/ClaudeDocs/blob/22cb5b5c8449f14e0c6d98a60c07b2deacafddff/docs-md/api/managed-agents/scheduled-deployments.md) [[Source](https://platform.claude.com/docs/en/managed-agents/scheduled-deployments)]

* New examples for updating a deployment's budget (CLI `ant apply deployment.md` with front matter, plus SDK examples), and per-SDK field-name annotations for `schedule`, `expression`, `timezone` and `budget`. [[lines 263-395](https://github.com/gpambrozio/ClaudeDocs/blob/22cb5b5c8449f14e0c6d98a60c07b2deacafddff/docs-md/api/managed-agents/scheduled-deployments.md?plain=1#L263-L395)] [[Source](https://platform.claude.com/docs/en/managed-agents/scheduled-deployments#set-a-budget-on-each-run)]

#### Other Managed Agents pages

* Smaller updates, mostly per-SDK field-name annotations and example adjustments, across `agent-setup`, `define-outcomes`, `dreams`, `environments`, `events-and-streaming`, `files`, `github`, `mcp-connector`, `memory`, `migration`, `multiagent-orchestration`, `permission-policies`, `reference`, `sessions`, `session-threads`, `skills`, `tools-web-restrictions`, `vaults`, `webhooks` and `workflow-runs`.
