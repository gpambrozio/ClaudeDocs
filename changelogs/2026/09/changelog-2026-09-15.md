# [Claude docs changes for September 15th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/9338ebe66ac60097772b0039e30dade435f1859c) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/9338ebe66ac60097772b0039e30dade435f1859c)]

## Executive Summary
- New security behavior worth knowing about: in a remote MCP server's `url` and `headers`, Claude Code now **reads credential variables as empty rather than expanding them** — `ANTHROPIC_API_KEY`, `AWS_BEARER_TOKEN_BEDROCK`, `HTTPS_PROXY`, `NPM_TOKEN` and friends — so a project's `.mcp.json` or a plugin can't quietly forward your credentials to a server it names
- Fast mode reaches cloud sessions and self-hosted runners (2.1.271), and `modelPricing` / the gateway `pricing` block now accept a `multiplier` **above** 1, up to 10, for marked-up internal chargeback rates
- `omitClaudeMd` lands in agent frontmatter, `--agents` JSON and plugin agents, letting a subagent run without user, project and local CLAUDE.md files while managed policy files still load
- `claude plugin install/update` gain `--accept-command <sha256>` as a tighter alternative to `-y`: the acceptance binds to exactly the command, plugin and catalog a previous `--json` run displayed, and any change since then makes Claude Code show the command again
- Three weekly "What's new" pages land at once (weeks 35, 36 and 37), and the Compliance API gains Claude-in-Slack per-channel manager assignment events

## New Claude Code versions

### [2.1.271](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/versions/2.1.271.md)

#### New features

* Added fast mode in Claude Code Remote sessions, both cloud and self-hosted runners
* Added mouse support to the `/config` panel in fullscreen mode: the wheel scrolls, a click on a value changes it
* Added per-command `allowed_domains` to Bash, PowerShell and Monitor in auto mode with sandboxing: the hosts a command needs are reviewed with it and opened for that command alone
* Added `omitClaudeMd` to agent frontmatter and `--agents` JSON
* Added `--accept-command <sha256>` to `claude plugin install` and `claude plugin update`
* Added support for a `multiplier` above 1, up to 10, in `modelPricing` and the gateway `pricing` block
* Added `claude self-hosted-runner --drain-marker-file <path>` to report a SIGTERM exit as a host drain

#### Existing feature improvements

* Improved Bash permission checking in four ways: catching the file `fmt`/`column` read after an unrecognized option, files a wildcard expands to inside a pattern or option value, shell variable declaration flags that could misrepresent the command, and commands with two directory changes or a `cd`+`git` chain that skipped the `blockReadsOutsideWorkingDirectories` prompt

#### Major bug fixes

* Fixed a cached organization policy being reused after switching accounts, organizations or API keys
* Fixed an enterprise `managed-mcp.json` that can't be read or parsed being ignored — it now keeps exclusive MCP control and warns at startup
* Fixed a stale `.git/config.lock` breaking `git checkout -b`, `git push -u` and `git config` for the rest of a session after a sandboxed command failed to start on Linux
* Fixed settings file changes made outside the session going unnoticed on macOS machines whose file-event service is saturated; the watcher now falls back to polling
* Fixed `/resume` and `/teleport` keeping the previous conversation's file-read tracking, **so Claude could edit files the resumed conversation had never read**
* Fixed MCP OAuth mishandling client registrations: denying consent forced a new one, one for another redirect URI was reused, and a concurrent write could delete a valid one
* Fixed sustained high CPU usage and repeated tool-list requests when an MCP server sends `list_changed` notifications in a tight loop
* Fixed self-hosted runner sessions silently losing all host config when the host config directory exceeds 64 MiB; added `--host-config-snapshot disk|memory`
* Fixed skills synced from claude.ai staying on disk indefinitely after signing out
* Fixed `--resume` dropping the 1M context window when the resumed session's model family differs from the configured default
* Fixed cross-session messages held by the receiving session's policy leaving no trace
* Fixed Claude starting a second copy of a background command that was still running after the conversation was compacted
* Fixed turns failing with "API returned an empty or malformed response" when an LLM gateway returns the non-streaming reply as `text/plain`

### [2.1.272](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/versions/2.1.272.md)

* Bug fixes and reliability improvements

-----

## Claude Code changes

### New Documents

#### [whats-new/2026-w35](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/claude-code/whats-new/2026-w35.md) [[Source](https://code.claude.com/docs/en/whats-new/2026-w35)]

Week 35 (August 24–28, v2.1.240 → v2.1.250): resuming terminal sessions in the Claude Code Desktop app with `/resume`, reviewing feedback reports Claude drafts for you, and starting a session in restricted mode.

#### [whats-new/2026-w36](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/claude-code/whats-new/2026-w36.md) [[Source](https://code.claude.com/docs/en/whats-new/2026-w36)]

Week 36 (August 31 – September 4, v2.1.251 → v2.1.261): Claude Fable 5.1 in Claude Code with the `fable` alias now selecting it — though **in Claude apps gateway sessions `fable` still selects Fable 5**, so you need `/model claude-fable-5-1` there. Plus computer use running in the background on Desktop and the live `/diff` panel.

#### [whats-new/2026-w37](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/claude-code/whats-new/2026-w37.md) [[Source](https://code.claude.com/docs/en/whats-new/2026-w37)]

Week 37 (September 7–11, v2.1.263 → v2.1.269): `claude plugin eval`, with the reminder that every run and every judge-scored check is a real model call on your account, and popping Claude Code Desktop panes out into their own windows.

### Changed documents

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* New "Credential variables that read as empty" section. In a remote server's `url` and `headers`, Claude Code deliberately reads credential variables as **empty** rather than expanding them, so a project `.mcp.json` or plugin can't send your credentials to a server it names. Writing `Bearer ${ANTHROPIC_AUTH_TOKEN}` sends `Bearer ` and the server usually answers `401`. The covered names are Claude Code's own credentials, your cloud provider's, and others your environment carries such as `HTTPS_PROXY` and `NPM_TOKEN`. [[lines 628-640](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/claude-code/mcp.md?plain=1#L628-L640)] [[Source](https://code.claude.com/docs/en/mcp#credential-variables-that-read-as-empty)]
* Two sharp edges of that rule: a covered name reads as empty **whether or not you set it**, and a `:-default` fallback on it is ignored. A provider base URL such as `ANTHROPIC_BASE_URL` still expands, so `"url": "${ANTHROPIC_BASE_URL}/mcp"` works — unless the URL itself embeds a credential. To pass a covered credential deliberately, copy it into a variable of your own naming. [[line 638](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/claude-code/mcp.md?plain=1#L638)] [[Source](https://code.claude.com/docs/en/mcp#credential-variables-that-read-as-empty)]
* The suppression is discoverable: run `claude --debug-file /tmp/claude-debug.log` and search for `never expanded toward a remote server`. [[line 642](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/claude-code/mcp.md?plain=1#L642)] [[Source](https://code.claude.com/docs/en/mcp#credential-variables-that-read-as-empty)]
* A missing `${VAR}` reference now warns in `claude mcp list` and `/mcp` naming the variable, and still loads the server with the text unexpanded. [[line 282](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/claude-code/mcp.md?plain=1#L282)] [[Source](https://code.claude.com/docs/en/mcp#configuration-warnings)]

#### [fast-mode](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/claude-code/fast-mode.md) [[Source](https://code.claude.com/docs/en/fast-mode)]

* New "Use fast mode in cloud sessions" section: `/fast on` works in cloud sessions on Anthropic-managed infrastructure or a self-hosted runner, for that session only, and needs v2.1.271 in the session's environment. [[lines 57-61](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/claude-code/fast-mode.md?plain=1#L57-L61)] [[Source](https://code.claude.com/docs/en/fast-mode#use-fast-mode-in-cloud-sessions)]
* Two distinct organization blocks documented, with their exact messages: fast mode not enabled for the org, and the fast-mode Opus model excluded by `availableModels`. In the latter case, a session already on an allowed Opus model that supports fast mode gets fast mode on its current model without a switch. [[lines 123-126](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/claude-code/fast-mode.md?plain=1#L123-L126)] [[Source](https://code.claude.com/docs/en/fast-mode#requirements)]
* The skip variables affect only the client-side check — an API rejection stands regardless, and Claude Code then retries at standard speed and turns fast mode off. [[line 159](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/claude-code/fast-mode.md?plain=1#L159)] [[Source](https://code.claude.com/docs/en/fast-mode#use-fast-mode-behind-proxies-and-llm-gateways)]

#### [sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)] / [agent-sdk/subagents](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/claude-code/agent-sdk/subagents.md)

* New `omitClaudeMd` frontmatter field. It drops the user, project and local CLAUDE.md files for an agent running as a subagent — **managed policy files still load** — and is ignored when the agent runs as the main thread agent. Requires TypeScript Agent SDK v0.3.271; the Python SDK's `AgentDefinition` doesn't have the field. [[line 150](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/claude-code/agent-sdk/subagents.md?plain=1#L150)] [[Source](https://code.claude.com/docs/en/agent-sdk/subagents#agentdefinition-configuration)]

#### [claude-apps-gateway-config](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/claude-code/claude-apps-gateway-config.md) [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config)]

* New "Mark prices up" section for a `multiplier` above 1. Two consequences are called out: **with an `admin:` block the markup also applies to spend limits**, so developers reach their caps sooner and the gateway logs a boot warning saying so; and the multiplier doesn't change what the upstream provider charges. A gateway server earlier than v2.1.271 refuses to start with a markup set, and clients earlier than v2.1.271 ignore it and show costs without it. [[lines 467-482](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/claude-code/claude-apps-gateway-config.md?plain=1#L467-L482)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config#mark-prices-up)]

#### [permission-modes](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/claude-code/permission-modes.md) [[Source](https://code.claude.com/docs/en/permission-modes)]

* A significant clarification that runs through the whole page: **in interactive terminal sessions where bypass permissions are available, plan mode's blocks aren't enforced.** Claude is still instructed to plan without editing, but a file edit or shell command it attempts during planning runs without prompting — only explicit ask rules and critical-path removals still prompt. [[line 514](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/claude-code/permission-modes.md?plain=1#L514)] [[Source](https://code.claude.com/docs/en/permission-modes#skip-all-checks-with-bypasspermissions-mode)]
* Plan mode keeps its blocks everywhere without an interactive terminal: `-p` runs, Agent SDK sessions, and the VS Code extension's chat panel. [[line 516](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/claude-code/permission-modes.md?plain=1#L516)] [[Source](https://code.claude.com/docs/en/permission-modes#skip-all-checks-with-bypasspermissions-mode)]
* Protected-path writes gained the same carve-out, and the planning-command table row now covers all three cases. [[lines 24-551](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/claude-code/permission-modes.md?plain=1#L24-L551)] [[Source](https://code.claude.com/docs/en/permission-modes#available-modes)]

#### [plugins-reference](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/claude-code/plugins-reference.md) [[Source](https://code.claude.com/docs/en/plugins-reference)]

* `--accept-command <sha256>` documented at length: the acceptance counts for exactly that command, plugin and marketplace catalog, and **if any of them changed since the command was displayed — including through the run's own marketplace refresh — Claude Code doesn't accept the digest and shows the command again.** It can't be combined with `-y`, and has no effect inside a Claude Code session. [[lines 1000-1017](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/claude-code/plugins-reference.md?plain=1#L1000-L1017)] [[Source](https://code.claude.com/docs/en/plugins-reference#plugin-install)]
* A `failed` result now carries a `shownCommand` object with the command as displayed, its plugin, and its `sha256`; `acceptCommandMatched: false` means the digest you passed doesn't match what's now displayed, so show that command to a person first. [[lines 1015-1017](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/claude-code/plugins-reference.md?plain=1#L1015-L1017)] [[Source](https://code.claude.com/docs/en/plugins-reference#plugin-install)]
* Synced plugins: `claude plugin disable <name>@synced` saves the choice in that environment's user-level `enabledPlugins`, but a plugin your organization requires can't be turned off this way and the command saves nothing. [[lines 413-414](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/claude-code/plugins-reference.md?plain=1#L413-L414)] [[Source](https://code.claude.com/docs/en/plugins-reference#edit-reload-and-disable-a-skills-directory-plugin)]
* Plugin agents support `omitClaudeMd`, and for security still don't support `hooks`, `mcpServers` or `permissionMode`. [[lines 62-64](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/claude-code/plugins-reference.md?plain=1#L62-L64)] [[Source](https://code.claude.com/docs/en/plugins-reference#agents)]

#### [prompt-caching](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/claude-code/prompt-caching.md) [[Source](https://code.claude.com/docs/en/prompt-caching)]

* A precise account of when adding a bare tool deny rule costs you the cache: **with tool search active (the default on supported models) the tool definitions don't change and the cached prefix survives**; without it Claude Code removes the definition and invalidates the cache, and so does removing the rule later. Only a rule matching in the tool-name position does this — scoped rules like `Bash(rm *)`, and all allow and ask rules, leave the prefix intact. [[lines 154-158](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/claude-code/prompt-caching.md?plain=1#L154-L158)] [[Source](https://code.claude.com/docs/en/prompt-caching#denying-an-entire-tool)]
* `/model` asks you to confirm a switch only while the cache is warm **and** the new model isn't the one that produced the last response. [[line 77](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/claude-code/prompt-caching.md?plain=1#L77)] [[Source](https://code.claude.com/docs/en/prompt-caching#switching-models)]

#### [managed-mcp](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/claude-code/managed-mcp.md) [[Source](https://code.claude.com/docs/en/managed-mcp)]

* Spells out exactly what a deployed `managed-mcp.json` permits: the file's servers, `managedMcpServers` from managed settings, and in-process servers the host app registers. Everything else — plugin servers and `--mcp-config` included — is excluded, and claude.ai connectors are suppressed unless explicitly allowed. [[lines 39-45](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/claude-code/managed-mcp.md?plain=1#L39-L45)] [[Source](https://code.claude.com/docs/en/managed-mcp#exclusive-control-with-managed-mcpjson)]
* Verification guidance distinguishing two failure signatures: user servers still appearing means the file isn't being read, while the file's servers missing plus a failed-to-parse diagnostic means it can't be parsed. [[lines 116-118](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/claude-code/managed-mcp.md?plain=1#L116-L118)] [[Source](https://code.claude.com/docs/en/managed-mcp#validate-the-configuration)]

#### [monitoring-usage](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* New `event.sequence` attribute added to every event, with an important caveat: it's counted **per Claude Code process, not per session**, and a resumed session takes its values from the resuming process — so within one session a later event can carry a lower value than an earlier one, or repeat one. Sort by `event.timestamp` and use `event.sequence` only to break ties. [[lines 620-626](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/claude-code/monitoring-usage.md?plain=1#L620-L626)] [[Source](https://code.claude.com/docs/en/monitoring-usage#event-correlation-attributes)]

#### [ide-integrations](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/claude-code/ide-integrations.md) [[Source](https://code.claude.com/docs/en/ide-integrations)]

* New **prompt cache clock** documentation: it counts down the conversation's cache lifetime and restarts on each response that uses the cache. Apart from compaction, the actions that invalidate the cache **don't** reset the clock, so it can still show minutes left after you switch models. It turns red without minutes right after a compaction too. [[lines 112-115](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/claude-code/ide-integrations.md?plain=1#L112-L115)] [[Source](https://code.claude.com/docs/en/ide-integrations#use-the-prompt-box)]
* New `attachOpenFile` setting (default on) for including the editor's open file in messages; when off, only selected text is added. A `Read` deny rule on a path prevents both the selection and the open-file notice for that file. Requires v2.1.271. [[lines 135-391](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/claude-code/ide-integrations.md?plain=1#L135-L391)] [[Source](https://code.claude.com/docs/en/ide-integrations#reference-files-and-folders)]
* The usage dialog now flags behaviors accounting for 10% or more of recent usage — cache misses, long context, subagent-heavy or highly parallel sessions — each with a tip, plus attribution tables per skill, subagent, plugin and MCP server. [[line 179](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/claude-code/ide-integrations.md?plain=1#L179)] [[Source](https://code.claude.com/docs/en/ide-integrations#check-account-and-usage)]

#### [cross-session-messaging](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/claude-code/cross-session-messaging.md) [[Source](https://code.claude.com/docs/en/cross-session-messaging)]

* When no `crossSessionInbound` value applies, Claude Code decides per message from the two sessions' permission modes, grouping bypass-style sessions into one class and everything else into the other. Plan mode counts as bypassing in interactive terminal sessions with bypass available, while auto, `acceptEdits` and `dontAsk` count as prompting. [[lines 215-217](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/claude-code/cross-session-messaging.md?plain=1#L215-L217)] [[Source](https://code.claude.com/docs/en/cross-session-messaging#control-inbound-messages)]
* Senders now get a notice when a receiver holds a message, and a follow-up when it's delivered, denied or expired, **so the sending Claude knows not to keep waiting**. `claude -p` senders receive it as an informational `system` message; that requires v2.1.271. [[lines 231-235](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/claude-code/cross-session-messaging.md?plain=1#L231-L235)] [[Source](https://code.claude.com/docs/en/cross-session-messaging#control-inbound-messages)]

#### [self-hosted-environments-reference](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/claude-code/self-hosted-environments-reference.md) [[Source](https://code.claude.com/docs/en/self-hosted-environments-reference)]

* New `--host-config-snapshot <mode>`. The default `disk` verifies every file against an in-memory digest at each session start and **refuses sessions until you restart the runner** if a file in the copy was modified; `memory` caps the snapshot at 64 MiB and starts sessions without host config above it. Requires v2.1.271. [[line 35](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/claude-code/self-hosted-environments-reference.md?plain=1#L35)] [[Source](https://code.claude.com/docs/en/self-hosted-environments-reference#runner-cli-flags)]
* New `--drain-marker-file <path>`, telemetry-only, with the caution to name a path on a local filesystem that sessions can't write to. [[line 26](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/claude-code/self-hosted-environments-reference.md?plain=1#L26)] [[Source](https://code.claude.com/docs/en/self-hosted-environments-reference#runner-cli-flags)]

#### [settings-reference](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/claude-code/settings-reference.md) [[Source](https://code.claude.com/docs/en/settings-reference)]

* `modelPricing.multiplier` now accepts up to 10, with markup requiring v2.1.271; earlier versions ignore a markup with a warning and keep the rest of the setting. [[lines 1090-1102](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/claude-code/settings-reference.md?plain=1#L1090-L1102)] [[Source](https://code.claude.com/docs/en/settings-reference#modelpricing)]
* Parent settings from an embedding host keep their `deny` and `ask` rules **except `Read` and `Edit` rules whose pattern starts with `!`** — a host can't carve paths out of the managed rules with a negation. [[line 1269](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/claude-code/settings-reference.md?plain=1#L1269)] [[Source](https://code.claude.com/docs/en/settings-reference#allowmanagedpermissionrulesonly)]
* Deny-rule coverage refined again: `tee` joins the recognized Bash file commands, and the exclusions now name a command that reads files without naming them, such as `grep -r pattern .`. [[line 1440](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/claude-code/settings-reference.md?plain=1#L1440)] [[Source](https://code.claude.com/docs/en/settings-reference#permissionsdeny)]
* New footer badge setting rendering clickable badges when a regex matches turn output — tool results, file contents, fetched pages and Claude's own replies — turning IDs like `PROJ-1234` into links. [[lines 3036-3057](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/claude-code/settings-reference.md?plain=1#L3036-L3057)] [[Source](https://code.claude.com/docs/en/settings-reference#footerlinksregexes)]
* The workflow size guideline is advice, not an enforced cap: `"small"` asks for fewer than 5 agents, `"medium"` fewer than 10, `"large"` fewer than 50. [[line 3925](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/claude-code/settings-reference.md?plain=1#L3925)] [[Source](https://code.claude.com/docs/en/settings-reference#workflowsizeguideline)]

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* `CLAUDE_CODE_RETRY_WATCHDOG` now fails at once on a standard-speed `429` reporting a spend limit or exhausted usage credits, including a gateway spend cap that resets on a schedule. Before v2.1.239 it retried those indefinitely. [[line 316](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/claude-code/errors.md?plain=1#L316)] [[Source](https://code.claude.com/docs/en/errors#tune-retry-behavior)]
* Distinguishes `Login expired` — which Claude Code produces itself for a login it already failed to renew, sending no request — from the API-returned OAuth rejections. [[line 1047](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/claude-code/errors.md?plain=1#L1047)] [[Source](https://code.claude.com/docs/en/errors#login-expired)]

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* A prompt sent while SessionStart hooks are still running doesn't reach Claude until they finish, including on a resume — press `Esc` to take it back into the input while the hooks keep running. [[lines 1108-1110](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/claude-code/hooks.md?plain=1#L1108-L1110)] [[Source](https://code.claude.com/docs/en/hooks#sessionstart)]
* New `resolvedModel` field naming the model a subagent actually started on, which can differ from the requested one when `availableModels` or another override applies. [[lines 1703-1712](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/claude-code/hooks.md?plain=1#L1703-L1712)] [[Source](https://code.claude.com/docs/en/hooks#agent)]

#### [artifacts](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/claude-code/artifacts.md) [[Source](https://code.claude.com/docs/en/artifacts)]

* Source file types tightened: `.html`, `.htm` or `.md` decoding as UTF-8 or BOM-marked little-endian UTF-16. A file that doesn't decode, or that contains `U+FFFD`, is refused with the line and column to fix. [[line 280](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/claude-code/artifacts.md?plain=1#L280)] [[Source](https://code.claude.com/docs/en/artifacts#page-constraints)]

#### [amazon-bedrock](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/claude-code/amazon-bedrock.md) [[Source](https://code.claude.com/docs/en/amazon-bedrock)]

* Credential-helper caching documented: with a valid ISO 8601 `Expiration`, Claude Code caches until five minutes before it; without one, for an hour. [[line 210](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/claude-code/amazon-bedrock.md?plain=1#L210)] [[Source](https://code.claude.com/docs/en/amazon-bedrock#configuration-settings-explained)]

#### [remote-control](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/claude-code/remote-control.md) [[Source](https://code.claude.com/docs/en/remote-control)]

* The three "session changed elsewhere" failure reasons are now spelled out individually — taken over by another connection, ended or archived from another device, or no longer reported by the server — each with whether reconnecting is what you want. [[lines 123-127](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/claude-code/remote-control.md?plain=1#L123-L127)] [[Source](https://code.claude.com/docs/en/remote-control#check-connection-status)]

#### [large-codebases](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/claude-code/large-codebases.md) [[Source](https://code.claude.com/docs/en/large-codebases)]

* A useful warning for monorepos: names always load, but when there are many skills **some lose their descriptions entirely**, stripping the keywords Claude uses to decide whether a skill applies. Keep descriptions short and lead with words a request would contain. [[lines 350-358](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/claude-code/large-codebases.md?plain=1#L350-L358)] [[Source](https://code.claude.com/docs/en/large-codebases#keep-skills-discoverable)]

-----

## API changes

### Changed documents

#### [api/compliance](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/api/api/compliance.md) [[Source](https://platform.claude.com/docs/en/api/compliance)]

* Two new activity types, `ccr_channel_manager_added` and `ccr_channel_manager_removed`, recording an owner or admin assigning an organization member to manage one Slack channel's Claude configuration. The activity-type enum now reads "or 492 more". [[lines 192-198](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/api/api/compliance.md?plain=1#L192-L198)] [[Source](https://platform.claude.com/docs/en/api/compliance#query-parameters)]
* A new `via_account_assignment` authorization leg on Claude Tag events, distinguishing a direct channel-manager assignment from a role-granted permission. When it's true, `via_full_manage` and `via_entitlement_leg` are false and `granting_role_ids` is empty — and the field is **absent on events recorded before direct assignments existed, which you should treat as false**. [[line 10501](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/api/api/compliance.md?plain=1#L10501)] [[Source](https://platform.claude.com/docs/en/api/compliance#returns)]
* A `move_thread` comment action was added to the comment-action enum. [[line 7450](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/api/api/compliance.md?plain=1#L7450)] [[Source](https://platform.claude.com/docs/en/api/compliance#returns)]

#### [api/beta](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/api/api/beta.md) [[Source](https://platform.claude.com/docs/en/api/beta)]

* `temperature` is now marked **Deprecated**: models released after Claude Opus 4.6 don't support setting it, and while `1.0` is accepted for backwards compatibility, every other value is rejected with a 400. [[line 5048](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/api/api/beta.md?plain=1#L5048)] [[Source](https://platform.claude.com/docs/en/api/beta#body-parameters)]
* A new terminal iteration entry marks a fallback-served turn: when a fallback hop's output is the returned message, the completing iteration carries this type in place of `message`. Its presence in `usage.iterations` is how you tell a fallback model served the response. [[lines 6637-6642](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/api/api/beta.md?plain=1#L6637-L6642)] [[Source](https://platform.claude.com/docs/en/api/beta#returns)]
* Subagent thread routing fields added across the streaming event types: a server-set field naming the subagent thread a confirmation or result was routed to, and a cross-post marker for events surfaced from a subagent's thread onto the primary thread's stream. The cross-post marker is **informational only** — the server routes the matching response by `tool_use_id` or `custom_tool_use_id`, so clients don't send it back. [[lines 36152-36490](https://github.com/gpambrozio/ClaudeDocs/blob/9338ebe66ac60097772b0039e30dade435f1859c/docs-md/api/api/beta.md?plain=1#L36152-L36490)] [[Source](https://platform.claude.com/docs/en/api/beta#returns)]
