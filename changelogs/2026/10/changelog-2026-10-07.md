# [Claude docs changes for October 7th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/a02081b483dcd9c38388936525dc20d53fad5e41) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/a02081b483dcd9c38388936525dc20d53fad5e41)]

## Executive Summary
- Claude Code 2.1.292 adds an `effort` parameter to the Agent tool, `claude plugin install --marketplace`, and new mod hooks (`prompt.autocomplete`, prompt caching in `$.model.complete`), plus many security and permission fixes (UNC path reads, sandbox read-deny paths, tampered managed-settings cache)
- New Managed Agents page on restricting `web_search` and `web_fetch` domains per tool, with content caps and search localization
- Admin API moved out of beta: SDKs now use `client.organization` and the CLI uses `ant organization` instead of the `beta` namespace
- New "Map egress paths to managed controls and events" guide, a retention-sweep verification guide, and HIPAA-configuration notes for permission modes and gateways
- Compliance API documents two new errors for very large local session transcripts, and inference hooks docs add a detailed error table

## New Claude Code versions

### [2.1.292](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/versions/2.1.292.md)

#### New features

* Added `--marketplace <source>` to `claude plugin install`: adds the marketplace if needed (under the same policy checks as `marketplace add`), then installs the plugin
* Added an `effort` parameter to the Agent tool so Claude can run a sub-agent at a chosen effort level
* Added `CLAUDE_CODE_OVERLOADED_RETRY_BASE_DELAY_MS` to set a longer base backoff delay when retrying overloaded (529) requests
* Mods: added the `prompt.autocomplete` event, prompt caching for `$.model.complete` (`cache: true` on a block), and workflow agents in the `agent.spawn` hook
* Claude Tag: Edit button for the Allowed domains card; Code Review analytics now shows period totals and a per-repository breakdown

#### Existing feature improvements

* Faster startup of `claude -p` and SDK sessions: the first turn no longer waits for HTTP/SSE MCP servers to answer `resources/list`
* Much faster rendering of long bulleted or numbered replies
* Local (stdio) MCP servers now negotiate protocol version 2026-07-28 by default on every install (`MCP_PROTOCOL_NEGOTIATION=legacy` opts out); servers that are slow to connect are remembered for 7 days
* Hook output has `<system-reminder>` tags escaped; Grep accepts `file_path` for `path`, and Write, WebFetch and Read ignore stray parameters
* Sandbox auto-allow now runs interpreter commands with an env var prefix (`FOO=bar python3 app.py`) unprompted under strict sandbox mode
* Artifact tool lists up to 200 artifacts (was 50); scheduled and Run now routine runs publish private artifacts without approval
* Agent names are limited to 256 characters
* `claude plugin test` now fails on a failed `expect` or a refused stub answer instead of passing silently
* Ctrl+C draft recovery keeps a cleared prompt reachable with Up

#### Major bug fixes

* Security: PreToolUse hook approvals and auto mode no longer bypass the permission prompt for reads from network (UNC) paths
* Fixed sandboxed commands being able to read staged `/ultrareview` uploads, and managed sandbox read-deny paths that change mid-session not dropping project grants
* Fixed a tampered on-disk cache of server-managed settings being able to disable the built-in policy plugin, and notebook/PDF reads on macOS and Windows returning files outside what was approved
* Fixed subagents with `permissionMode: auto` entering auto mode when it is unavailable
* Fixed `NO_PROXY` being ignored for Claude Code's own API requests when `HTTPS_PROXY` is set
* Fixed an MCP tool name longer than 128 characters making every request fail
* Fixed plan mode not being restored on `claude --resume` / `/resume`, and scheduled tasks/`/loop` wakeups being lost after resume, crash or restart
* Fixed `claude -p` stopping background commands 5 seconds after the final result and dropping scheduled wakeups
* Fixed Read returning only the first entry for a PDF `pages` list like "6,9,15", and @-mentioned files over 256KB being silently left out
* Fixed multiple mod/plugin hook issues (denials after `next(e)`, `tool.check` allow skipping dialogs, hooks worker restarts bypassing permission hooks)

-----

## Claude Code changes

### Changed documents

#### [agent-sdk/hooks](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/claude-code/agent-sdk/hooks.md) [[Source](https://code.claude.com/docs/en/agent-sdk/hooks)]

* `WorktreeRemove` now fires only for a worktree that a `WorktreeCreate` hook created. [[line 167](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/claude-code/agent-sdk/hooks.md?plain=1#L167)] [[Source](https://code.claude.com/docs/en/agent-sdk/hooks#available-hooks)]

#### [agent-sdk/typescript](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* Example now wraps the claimed query loop in try/catch because a refused claim throws after yielding the error result. [[lines 157-165](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L157-L165)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#example)]
* `setMcpServers()` now only replaces the servers it manages (added through it and in-process SDK servers), with new rules for servers the call doesn't name. [[line 635](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L635)] [[lines 5028-5029](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L5028-L5029)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#methods)]
* `ReportFindings` `level` is now optional and not compared with the level the review ran at. [[lines 3432-3434](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L3432-L3434)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#reportfindings)]

#### [claude-apps-gateway-deploy](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/claude-code/claude-apps-gateway-deploy.md) [[Source](https://code.claude.com/docs/en/claude-apps-gateway-deploy)]

* New guidance that the gateway needs real PostgreSQL and `store.postgres_url` takes a single host (use a load balancer or managed endpoint for multi-node databases). [[lines 212-216](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/claude-code/claude-apps-gateway-deploy.md?plain=1#L212-L216)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-deploy#postgres)]
* New troubleshooting row for an unparseable `store.postgres_url`. [[line 348](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/claude-code/claude-apps-gateway-deploy.md?plain=1#L348)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-deploy#troubleshooting)]

#### [claude-directory](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/claude-code/claude-directory.md) [[Source](https://code.claude.com/docs/en/claude-directory)]

* Link to the new "Check the retention sweep" guide. [[line 1352](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/claude-code/claude-directory.md?plain=1#L1352)] [[Source](https://code.claude.com/docs/en/claude-directory#cleaned-up-automatically)]
* Purge command: success is indicated by the `Purged N item(s)` line, and `.heapsnapshot` files from `/heapdump` must be deleted separately. [[lines 1463-1465](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/claude-code/claude-directory.md?plain=1#L1463-L1465)] [[Source](https://code.claude.com/docs/en/claude-directory#clear-local-data)]
* `AGENTS.md` is read in place of a `CLAUDE.md` rather than alongside it. [[line 1217](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/claude-code/claude-directory.md?plain=1#L1217)] [[Source](https://code.claude.com/docs/en/claude-directory#database-connection-drops)]

#### [cli-reference](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* Added `claude daemon logs` and `claude daemon run` for the background-session supervisor. [[lines 28-29](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/claude-code/cli-reference.md?plain=1#L28-L29)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-commands)]

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* Added `CLAUDE_CODE_PLUGIN_DIR_WATCH` to control reloading of mods loaded with `--plugin-dir`. [[line 337](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/claude-code/env-vars.md?plain=1#L337)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB` notes: before v2.1.251 the scrub removed only `ANTHROPIC_API_KEY` and `AWS_SECRET_ACCESS_KEY`. [[lines 518-542](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/claude-code/env-vars.md?plain=1#L518-L542)] [[Source](https://code.claude.com/docs/en/env-vars#what-the-subprocess-environment-scrub-removes)]

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* Output-content-filter blocks that arrive before any text or tool call are now retried once. [[line 381](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/claude-code/errors.md?plain=1#L381)] [[Source](https://code.claude.com/docs/en/errors#automatic-retries)]
* New entry for `Cloud sessions need a claude.ai sign-in`. [[line 192](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/claude-code/errors.md?plain=1#L192)] [[Source](https://code.claude.com/docs/en/errors#find-your-error)]
* Image limit corrected: 3000 pixels when more than 20 images are in context. [[line 2161](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/claude-code/errors.md?plain=1#L2161)] [[Source](https://code.claude.com/docs/en/errors#image-was-too-large)]

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* `WorktreeRemove` clarified: fires only for worktrees created by a `WorktreeCreate` hook (no longer for subagent isolation). [[line 54](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/claude-code/hooks.md?plain=1#L54)] [[lines 2975-2978](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/claude-code/hooks.md?plain=1#L2975-L2978)] [[Source](https://code.claude.com/docs/en/hooks#hook-lifecycle)]

#### [keybindings](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/claude-code/keybindings.md) [[Source](https://code.claude.com/docs/en/keybindings)]

* Footer context: Ctrl+P/Ctrl+N added for up/down, and new `footer:close` (x) action stops or dismisses an agent or workflow row. [[lines 264-268](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/claude-code/keybindings.md?plain=1#L264-L268)] [[Source](https://code.claude.com/docs/en/keybindings#footer-actions)]

#### [llm-gateway-connect](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/claude-code/llm-gateway-connect.md) [[Source](https://code.claude.com/docs/en/llm-gateway-connect)]

* Desktop app SSH sessions are now available in beta with a gateway configuration (Desktop v1.40609.0+), controlled by an `sshHostAllowlist`; the gateway must not be at `localhost`. [[lines 179-186](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/claude-code/llm-gateway-connect.md?plain=1#L179-L186)] [[Source](https://code.claude.com/docs/en/llm-gateway-connect#desktop-app)]

#### [llm-gateway-rollout](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/claude-code/llm-gateway-rollout.md) [[Source](https://code.claude.com/docs/en/llm-gateway-rollout)]

* New section: gateway sessions aren't eligible for the HIPAA configuration; lists managed keys to restrict features and what they don't cover. [[lines 191-201](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/claude-code/llm-gateway-rollout.md?plain=1#L191-L201)] [[Source](https://code.claude.com/docs/en/llm-gateway-rollout#the-hipaa-configuration-behind-a-gateway)]

#### [managed-mcp](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/claude-code/managed-mcp.md) [[Source](https://code.claude.com/docs/en/managed-mcp)]

* URL patterns without a port now match only the default port (443/80) when the hostname has no `*`, and every port when it does; new examples for explicit ports and for `deniedMcpServers` entries. [[lines 296-318](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/claude-code/managed-mcp.md?plain=1#L296-L318)] [[line 484](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/claude-code/managed-mcp.md?plain=1#L484)] [[Source](https://code.claude.com/docs/en/managed-mcp#how-serverurl-entries-match)]

#### [monitoring-usage](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* New section "Map egress paths to managed controls and events", pairing each path (Bash, MCP, hooks, plugins, WebFetch, Artifact, Remote Control, transcript retention) with managed settings keys and telemetry events. [[lines 1476-1518](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/claude-code/monitoring-usage.md?plain=1#L1476-L1518)] [[Source](https://code.claude.com/docs/en/monitoring-usage#map-egress-paths-to-managed-controls-and-events)]
* New section "Check the retention sweep" explaining how to interpret the `retention_sweep` event. [[lines 1502-1520](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/claude-code/monitoring-usage.md?plain=1#L1502-L1520)] [[Source](https://code.claude.com/docs/en/monitoring-usage#check-the-retention-sweep)]
* `files_past_cutoff` also counts stale `skills/synced/` and `plugins/synced/` folders. [[line 1291](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/claude-code/monitoring-usage.md?plain=1#L1291)] [[Source](https://code.claude.com/docs/en/monitoring-usage#retention-sweep-event)]

#### [permission-modes](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/claude-code/permission-modes.md) [[Source](https://code.claude.com/docs/en/permission-modes)]

* With the HIPAA configuration applied, sessions start in default (Manual) mode instead of auto; auto mode and `bypassPermissions` remain available and can be disabled via managed settings (v2.1.285+). [[line 82](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/claude-code/permission-modes.md?plain=1#L82)] [[lines 121-135](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/claude-code/permission-modes.md?plain=1#L121-L135)] [[Source](https://code.claude.com/docs/en/permission-modes#common-setups)]

#### [plugins/mods/reference](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/claude-code/plugins/mods/reference.md) [[Source](https://code.claude.com/docs/en/plugins/mods/reference)]

* Added the `prompt.mention` event (v2.1.290+) to redirect or deny reading an @-mentioned file. [[line 67](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/claude-code/plugins/mods/reference.md?plain=1#L67)] [[Source](https://code.claude.com/docs/en/plugins/mods/reference#prompts-and-what-claude-reads)]
* New "Box border styles" table listing valid `borderStyle` names (an invalid name draws no border). [[lines 235-255](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/claude-code/plugins/mods/reference.md?plain=1#L235-L255)] [[Source](https://code.claude.com/docs/en/plugins/mods/reference#elements)]
* Text limits relaxed: `Code`/`Markdown` no longer capped at 10,000 characters; first 100,000 characters of text in one tree are drawn. [[lines 224-225](https://github.com/gpambrozo/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/claude-code/plugins/mods/reference.md?plain=1#L224-L225)] [[Source](https://code.claude.com/docs/en/plugins/mods/reference#elements)]
* `engine.create`: only mods outside the `user` tier can withhold a namespace. [[line 139](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/claude-code/plugins/mods/reference.md?plain=1#L139)] [[Source](https://code.claude.com/docs/en/plugins/mods/reference#other-mods)]

#### [quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/claude-code/quickstart.md) [[Source](https://code.claude.com/docs/en/quickstart)]

* Restructured: login merged into "Start your first session" (steps reduced from 8 to 7), added a list pointing to other pages for terminal beginners and other surfaces, removed the auto-mode default paragraph, and converted the "next steps" cards to a list. [[lines 1-20](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/claude-code/quickstart.md?plain=1#L1-L20)] [[lines 84-110](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/claude-code/quickstart.md?plain=1#L84-L110)] [[Source](https://code.claude.com/docs/en/quickstart#quickstart)]

#### [sandboxing](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/claude-code/sandboxing.md) [[Source](https://code.claude.com/docs/en/sandboxing)]

* Notes that background sessions sandbox Bash commands per their own settings, and how to wrap the whole process in the sandbox runtime. [[lines 959-960](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/claude-code/sandboxing.md?plain=1#L959-L960)] [[Source](https://code.claude.com/docs/en/sandboxing#scope)]

#### [self-hosted-environments-deploy](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/claude-code/self-hosted-environments-deploy.md) [[Source](https://code.claude.com/docs/en/self-hosted-environments-deploy)]

* Runner shutdown section rewritten into a three-step drain (wait, terminate process trees, post-session hook) with an itemized timing formula (80s at defaults) and `--retire-at` / `--defer-shutdown-max-min` guidance. [[lines 375-395](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/claude-code/self-hosted-environments-deploy.md?plain=1#L375-L395)] [[Source](https://code.claude.com/docs/en/self-hosted-environments-deploy#shutdown-timing)]
* Processes that outlive their shell command (such as daemonized services) are not signaled when a session stops. [[line 14](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/claude-code/self-hosted-environments-deploy.md?plain=1#L14)] [[Source](https://code.claude.com/docs/en/self-hosted-environments-deploy#harden-your-deployment)]

#### [sessions](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/claude-code/sessions.md) [[Source](https://code.claude.com/docs/en/sessions)]

* A conversation that ended in plan mode now resumes in plan mode from the picker and `/resume`. [[lines 76-84](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/claude-code/sessions.md?plain=1#L76-L84)] [[Source](https://code.claude.com/docs/en/sessions#permission-mode-on-resume)]
* Session picker: `k`/`j` navigate and `1`-`9` resume the session at that position. [[lines 176-182](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/claude-code/sessions.md?plain=1#L176-L182)] [[Source](https://code.claude.com/docs/en/sessions#use-the-session-picker)]

#### [sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* Subagent `name` limited to 256 characters; longer names are skipped. [[lines 285](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/claude-code/sub-agents.md?plain=1#L285)] [[line 321](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/claude-code/sub-agents.md?plain=1#L321)] [[Source](https://code.claude.com/docs/en/sub-agents#write-subagent-files)]
* Subagent `effort` doesn't override `CLAUDE_CODE_EFFORT_LEVEL`. [[line 298](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/claude-code/sub-agents.md?plain=1#L298)] [[Source](https://code.claude.com/docs/en/sub-agents#write-subagent-files)]

#### [worktrees](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/claude-code/worktrees.md) [[Source](https://code.claude.com/docs/en/worktrees)]

* Worktree safety checks don't track files written by shell commands such as `cp`. [[line 83](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/claude-code/worktrees.md?plain=1#L83)] [[Source](https://code.claude.com/docs/en/worktrees#how-claude-code-enforces-isolation)]

-----

## API changes

### New Documents

#### [managed-agents/tools-web-restrictions](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/api/managed-agents/tools-web-restrictions.md) [[Source](https://platform.claude.com/docs/en/managed-agents/tools-web-restrictions)]

New Managed Agents (beta) page, split out of the tools page, describing how to restrict `web_search` and `web_fetch` per tool with `allowed_domains` or `blocked_domains` on the agent toolset's `configs` entries. It covers `max_content_tokens`, `user_location`, how `limited` environment networking also applies, changing the lists mid-session, and examples in multiple languages.

### Changed documents

#### [api/*/beta (SDK reference for Python, TypeScript, Go, Java, Ruby, PHP, C#, CLI)](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/api/api/python/beta.md) [[Source](https://platform.claude.com/docs/en/api/python/beta)]

* Parameter docs across beta, sessions, memory stores, vaults, environments and messages now label each parameter as a query, header, path or body parameter instead of prefixing the description (mechanical reformat).

#### [manage-claude/admin-api](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/api/manage-claude/admin-api.md) [[Source](https://platform.claude.com/docs/en/manage-claude/admin-api)]

* Admin API is no longer under beta: SDKs use `client.organization` (was `client.beta.organization`) and the CLI uses `ant organization` (was `ant beta:organization`); reference links updated. The same change appears in wif-admin-api, workspaces, rate-limits-api, user-management and the CMEK guides. [[line 29](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/api/manage-claude/admin-api.md?plain=1#L29)] [[Source](https://platform.claude.com/docs/en/manage-claude/admin-api#authentication)]

#### [manage-claude/compliance-errors](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/api/manage-claude/compliance-errors.md) [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-errors)]

* New 400 error `transcript_page_read_limit_exceeded` ("Transcript page too large") for local session messages, with guidance to read oldest first and use a 5-minute timeout. [[lines 131-150](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/api/manage-claude/compliance-errors.md?plain=1#L131-L150)] [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-errors#transcript-page-too-large)]
* New 429 error `transcript_read_server_busy` (not a rate limit): wait for `retry-after` and resend unchanged. [[lines 450-463](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/api/manage-claude/compliance-errors.md?plain=1#L450-L463)] [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-errors#server-busy-reading-large-transcripts)]

#### [manage-claude/inference-hooks-configuration](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/api/manage-claude/inference-hooks-configuration.md) [[Source](https://platform.claude.com/docs/en/manage-claude/inference-hooks-configuration)]

* Endpoint URLs that are private IPs, IPv6 addresses or `localhost` are rejected. [[line 60](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/api/manage-claude/inference-hooks-configuration.md?plain=1#L60)] [[Source](https://platform.claude.com/docs/en/manage-claude/inference-hooks-configuration#set-up-inference-hooks)]
* "Validate tool calls" is on by default in new configurations. [[line 92](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/api/manage-claude/inference-hooks-configuration.md?plain=1#L92)] [[Source](https://platform.claude.com/docs/en/manage-claude/inference-hooks-configuration#set-up-inference-hooks)]
* New table of "Recent errors" types (`DlpWebhookTimeoutError`, `...StatusError`, `...RelayError`, etc.) with `webhook_error` / `relay_error` categories. [[lines 118-132](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/api/manage-claude/inference-hooks-configuration.md?plain=1#L118-L132)] [[Source](https://platform.claude.com/docs/en/manage-claude/inference-hooks-configuration#monitor-your-ai-security-server)]

#### [manage-claude/inference-hooks-endpoint](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/api/manage-claude/inference-hooks-endpoint.md) [[Source](https://platform.claude.com/docs/en/manage-claude/inference-hooks-endpoint)]

* Tools on local MCP servers connected directly by Claude Code are client tools named `mcp__<server>__<tool>`; denies stop the call before it runs. [[lines 310-313](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/api/manage-claude/inference-hooks-endpoint.md?plain=1#L310-L313)] [[Source](https://platform.claude.com/docs/en/manage-claude/inference-hooks-endpoint#client-tools)]
* A third-party tool's `origin` can be a private or local address; clients should tolerate new message `role` values. [[line 283](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/api/manage-claude/inference-hooks-endpoint.md?plain=1#L283)] [[line 800](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/api/manage-claude/inference-hooks-endpoint.md?plain=1#L800)] [[Source](https://platform.claude.com/docs/en/manage-claude/inference-hooks-endpoint#third-party-tools)]

#### [managed-agents/environments](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/api/managed-agents/environments.md) [[Source](https://platform.claude.com/docs/en/managed-agents/environments)]

* With `limited` networking, `allowed_hosts` now also applies to `web_search` and `web_fetch`; a bare hostname matches only that exact host. [[lines 407-409](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/api/managed-agents/environments.md?plain=1#L407-L409)] [[line 578](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/api/managed-agents/environments.md?plain=1#L578)] [[Source](https://platform.claude.com/docs/en/managed-agents/environments#networking)]

#### [managed-agents/tools](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/api/managed-agents/tools.md) [[Source](https://platform.claude.com/docs/en/managed-agents/tools)]

* Web search/fetch restriction content (about 400 lines) moved to the new tools-web-restrictions page, leaving a pointer. [[line 235](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/api/managed-agents/tools.md?plain=1#L235)] [[Source](https://platform.claude.com/docs/en/managed-agents/tools#restricting-web-search-and-web-fetch)]

#### [build-with-claude/effort](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/api/build-with-claude/effort.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/effort)]

* Per-message effort (beta) now lists supported models on the Claude API and Google Cloud (Fable 5.1, Mythos 5.1, Opus 5.5, Opus 5, Sonnet 5.5), notes it is unavailable for Opus 5 on Amazon Bedrock, and describes the 400 error without the beta header. [[line 278](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/api/build-with-claude/effort.md?plain=1#L278)] [[lines 365-367](https://github.com/gpambrozio/ClaudeDocs/blob/a02081b483dcd9c38388936525dc20d53fad5e41/docs-md/api/build-with-claude/effort.md?plain=1#L365-L367)] [[Source](https://platform.claude.com/docs/en/build-with-claude/effort#recommended-effort-levels-for-claude-opus-5)]
