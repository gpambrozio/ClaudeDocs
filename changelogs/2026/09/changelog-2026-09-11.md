# [Claude docs changes for September 11th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5)]

## Executive Summary
- Plugin changes made in the `/plugin` menu now apply when you close it — Claude Code runs `/reload-plugins` for you, so installing, enabling, disabling and uninstalling no longer leave the session stale. This rewording lands across a dozen pages
- Task-tracking tool availability is now stated as an allowlist rather than a denylist: `TaskCreate`/`TaskGet`/`TaskUpdate`/`TaskList`/`TodoWrite` ship by default only on Claude 3.x, Opus 4–4.7, Sonnet 4–4.6 and Haiku 4.5. Every other model, **including a model ID Claude Code doesn't recognize**, needs an opt-in
- `WorktreeRemove` hooks gain decision control for the first time: a non-zero exit now fails worktree removal, and a refused session delete can be forced through with `claude rm <id> --force-remove-worktree <worktree-id>`
- The Claude apps gateway can now push its contracted `pricing` rates to signed-in clients as the `modelPricing` managed setting, and a managed policy can send session telemetry straight to your own collector instead of through the gateway relay
- Auto mode denials now name the classifier rule that matched, in square brackets (`[Data Exfiltration]`, `[Production Deploy]`), in place of the fixed `Blocked by classifier` text

## New Claude Code versions

### [2.1.268](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/versions/2.1.268.md)

#### New features

* Added `pricing:` delivery to signed-in clients through managed settings, so `/cost` and telemetry match the Claude apps gateway spend meter
* Added the `gatewayInternalNetworks` managed setting, letting administrators allow `/login` to a gateway on their organization's own public IPv4 block
* Added a gateway startup warning when `access_control.allow_cidrs` is empty, plus a one-time warning on the first request from a public address
* Added `claude self-hosted-runner --remove-session-state` to delete per-session directories under `<base-dir>/_sessions/` when a session ends
* Added `--json` to `claude plugin install`, `uninstall`, `update`, `enable` and `disable`, and `errorDetails`/`noteDetails` to `claude plugin list --json` rows
* Added `configDirectory` to `claude auth status --json`
* Added browser-tab icons for published artifacts, chosen by Claude to match each page

#### Existing feature improvements

* Improved `/plugin`: installing, enabling or disabling a plugin now takes effect when you close the menu, so `/reload-plugins` is no longer needed afterwards
* Improved `--continue` / `--resume`: the conversation appears immediately instead of waiting for SessionStart hooks, and the first message no longer re-reads the whole transcript
* Improved fullscreen mode so adding or removing a prompt line repaints as fast as typing a character
* Improved auto mode denials: the message Claude receives names the blocking rule and asks it to try a safer method and finish unrelated work before stopping to ask
* Improved startup time in projects with `.claude/workflows/` scripts by no longer parsing each script to list them
* Changed the task-tracking tools to be offered only on Claude 3.x, Opus 4.0–4.7, Sonnet 4.0–4.6 and Haiku 4.5; set `CLAUDE_CODE_ENABLE_TODO_TOOLS=1` elsewhere
* Changed Bedrock, Vertex and Foundry sessions to deliver environment and settings details as attachments and to keep the tool list byte-stable, matching first-party sessions
* Changed plain `WebFetch` deny and ask rules to stop applying to Artifact tool reads and updates; use an `Artifact` rule instead

#### Major bug fixes

* Fixed every turn failing with HTTP 400 on third-party Anthropic-compatible endpoints since 2.1.265, caused by a regex in the Artifact tool's input schema
* Fixed WebFetch hanging indefinitely on a server that never finishes the response; fetches now fail after 300 seconds, tunable with `CLAUDE_CODE_WEBFETCH_DEADLINE_MS`
* Fixed sustained high CPU usage from a busy loop in long-running idle sessions and from rapid terminal focus reports during a session recap
* Fixed deny and ask permission rules not applying on symlinked directories (`/etc`, `/tmp`, `/var` on macOS; `/bin` on Linux) when a path was given by its real location
* Fixed a Read or Edit deny rule not applying when an `env -C`, `eval` or similar unanalyzable command shared the line
* Fixed plugin, marketplace, `/mcp`, `/plugin` and `claude mcp` output leaking tokens, passwords and `${VAR}`-resolved secrets
* Fixed prompt caching and extended thinking breaking mid-session for SDK sessions using `excludeDynamicSections`
* Fixed a running session silently switching to the organization's default model when another Claude Code process refreshed a stale model-access entry
* Fixed workload identity federation via a profile failing mid-run with `401 … jti reused`
* Fixed `/compact` mangling text containing `$` sequences, and fixed SDK prompt suggestions and `/rename` sending the pre-compaction conversation
* Fixed a respawned in-process teammate picking up tools or a system prompt from a same-named agent file in an untrusted folder
* Fixed `PermissionRequest` hooks not firing in `--print` mode, and policy-helper warnings not printing on headless runs

-----

## Claude Code changes

### Changed documents

#### [advisor](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/advisor.md) [[Source](https://code.claude.com/docs/en/advisor)]

* Dropped the separate Fable 5 minimum version; both Fable models are now described as simply requiring Fable access, with only Fable 5.1's v2.1.257 floor called out. [[line 91](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/advisor.md?plain=1#L91)] [[Source](https://code.claude.com/docs/en/advisor#choose-an-advisor-model)]

#### [agent-sdk/modifying-system-prompts](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/agent-sdk/modifying-system-prompts.md) [[Source](https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts)]

* System-prompt recording now applies on Bedrock, Google Cloud's Agent Platform and Foundry too. The old carve-out for sessions that don't fetch feature flags is now written as history: before v2.1.268 those sessions rebuilt the prompt every request and `snapshot` had no effect. [[line 346](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/agent-sdk/modifying-system-prompts.md?plain=1#L346)] [[Source](https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts#change-the-prompt-of-an-existing-session)]

#### [agent-sdk/python](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/agent-sdk/python.md) [[Source](https://code.claude.com/docs/en/agent-sdk/python)]

* Task-tool availability restated as an allowlist — Claude 3.x, Opus 4–4.7, Sonnet 4–4.6, Haiku 4.5 — with every other model, including unrecognized model IDs, requiring an opt-in. Applies from Claude Code v2.1.268 (TypeScript SDK v0.3.268). [[line 2820](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/agent-sdk/python.md?plain=1#L2820)] [[Source](https://code.claude.com/docs/en/agent-sdk/python#todowrite)]

#### [agent-sdk/todo-tracking](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/agent-sdk/todo-tracking.md) [[Source](https://code.claude.com/docs/en/agent-sdk/todo-tracking)]

* Same allowlist rewrite, with the page's opening paragraph inverted to lead with where the tools *are* provided rather than where they're withheld. [[lines 5-23](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/agent-sdk/todo-tracking.md?plain=1#L5-L23)] [[Source](https://code.claude.com/docs/en/agent-sdk/todo-tracking#track-todos)]

#### [agent-sdk/typescript](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* `pending_permission_requests` is now always present on a successful `initialize` response and empty when nothing is pending, rather than optional. Earlier versions could omit it, so hand-rolled wire-protocol parsers should read a missing field as an older CLI, not as proof nothing is pending. Requires v2.1.268. [[lines 659-663](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L659-L663)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#sdkcontrolinitializeresponse)]
* The Artifact tool's `favicon` is now described as marking the artifact in the user's gallery rather than as the browser-tab icon. [[line 3103](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L3103)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#artifact)]
* Task-tool availability rewritten to the same allowlist form in both places the page states it. [[line 2786](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L2786)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#todowrite)]

#### [agent-teams](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/agent-teams.md) [[Source](https://code.claude.com/docs/en/agent-teams)]

* A named Agent call no longer launches a teammate when the call is a fork or passes `isolation` itself — the two exceptions to teams forming automatically. [[lines 213-215](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/agent-teams.md?plain=1#L213-L215)] [[Source](https://code.claude.com/docs/en/agent-teams#how-claude-starts-agent-teams)]
* Teammates inherit the lead's permission mode **except `dontAsk` mode**, which is now explicitly not inherited. [[line 269](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/agent-teams.md?plain=1#L269)] [[Source](https://code.claude.com/docs/en/agent-teams#permissions)]
* Teammate subagent scopes narrowed from "project, user, plugin, or CLI-defined" to "project, user, or managed". [[line 251](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/agent-teams.md?plain=1#L251)] [[Source](https://code.claude.com/docs/en/agent-teams#use-subagent-definitions-for-teammates)]

#### [agent-view](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/agent-view.md) [[Source](https://code.claude.com/docs/en/agent-view)]

* New guidance for a session delete refused because git or a `WorktreeRemove` hook couldn't remove the worktree: the message now names the cause, reports how the hook ended (`exited 1`) and quotes the start of its stderr. Pressing `Ctrl+X` twice, or passing `--force-remove-worktree`, deletes the directory anyway — but only when Claude Code can confirm it's a linked worktree under `.claude/worktrees/` with no uncommitted tracked changes, no nested repository and no other session claiming it. [[lines 542-546](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/agent-view.md?plain=1#L542-L546)] [[Source](https://code.claude.com/docs/en/agent-view#what-deleting-a-session-removes)]
* `claude rm <id> --force-remove-worktree <worktree-id>` added to the shell command table, requiring v2.1.268. [[line 691](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/agent-view.md?plain=1#L691)] [[Source](https://code.claude.com/docs/en/agent-view#manage-sessions-from-the-shell)]
* Version history gained a v2.1.268 row describing what the refusal used to show: only `worktree could not be removed (WorktreeRemove hook failed)` or git's error, with the hook's stderr going to the debug log alone. [[line 928](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/agent-view.md?plain=1#L928)] [[Source](https://code.claude.com/docs/en/agent-view#version-history)]

#### [agents](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/agents.md) [[Source](https://code.claude.com/docs/en/agents)]

* Clarified that a dispatched session moves into its own worktree *before it edits files*, rather than at dispatch. [[line 18](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/agents.md?plain=1#L18)] [[Source](https://code.claude.com/docs/en/agents#run-agents-in-parallel)]

#### [amazon-bedrock](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/amazon-bedrock.md) [[Source](https://code.claude.com/docs/en/amazon-bedrock)]

* Dropped the v2.1.171-and-earlier caveats around `AWS_REGION` resolution; reading the AWS config files is now simply how it works. [[lines 234-245](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/amazon-bedrock.md?plain=1#L234-L245)] [[Source](https://code.claude.com/docs/en/amazon-bedrock#3-configure-claude-code)]

#### [analytics](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/analytics.md) [[Source](https://code.claude.com/docs/en/analytics)]

* Removed the "Tagging criteria" section that explained how PRs are counted as "with Claude Code".

#### [artifacts](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/artifacts.md) [[Source](https://code.claude.com/docs/en/artifacts)]

* Claude now picks a browser-tab icon matching what the page is, such as a chart or a calendar, separately from the artifact's title and emoji — and you can ask for a specific one. [[line 53](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/artifacts.md?plain=1#L53)] [[Source](https://code.claude.com/docs/en/artifacts#create-an-artifact)]
* The "no backend" limits were trimmed: the claim that an artifact can't store form input and that MCP connectors are its only route to outside data has been dropped from both the intro and the constraints table. [[lines 26-277](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/artifacts.md?plain=1#L26-L277)] [[Source](https://code.claude.com/docs/en/artifacts#what-an-artifact-is-not)]

#### [auto-mode-config](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/auto-mode-config.md) [[Source](https://code.claude.com/docs/en/auto-mode-config)]

* Denial reasons now name the matched rule in square brackets — `[Data Exfiltration]`, `[Production Deploy]` — replacing the description of a fixed `Blocked by classifier` string produced by an internal severity scale. [[lines 366-376](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/auto-mode-config.md?plain=1#L366-L376)] [[Source](https://code.claude.com/docs/en/auto-mode-config#fix-a-denial-with-an-allow-rule-an-environment-entry-or-a-retry)]

#### [best-practices](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/best-practices.md) [[Source](https://code.claude.com/docs/en/best-practices)]

* Checkpoints are now created by "every prompt you send **that starts a turn**", not every prompt. [[line 370](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/best-practices.md?plain=1#L370)] [[Source](https://code.claude.com/docs/en/best-practices#rewind-with-checkpoints)]

#### [channels-reference](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/channels-reference.md) [[Source](https://code.claude.com/docs/en/channels-reference)]

* Getting a failed channel server's stderr trace now requires restarting with `claude --debug --dangerously-load-development-channels server:webhook`, not just reading the debug log. [[line 161](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/channels-reference.md?plain=1#L161)] [[Source](https://code.claude.com/docs/en/channels-reference#example-build-a-webhook-receiver)]

#### [channels](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/channels.md) [[Source](https://code.claude.com/docs/en/channels)]

* Both install walkthroughs now point at "Apply plugin changes without restarting" instead of telling you to run `/reload-plugins`. [[lines 42-118](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/channels.md?plain=1#L42-L118)] [[Source](https://code.claude.com/docs/en/channels#supported-channels)]

#### [checkpointing](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/checkpointing.md) [[Source](https://code.claude.com/docs/en/checkpointing)]

* New section "Messages sent mid-turn not checkpointed": a message you queue while Claude works joins the running turn, so it gets no checkpoint and never appears in the rewind menu. To undo it, rewind to the prompt that started the turn — which discards the work Claude did before your message arrived too. [[lines 85-89](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/checkpointing.md?plain=1#L85-L89)] [[Source](https://code.claude.com/docs/en/checkpointing#messages-sent-mid-turn-not-checkpointed)]

#### [claude-apps-gateway-config](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/claude-apps-gateway-config.md) [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config)]

* New "Send the rates to signed-in clients" section: with v2.1.268 on the gateway server, `pricing` is injected into served `managed` policies as the [`modelPricing`](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/settings-reference.md) setting, so matched developers see contracted rates in `/usage`, the status line and OpenTelemetry. A policy opts out with `modelPricing: {}`, and one that sets its own `modelPricing` is left whole. [[lines 467-473](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/claude-apps-gateway-config.md?plain=1#L467-L473)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config#send-the-rates-to-signed-in-clients)]
* New "Export directly to your collector" section: setting `OTEL_EXPORTER_OTLP_ENDPOINT` in a managed policy's `env` block sends telemetry straight to your collector, bypassing the relay, subject to five checks — the endpoint must come from the gateway itself, use `https://` (or loopback `http://`), resolve to a `/v1/<signal>` path, not be the gateway's own host, and no `otelHeadersHelper` may be configured anywhere. Requires v2.1.265 on each client. [[lines 772-796](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/claude-apps-gateway-config.md?plain=1#L772-L796)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config#export-directly-to-your-collector)]
* New "When a destination fails" section: the gateway never buffers or retries telemetry, pauses a destination in 30-second stretches after five consecutive failures, and treats `400`/`413`/`415`/`422`/`431` as refused payloads that neither advance nor reset the failure count. [[lines 797-803](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/claude-apps-gateway-config.md?plain=1#L797-L803)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config#when-a-destination-fails)]
* With `forward_user_identity: true`, a `429` answering a request that carried the developer's email no longer fails over — it's a per-user denial, so your proxy's per-user budget holds. Before v2.1.267 every `429` failed over. [[lines 121-207](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/claude-apps-gateway-config.md?plain=1#L121-L207)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config#upstreams)]
* `pricing` now also works with a `managed:` block, not just `admin:`, and override rates gained an upper bound of 10000. [[lines 438-455](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/claude-apps-gateway-config.md?plain=1#L438-L455)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config#pricing)]
* Desktop and Cowork sessions now stamp telemetry with `user.email` and `user.groups`; an over-long or comma-bearing group list is omitted rather than truncated. Requires v2.1.265 on the gateway and Claude Desktop 1.24012. [[lines 711-717](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/claude-apps-gateway-config.md?plain=1#L711-L717)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config#telemetry)]
* The three pushed `OTEL_*_EXPORTER` selectors are now set per-signal to `otlp` or `none` based on whether a `forward_to` destination enables that signal; before v2.1.265 all three were pushed as `otlp`. [[lines 751-755](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/claude-apps-gateway-config.md?plain=1#L751-L755)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config#telemetry)]

#### [claude-apps-gateway](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/claude-apps-gateway.md) [[Source](https://code.claude.com/docs/en/claude-apps-gateway)]

* The telemetry-destination entry was broken into sub-bullets and now allows a policy to name your own collector as the endpoint. [[lines 378-381](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/claude-apps-gateway.md?plain=1#L378-L381)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway#ci-pipelines-and-remote-machines)]

#### [claude-code-on-the-web](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/claude-code-on-the-web.md) [[Source](https://code.claude.com/docs/en/claude-code-on-the-web)]

* The network-access bullet gained a `default-allowed-domains` anchor and now links out to the access levels, default allowed domains, and the traffic that bypasses the allowlist. [[line 287](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L287)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#security-and-isolation)]

#### [claude-md](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/claude-md.md) [[Source](https://code.claude.com/docs/en/claude-md)]

* A `.claude/rules/` symlink pointing outside the working directory is now treated as an external import: the rules don't load until you approve external imports, and then only those without a `paths` field. Because that approval is only ever requested for an `@path` import, shared rules are better kept in `~/.claude/rules/`. [[lines 240-242](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/claude-md.md?plain=1#L240-L242)] [[Source](https://code.claude.com/docs/en/claude-md#share-rules-across-projects-with-symlinks)]

#### [claude-security](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/claude-security.md) [[Source](https://code.claude.com/docs/en/claude-security)]

* Replaced the literal `/reload-plugins` code block with a pointer to "Apply plugin changes without restarting". [[line 35](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/claude-security.md?plain=1#L35)] [[Source](https://code.claude.com/docs/en/claude-security#install-the-plugin)]

#### [cli-reference](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* `claude rm` rewritten around the two flags a refusal can print: `--discard-unpushed <commit>@<worktree-id>` (v2.1.260) for unpushed commits, and the new `--force-remove-worktree <worktree-id>` (v2.1.268) for a worktree git or the hook couldn't remove. [[line 40](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/cli-reference.md?plain=1#L40)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-commands)]
* `--system-prompt-snapshot` now takes effect on Bedrock, Agent Platform and Foundry; the feature-flag carve-out is recast as pre-v2.1.268 history. [[line 158](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/cli-reference.md?plain=1#L158)] [[Source](https://code.claude.com/docs/en/cli-reference#system-prompt-flags-in-resumed-conversations)]

#### [cloud-environments](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/cloud-environments.md) [[Source](https://code.claude.com/docs/en/cloud-environments)]

* Environments can now be managed from the Desktop app's prompt box, not only at claude.ai/code. [[line 35](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/cloud-environments.md?plain=1#L35)] [[Source](https://code.claude.com/docs/en/cloud-environments#configure-your-environment)]

#### [desktop](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)]

* Cloud environment management documented as a dropdown in the prompt box, with **Add cloud environment** to create one and a hover gear icon to edit or archive your own. [[lines 630-635](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/desktop.md?plain=1#L630-L635)] [[Source](https://code.claude.com/docs/en/desktop#cloud-sessions)]

#### [desktop-changelog](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/desktop-changelog.md) [[Source](https://code.claude.com/docs/en/desktop-changelog)]

* Same cloud-environment dropdown rewrite as the Desktop page. [[lines 630-635](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/desktop-changelog.md?plain=1#L630-L635)] [[Source](https://code.claude.com/docs/en/desktop-changelog#cloud-sessions)]

#### [desktop-scheduled-tasks](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/desktop-scheduled-tasks.md) [[Source](https://code.claude.com/docs/en/desktop-scheduled-tasks)]

* The comparison table's `/loop` persistence cell changed from "Restored on `--resume` if unexpired" to "Restored on `--resume`, with exceptions", linking to the new limitations. [[line 18](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/desktop-scheduled-tasks.md?plain=1#L18)] [[Source](https://code.claude.com/docs/en/desktop-scheduled-tasks#compare-scheduling-options)]

#### [discover-plugins](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/discover-plugins.md) [[Source](https://code.claude.com/docs/en/discover-plugins)]

* Closing the `/plugin` menu now triggers `/reload-plugins` automatically for installs, enables, disables and uninstalls; if the reload would invalidate the prompt cache it warns and leaves the changes pending for `/reload-plugins --force`. If Claude is still responding, the reload waits. [[line 386](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/discover-plugins.md?plain=1#L386)] [[Source](https://code.claude.com/docs/en/discover-plugins#apply-plugin-changes-without-restarting)]
* New list of the plugin changes that still need a manual `/reload-plugins`: a `claude plugin` command run in another terminal, edits to a `--plugin-dir` plugin, an auto-update that asks for a reload, and a held `--plugin-dir` change. [[lines 388-393](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/discover-plugins.md?plain=1#L388-L393)] [[Source](https://code.claude.com/docs/en/discover-plugins#apply-plugin-changes-without-restarting)]
* Records that before v2.1.268, menu changes and non-activating installs stayed pending until you ran `/reload-plugins` yourself. [[line 395](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/discover-plugins.md?plain=1#L395)] [[Source](https://code.claude.com/docs/en/discover-plugins#apply-plugin-changes-without-restarting)]

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* Added `CLAUDE_CODE_WEBFETCH_DEADLINE_MS`, bounding how long WebFetch waits for a page including redirects. Defaults to `300000`; `0` removes the limit, and any non-integer spelling silently keeps the default. Requires v2.1.268. [[line 381](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/env-vars.md?plain=1#L381)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* `CLAUDE_CODE_ENABLE_TODO_TOOLS` reworded to "get the task-tracking tools on every model", matching the allowlist framing. [[line 268](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/env-vars.md?plain=1#L268)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* New macOS guidance for `EPERM` in `~/Desktop`, `~/Documents`, `~/Downloads` or iCloud Drive: it's the terminal app being blocked by privacy settings, confirmed by `ls` failing with `Operation not permitted` even under `sudo`. Fix by quitting the terminal with Cmd+Q and reopening, or granting the folder in **System Settings > Privacy & Security > Files and Folders**. [[lines 2171-2177](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/errors.md?plain=1#L2171-L2177)] [[Source](https://code.claude.com/docs/en/errors#the-current-directory-no-longer-exists)]
* The GitHub-connect URL for ultrareview moved from `claude.ai/code/onboarding?step=alt-auth` to `claude.ai/connect-github`. [[lines 2531-2538](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/errors.md?plain=1#L2531-L2538)] [[Source](https://code.claude.com/docs/en/errors#your-checkout-has-no-branches)]

#### [fullscreen](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/fullscreen.md) [[Source](https://code.claude.com/docs/en/fullscreen)]

* `--system-prompt-snapshot` added to the flags fullscreen mode carries over. [[line 26](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/fullscreen.md?plain=1#L26)] [[Source](https://code.claude.com/docs/en/fullscreen#enable-fullscreen-rendering)]

#### [glossary](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/glossary.md) [[Source](https://code.claude.com/docs/en/glossary)]

* Checkpoint definition narrowed to prompts that start a turn. [[line 75](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/glossary.md?plain=1#L75)] [[Source](https://code.claude.com/docs/en/glossary#checkpoint)]

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* `WorktreeRemove` gains decision control: any non-zero exit code now fails worktree removal if the directory still exists afterward. The worktree and the background session both stay, and the refusal reports how the hook ended and quotes its stderr. [[lines 2954-2957](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/hooks.md?plain=1#L2954-L2957)] [[Source](https://code.claude.com/docs/en/hooks#worktreeremove-input)]
* New "MCP tool hook fields" guidance on when an `mcp_tool` hook actually runs: `SessionStart` at launch fires before MCP servers are available and its `mcp_tool` hooks are skipped (logged as `no MCP client context`), `Setup` skips them always, and only a `SessionStart` re-fired by `/clear` or compaction runs them. Use a `type: "command"` hook for anything needed from the first turn. [[lines 558-584](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/hooks.md?plain=1#L558-L584)] [[Source](https://code.claude.com/docs/en/hooks#mcp-tool-hook-fields)]
* `stopReason` now stays in the conversation, so Claude sees it if the conversation continues — previously documented as not shown to Claude. [[line 922](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/hooks.md?plain=1#L922)] [[Source](https://code.claude.com/docs/en/hooks#json-output)]
* `PermissionDenied`'s `reason` field rewritten for the bracketed rule names, and the `SubagentStop` example reason changed to `[Irreversible Local Destruction]`. [[lines 2151-2157](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/hooks.md?plain=1#L2151-L2157)] [[Source](https://code.claude.com/docs/en/hooks#permissiondenied-input)]
* `AskUserQuestion` and `ExitPlanMode` are now offered in `-p` runs **only when the run has a permission host**, such as an Agent SDK `canUseTool` callback or a `--permission-prompt-tool` MCP tool. [[lines 1768-1783](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/hooks.md?plain=1#L1768-L1783)] [[Source](https://code.claude.com/docs/en/hooks#pretooluse-decision-control)]
* `CLAUDE_ENV_FILE` variables set by `CwdChanged` and `FileChanged` hooks now persist only until the next `CwdChanged` event, when Claude Code clears them. [[lines 2695-2815](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/hooks.md?plain=1#L2695-L2815)] [[Source](https://code.claude.com/docs/en/hooks#cwdchanged)]
* `Write`'s structured output field changed from `success: true` to `type: "create"` in both the `PostToolUse` example and the `PostToolBatch` comparison. [[lines 1939-2107](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/hooks.md?plain=1#L1939-L2107)] [[Source](https://code.claude.com/docs/en/hooks#posttooluse-input)]
* `permission_suggestions` clarified: some dialogs, such as the one for file edits, don't read the array at all and derive options from the request itself. [[line 1827](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/hooks.md?plain=1#L1827)] [[Source](https://code.claude.com/docs/en/hooks#permissionrequest-input)]

#### [ide-integrations](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/ide-integrations.md) [[Source](https://code.claude.com/docs/en/ide-integrations)]

* Plugin changes made in the VS Code dialog now apply immediately to open sessions in that window instead of prompting for a restart; if the originating session can't reload, the dialog offers a retry or a restart. [[line 241](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/ide-integrations.md?plain=1#L241)] [[Source](https://code.claude.com/docs/en/ide-integrations#manage-marketplaces)]

#### [interactive-mode](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* The task list section rewritten around the allowlist: the list stays empty on any model outside it, including unrecognized model IDs, unless you opt in. [[line 594](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/interactive-mode.md?plain=1#L594)] [[Source](https://code.claude.com/docs/en/interactive-mode#task-list)]

#### [keybindings](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/keybindings.md) [[Source](https://code.claude.com/docs/en/keybindings)]

* Two more default `ctrl+x` chords documented — `ctrl+x ctrl+a` and `ctrl+x tab` in `Chat`, both requiring v2.1.260 — and added to the unbind example. [[lines 471-495](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/keybindings.md?plain=1#L471-L495)] [[Source](https://code.claude.com/docs/en/keybindings#unbind-default-shortcuts)]

#### [llm-gateway-connect](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/llm-gateway-connect.md) [[Source](https://code.claude.com/docs/en/llm-gateway-connect)]

* Where to put a gateway's own token now depends on the provider, and the page warns that without the skip-auth variable Claude Code strips any `Authorization` header that `ANTHROPIC_AUTH_TOKEN`, `apiKeyHelper` or `ANTHROPIC_CUSTOM_HEADERS` would add. [[lines 379-386](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/llm-gateway-connect.md?plain=1#L379-L386)] [[Source](https://code.claude.com/docs/en/llm-gateway-connect#route-to-a-cloud-provider-through-a-gateway)]
* New note that a set `AWS_BEARER_TOKEN_BEDROCK` overrides your gateway token even with `CLAUDE_CODE_SKIP_BEDROCK_AUTH` set. [[line 386](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/llm-gateway-connect.md?plain=1#L386)] [[Source](https://code.claude.com/docs/en/llm-gateway-connect#amazon-bedrock)]
* New Agent Platform guidance on per-model regions, pinned model versions, and declaring capabilities for a model ID your Claude Code version doesn't recognize. [[lines 428-432](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/llm-gateway-connect.md?plain=1#L428-L432)] [[Source](https://code.claude.com/docs/en/llm-gateway-connect#google-clouds-agent-platform)]
* Notes that on the Bedrock and Agent Platform routes Claude Code now limits beta headers and request fields to what the provider accepts. [[line 375](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/llm-gateway-connect.md?plain=1#L375)] [[Source](https://code.claude.com/docs/en/llm-gateway-connect#route-to-a-cloud-provider-through-a-gateway)]

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* A failed-connection message now shows the host **as written in configuration**, so a `${VAR}` in the host is no longer expanded in the error — the reverse of the previous behavior. [[line 270](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/mcp.md?plain=1#L270)] [[Source](https://code.claude.com/docs/en/mcp#server-status-detail)]
* New constraints on OAuth client secrets: settable only when adding the server, never re-prompted or read from `MCP_CLIENT_SECRET` at login, and changeable only by removing and re-adding the server. [[lines 820-821](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/mcp.md?plain=1#L820-L821)] [[Source](https://code.claude.com/docs/en/mcp#use-pre-configured-oauth-credentials)]
* Plugin MCP servers now connect or disconnect when the plugin change applies, rather than requiring `/reload-plugins`. [[line 468](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/mcp.md?plain=1#L468)] [[Source](https://code.claude.com/docs/en/mcp#plugin-provided-mcp-servers)]

#### [memory](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/memory.md) [[Source](https://code.claude.com/docs/en/memory)]

* Same external-import treatment for out-of-tree `.claude/rules/` symlinks as on the CLAUDE.md page. [[lines 240-242](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/memory.md?plain=1#L240-L242)] [[Source](https://code.claude.com/docs/en/memory#share-rules-across-projects-with-symlinks)]

#### [model-config](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* Dropped Fable 5's separate v2.1.170 requirement. [[line 79](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/model-config.md?plain=1#L79)] [[Source](https://code.claude.com/docs/en/model-config#work-with-fable)]

#### [monitoring-usage](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* `user.email` and the other identity attributes can now also come from a cloud session's own credentials, not just your sign-in. [[lines 458-1225](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/monitoring-usage.md?plain=1#L458-L1225)] [[Source](https://code.claude.com/docs/en/monitoring-usage#standard-attributes)]
* The retry `attempt` attribute now notes that some causes carry their own smaller retry budget — AWS or Google Cloud credential loading is retried at most twice. [[lines 1200-1202](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/monitoring-usage.md?plain=1#L1200-L1202)] [[Source](https://code.claude.com/docs/en/monitoring-usage#detect-retry-exhaustion)]

#### [permission-modes](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/permission-modes.md) [[Source](https://code.claude.com/docs/en/permission-modes)]

* Auto mode step 4 updated for the bracketed rule names Claude now receives. [[line 449](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/permission-modes.md?plain=1#L449)] [[Source](https://code.claude.com/docs/en/permission-modes#when-auto-mode-falls-back)]

#### [plugin-marketplaces](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/plugin-marketplaces.md) [[Source](https://code.claude.com/docs/en/plugin-marketplaces)]

* Install walkthrough now points at "Apply plugin changes without restarting". [[line 89](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/plugin-marketplaces.md?plain=1#L89)] [[Source](https://code.claude.com/docs/en/plugin-marketplaces#walkthrough-create-a-local-marketplace)]

#### [plugins-reference](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/plugins-reference.md) [[Source](https://code.claude.com/docs/en/plugins-reference)]

* New `--json` option documented on `plugin install`, `uninstall`, `update`, `enable` and `disable`, all requiring v2.1.268. `--json` can't be combined with `--prune` on uninstall. [[lines 993-1128](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/plugins-reference.md?plain=1#L993-L1128)] [[Source](https://code.claude.com/docs/en/plugins-reference#plugin-install)]
* New "JSON result format" section: parse only the last line of stdout, since a marketplace-declared command may print ahead of it. Always carries `command`, `outcome` (`ok`/`failed`) and `message`; a usage error prints no result line and exits 1. [[lines 998-1004](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/plugins-reference.md?plain=1#L998-L1004)] [[Source](https://code.claude.com/docs/en/plugins-reference#plugin-install)]
* `plugin list --json` rows gained parallel `errorDetails` and `noteDetails` arrays giving each diagnostic's `type` and the names it refers to. [[line 1147](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/plugins-reference.md?plain=1#L1147)] [[Source](https://code.claude.com/docs/en/plugins-reference#plugin-list)]

#### [prompt-caching](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/prompt-caching.md) [[Source](https://code.claude.com/docs/en/prompt-caching)]

* New "Resuming a session" section explaining that a resumed conversation keeps the system prompt it started with by default, so an upgrade or different `--append-system-prompt` text doesn't invalidate the cache until compaction or a new conversation. [[lines 229-233](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/prompt-caching.md?plain=1#L229-L233)] [[Source](https://code.claude.com/docs/en/prompt-caching#resuming-a-session)]
* "Changing output style" simplified: the feature-flag split is gone, and switching styles mid-session now always arrives as a message in the conversation, keeping the cache. [[lines 209-213](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/prompt-caching.md?plain=1#L209-L213)] [[Source](https://code.claude.com/docs/en/prompt-caching#changing-output-style)]
* The layer table no longer lists a Claude Code upgrade as something that changes the system prompt layer. [[lines 21-25](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/prompt-caching.md?plain=1#L21-L25)] [[Source](https://code.claude.com/docs/en/prompt-caching#how-the-cache-is-organized)]
* Compaction now switches a resumed session to the current system prompt, rebuilding that layer once. [[line 160](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/prompt-caching.md?plain=1#L160)] [[Source](https://code.claude.com/docs/en/prompt-caching#compacting-the-conversation)]
* Mid-conversation system context is now sent uncached when `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS` is set. [[line 47](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/prompt-caching.md?plain=1#L47)] [[Source](https://code.claude.com/docs/en/prompt-caching#where-the-cache-lives)]
* Cache scoping reworded: the working directory, platform, shell, OS version, branch and recent commits are now carried by the conversation rather than embedded in the system prompt. [[lines 285-287](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/prompt-caching.md?plain=1#L285-L287)] [[Source](https://code.claude.com/docs/en/prompt-caching#cache-scope)]

#### [remote-control](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/remote-control.md) [[Source](https://code.claude.com/docs/en/remote-control)]

* The `/rc active` indicator now sits at the end of the working-directory line in the startup header under fullscreen rendering, and in the footer otherwise. A failed connection also adds a warning line with the reason to the conversation. [[lines 121-125](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/remote-control.md?plain=1#L121-L125)] [[Source](https://code.claude.com/docs/en/remote-control#check-connection-status)]

#### [sandboxing](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/sandboxing.md) [[Source](https://code.claude.com/docs/en/sandboxing)]

* New one-session example using `--settings` to enable the sandbox and forbid unsandboxed retries without touching a settings file. [[lines 45-49](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/sandboxing.md?plain=1#L45-L49)] [[Source](https://code.claude.com/docs/en/sandboxing#get-started)]

#### [scheduled-tasks](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/scheduled-tasks.md) [[Source](https://code.claude.com/docs/en/scheduled-tasks)]

* A self-paced `/loop` is now explicitly **not restored** on resume — run `/loop` again to restart it. Only `CronCreate`-scheduled tasks come back. [[line 202](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/scheduled-tasks.md?plain=1#L202)] [[Source](https://code.claude.com/docs/en/scheduled-tasks#limitations)]

#### [security-guidance](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/security-guidance.md) [[Source](https://code.claude.com/docs/en/security-guidance)]

* Replaced the literal `/reload-plugins` block with a pointer to "Apply plugin changes without restarting". [[line 38](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/security-guidance.md?plain=1#L38)] [[Source](https://code.claude.com/docs/en/security-guidance#install-the-plugin)]

#### [server-managed-settings](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/server-managed-settings.md) [[Source](https://code.claude.com/docs/en/server-managed-settings)]

* Approving `sandbox.credentials` or `sandbox.network.tlsTerminate` now also covers the `sandbox.network.allowedDomains` entries delivered alongside them, and the dialog reappears when an administrator changes one of those entries. [[line 251](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/server-managed-settings.md?plain=1#L251)] [[Source](https://code.claude.com/docs/en/server-managed-settings#approval-memory)]

#### [settings-reference](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/settings-reference.md) [[Source](https://code.claude.com/docs/en/settings-reference)]

* New `copyOnSelect` global config setting (default `true`) controlling automatic clipboard copy on mouse selection in fullscreen rendering and agent view. Ignored in `settings.json` — it belongs in `~/.claude.json`. [[lines 5808-5824](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/settings-reference.md?plain=1#L5808-L5824)] [[Source](https://code.claude.com/docs/en/settings-reference#copyonselect)]
* A failed startup helper now reports its stdout when stderr is empty, and a timeout names the `timeoutMs` limit while including none of the helper's output. [[line 5684](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/settings-reference.md?plain=1#L5684)] [[Source](https://code.claude.com/docs/en/settings-reference#helper-failures)]

#### [settings](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* `modelPicker` added to the keys a `CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST` app overrides from managed sources. [[line 700](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/settings.md?plain=1#L700)] [[Source](https://code.claude.com/docs/en/settings#exceptions-to-managed-settings-precedence)]

#### [skills](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)]

* `context: fork` given a prominent warning that despite its name it does **not** fork the current conversation: the subagent starts with no history, so the skill's instructions must stand alone. Fork the conversation instead when the task depends on history. [[lines 652-654](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/skills.md?plain=1#L652-L654)] [[Source](https://code.claude.com/docs/en/skills#run-skills-in-a-subagent)]
* Command files in a subdirectory of `.claude/commands/` documented: the path becomes a `:`-separated prefix, so `.claude/commands/frontend/component.md` is invoked as `/frontend:component`. [[line 362](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/skills.md?plain=1#L362)] [[Source](https://code.claude.com/docs/en/skills#how-a-skill-gets-its-command-name)]
* `disableBundledSkills` no longer described as sparing `/doctor` — it now turns off bundled skills outright. [[lines 23-244](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/skills.md?plain=1#L23-L244)] [[Source](https://code.claude.com/docs/en/skills#bundled-skills)]
* A missing `description` now falls back to the first non-empty line of markdown content rather than the first paragraph. [[line 312](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/skills.md?plain=1#L312)] [[Source](https://code.claude.com/docs/en/skills#frontmatter-reference)]
* Several synced-skill protections now carry a v2.1.228 minimum: name-collision checks, display-text sanitization, literal handling of `!` and `@` in synced bodies, and the refusal to run `` !`<command>` `` from a synced skill. [[lines 211-612](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/skills.md?plain=1#L211-L612)] [[Source](https://code.claude.com/docs/en/skills#when-a-synced-skill-name-matches-another-command)]

#### [slash-commands](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/slash-commands.md) [[Source](https://code.claude.com/docs/en/slash-commands)]

* Carries the same set of skill changes: the `context: fork` warning, the `/frontend:component` subdirectory naming rule, the `disableBundledSkills` rewording, the `description` fallback, and the v2.1.228 floors on synced-skill handling. [[lines 23-654](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/slash-commands.md?plain=1#L23-L654)] [[Source](https://code.claude.com/docs/en/slash-commands#bundled-skills)]

#### [sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* Important clarification: a `disallowedTools` entry **with a specifier**, such as `Bash(git push *)`, removes the whole tool from the subagent rather than only the matching commands. To keep Bash and block specific commands, use a `permissions.deny` Bash rule instead. [[lines 277-442](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/sub-agents.md?plain=1#L277-L442)] [[Source](https://code.claude.com/docs/en/sub-agents#supported-frontmatter-fields)]

#### [terminal-config](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/terminal-config.md) [[Source](https://code.claude.com/docs/en/terminal-config)]

* Theme tokens retargeted: `promptBorder` now covers the input box border in every mode rather than Manual only, `autoAccept` and `planMode` no longer own their borders, and `planMode` extends to plan messages and dialogs. [[lines 205-216](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/terminal-config.md?plain=1#L205-L216)] [[Source](https://code.claude.com/docs/en/terminal-config#status-colors)]

#### [third-party-integrations](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/third-party-integrations.md) [[Source](https://code.claude.com/docs/en/third-party-integrations)]

* The inline list of organization-wide CLAUDE.md paths was replaced with links to the memory page. [[line 210](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/third-party-integrations.md?plain=1#L210)] [[Source](https://code.claude.com/docs/en/third-party-integrations#invest-in-documentation-and-memory)]

#### [tools-reference](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/tools-reference.md) [[Source](https://code.claude.com/docs/en/tools-reference)]

* "Task tool availability" rewritten as the allowlist, explicitly covering custom model names served through an LLM gateway. Applies from v2.1.268. [[lines 505-520](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/tools-reference.md?plain=1#L505-L520)] [[Source](https://code.claude.com/docs/en/tools-reference#task-tool-availability)]
* Auto-backgrounding simplified: only commands starting with `sleep` are now excluded. The former carve-outs for any command running `git` and for compound commands Claude Code can't fully parse are gone. [[line 175](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/tools-reference.md?plain=1#L175)] [[Source](https://code.claude.com/docs/en/tools-reference#background-commands)]
* WebFetch's five-minute download deadline is now tunable with `CLAUDE_CODE_WEBFETCH_DEADLINE_MS` on v2.1.268. [[line 533](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/tools-reference.md?plain=1#L533)] [[Source](https://code.claude.com/docs/en/tools-reference#webfetch-tool-behavior)]

#### [troubleshooting](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/troubleshooting.md) [[Source](https://code.claude.com/docs/en/troubleshooting)]

* New section on copied text not reaching your clipboard over SSH: outside tmux Claude Code falls back to an OSC 52 escape sequence, `/copy` reports success whether or not it arrived, and iTerm2 ignores it until you enable clipboard access while Terminal.app doesn't support it at all. Work around it with your terminal's native-selection key (`Fn` in Terminal.app, `Option` in iTerm2) or `CLAUDE_CODE_DISABLE_MOUSE=1`. [[lines 91-101](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/troubleshooting.md?plain=1#L91-L101)] [[Source](https://code.claude.com/docs/en/troubleshooting#copied-text-doesnt-reach-your-local-clipboard-over-ssh)]

#### [vs-code](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/vs-code.md) [[Source](https://code.claude.com/docs/en/vs-code)]

* Same two changes as the IDE integrations page: sessions open in your preferred location, and plugin dialog changes apply without a restart. [[lines 47-241](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/claude-code/vs-code.md?plain=1#L47-L241)] [[Source](https://code.claude.com/docs/en/vs-code#get-started)]

-----

## API changes

### Changed documents

#### [api/errors](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/api/api/errors.md) [[Source](https://platform.claude.com/docs/en/api/errors)]

* The `thinking.type.disabled` 400 error now has two documented message forms. Claude Mythos Preview — the only always-thinking model that still accepts extended thinking — returns a different message from Fable 5.1, Mythos 5.1, Fable 5 and Mythos 5, which are told to use `thinking.type.adaptive` with `output_config.effort`. [[lines 472-484](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/api/api/errors.md?plain=1#L472-L484)] [[Source](https://platform.claude.com/docs/en/api/errors#thinking-cannot-be-disabled)]

#### [build-with-claude/extended-thinking](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/api/build-with-claude/extended-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]

* Shortened the interleaved-thinking beta header's model list to "earlier Claude 4 models" instead of enumerating them. [[line 287](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/api/build-with-claude/extended-thinking.md?plain=1#L287)] [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#interleaved-thinking-in-manual-mode)]

#### [build-with-claude/task-budgets](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/api/build-with-claude/task-budgets.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/task-budgets)]

* The minimum `task_budget.total` is no longer described as model-specific: it's 20,000 tokens on every supporting model. [[line 617](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/api/build-with-claude/task-budgets.md?plain=1#L617)] [[Source](https://platform.claude.com/docs/en/build-with-claude/task-budgets#measure-your-current-usage)]

#### [build-with-claude/thinking-troubleshooting](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/api/build-with-claude/thinking-troubleshooting.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/thinking-troubleshooting)]

* Both error message forms spelled out here too, with the explanation now pointing at the per-model configuration table instead of repeating which models reject `"thinking.type.enabled"`. [[lines 59-71](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/api/build-with-claude/thinking-troubleshooting.md?plain=1#L59-L71)] [[Source](https://platform.claude.com/docs/en/build-with-claude/thinking-troubleshooting#a-400-error-says-thinkingtypedisabled-is-not-supported)]

#### [manage-claude/inference-hooks-configuration](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/api/manage-claude/inference-hooks-configuration.md) [[Source](https://platform.claude.com/docs/en/manage-claude/inference-hooks-configuration)]

* The endpoint setup flow was reordered so the signing secret now exists before the first connection test. The dialog (renamed **Set up endpoint**) asks only for the URL, then reveals the secret once, then reopens with custom headers and **Test connection**. [[lines 36-53](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/api/manage-claude/inference-hooks-configuration.md?plain=1#L36-L53)] [[Source](https://platform.claude.com/docs/en/manage-claude/inference-hooks-configuration#set-up-inference-hooks)]
* New "Signing secret required" failure result, telling you to click **Generate secret** under **Request signing** before testing. [[line 65](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/api/manage-claude/inference-hooks-configuration.md?plain=1#L65)] [[Source](https://platform.claude.com/docs/en/manage-claude/inference-hooks-configuration#set-up-inference-hooks)]
* The **Rotate secret** button reads **Generate secret** when the organization has no secret yet. [[line 134](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/api/manage-claude/inference-hooks-configuration.md?plain=1#L134)] [[Source](https://platform.claude.com/docs/en/manage-claude/inference-hooks-configuration#rotate-your-signing-secret)]

#### [manage-claude/inference-hooks-endpoint](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/api/manage-claude/inference-hooks-endpoint.md) [[Source](https://platform.claude.com/docs/en/manage-claude/inference-hooks-endpoint)]

* Connection tests are now signed, since the setup flow generates the secret first. The unsigned-request exception narrowed to organizations that enabled Inference hooks before secrets were required. [[line 291](https://github.com/gpambrozio/ClaudeDocs/blob/5dcef2548153763cbcd5ce2f06854f9fd72fe6f5/docs-md/api/manage-claude/inference-hooks-endpoint.md?plain=1#L291)] [[Source](https://platform.claude.com/docs/en/manage-claude/inference-hooks-endpoint#verify-the-signature)]
