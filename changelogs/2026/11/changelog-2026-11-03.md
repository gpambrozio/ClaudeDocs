# [Claude docs changes for November 3rd, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/7f18f0fb515a154b6908d82d05beda57aa5206a8) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/7f18f0fb515a154b6908d82d05beda57aa5206a8)]

## Executive Summary
- Claude Code 2.1.317 adds an email-sharing check before web or shell calls, `onFailure: "block"` for Agent SDK hook callbacks, a Claude apps gateway cost report API, and richer OTel attributes, plus many fixes.
- Computer use and browser use toolsets (`computer_toolset_20260801`, `browser_toolset_20260801`) are now documented as available on Amazon Bedrock, Claude Platform on AWS and Microsoft Foundry. Claude 5.5 models reject older computer use tool versions.
- LLM gateway docs now describe how Claude Code retries after a rejected beta value, advisor tool, `effort` or `context_management`, and how long each rejection is remembered.
- Claude Code docs add Bedrock and Vertex AI pin-update prompts, `/btw` for subagent transcripts, cloud-session MCP elicitation cards, and Desktop SSH `ConnectTimeout` behavior.
- Managed Agents examples now disable `web_search` and `web_fetch` through `agent_toolset_20260401` configs.

## New Claude Code versions

### [2.1.317](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/versions/2.1.317.md)

#### New features

* `/schedule` warns when a new cloud scheduled task gets connectors you did not ask for
* Asks before a web or shell tool call sends your account email address to the network
* Agent SDK hook callbacks support `onFailure: "block"`, so a failing callback blocks the action
* Notices in Claude Desktop's Code tab when remote managed settings haven't loaded, and when they do
* Notice when auto mode's check has no answer for a subagent's tool call
* OTel metrics, events and spans now carry `anthropic.plan`, `anthropic.seat_type`, `anthropic.provider` and `anthropic.custom_base_url`
* Claude apps gateway admin API cost report, `GET /v1/organizations/analytics/cost`, by total, developer, day or IdP group
* Gateways with `admin:` set keep a daily record of developers' IdP groups for `admin.identity_retention_days`
* `CLAUDE_CODE_DISABLE_NESTED_SESSION_ID=1` restores the old session ID and transcript sharing for `claude -p` run inside a session on a self-hosted runner
* Cloud sessions get a link card for MCP server link requests

#### Existing feature improvements

* Clearer Microsoft Foundry error when Azure credentials can't be loaded (`cloud_credential_error`)
* `/design-sync` says up front when your design system has moved to Claude
* Clearer startup error when a required Claude apps gateway is unreachable or its TLS certificate can't be verified
* The "Resume this session with" exit hint repeats the flags you launched with
* Better self-hosted runner recovery from 5xx errors and unanswered heartbeats
* SendMessage to a running background agent arrives earlier, moving its running command to the background
* Subagents and teammates on a different model use that model's saved or default effort level
* Exit skips the "Background work is running" prompt for plugin monitors
* The `plugin-authoring` skill offers to help share a mod once it works
* Removed the Read tool's "file unchanged since your last Read" stub
* Remote Control fork names keep their "(fork)" ending
* Cloud sessions: the organization environment dialog has a shorter layout, adding a network secret for a host that already has one is refused, and new scheduled tasks start on the organization's default environment
* Claude Tag: pasted artifact links in Slack show a simpler card with an Open button

#### Major bug fixes

* Fixed project and local MCP servers disconnecting after the first turn in some Desktop sessions
* Fixed auto mode failing every turn when an LLM gateway answers 403 or 422 to its safety check
* Fixed `claude auth status` exiting before a slow token refresh was saved, which could sign you out
* Fixed `claude -p` exiting 0 when a full disk or quota lost its transcript or `~/.claude.json` writes
* Fixed `claude -p` inside cloud or self-hosted runner sessions sharing the session's ID and transcript, and generating its own title
* Fixed "Prompt is too long" after automatic compaction with a very large, changed CLAUDE.md
* Fixed very long conversations losing their earlier summary when compaction had to shorten its request
* Fixed the Claude apps gateway hiding Amazon Bedrock's "Input is too long." error
* Fixed Claude treating partial Grep and Glob results as complete after a timeout
* Fixed a region or network block (HTTP 403) showing as a sign-in failure
* Fixed "unable to get local issuer certificate" behind some TLS-inspecting proxies after a root certificate renewal
* Fixed OpenTelemetry export hangs and connection floods behind proxies; exports now time out after 10 seconds
* Fixed `DISABLE_PROMPT_CACHING_OPUS` and `DISABLE_PROMPT_CACHING_SONNET` not applying to `[1m]`, other-region and undated model spellings
* Fixed settings edits made just after launch not taking effect
* Fixed Claude deleting the most recently updated `/team-onboarding` guide when none was named
* Fixed Ctrl+C at the prompt stopping all background agents
* Fixed several agent team issues with inboxes, re-created teammates and auto mode in panes
* Fixed `claude --from-pr` reporting "No conversations found" in projects with many sessions
* Fixed self-hosted runner sessions losing turns when restarted while a plan awaited approval
* Fixed high memory use and slow startup in headless sessions with many plugins
* VSCode: fixed forked conversations dropping messages and messages lost when Claude was slow to start
* Windows: fixed every tool call refused on some volumes and scratchpad paths hitting the 260-character limit

-----

## Claude Code changes

### New Documents

None.

### Changed documents

#### [admin-setup](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/admin-setup.md) [[Source](https://code.claude.com/docs/en/admin-setup)]

* In WSL sessions, a `~` entry in Claude Desktop's `allowedWorkspaceFolders` means the distribution's home directory. [[line 78](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/admin-setup.md?plain=1#L78)] [[Source](https://code.claude.com/docs/en/admin-setup#wsl-sessions-in-claude-code-desktop)]

#### [agent-sdk/typescript](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* Documents what the `/core` entry exports and which root exports it leaves out. [[line 51](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L51)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#import-the-core-entry-when-you-bundle-the-agent-sdk)]
* New startup failure reasons `sandbox_required_unavailable` and `org_config_refused`. [[lines 2004-2028](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L2004-L2028)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#startup_failure_reason)]

#### [amazon-bedrock](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/amazon-bedrock.md) [[Source](https://code.claude.com/docs/en/amazon-bedrock)]

* Claude Code prompts to update an older pinned model version when the account can invoke the newer one. Managed-settings pins and inference profile ARN pins are not checked. [[lines 307-314](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/amazon-bedrock.md?plain=1#L307-L314)] [[Source](https://code.claude.com/docs/en/amazon-bedrock#startup-model-checks)]
* New sections on starting a session on a specific model and on remembered model refusals, cached for up to a day. [[lines 318-329](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/amazon-bedrock.md?plain=1#L318-L329)] [[Source](https://code.claude.com/docs/en/amazon-bedrock#start-a-session-on-a-specific-model)]

#### [analytics](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/analytics.md) [[Source](https://code.claude.com/docs/en/analytics)]

* Clarified the Console dashboard metrics (lines accepted, spend, active users, team insights date range) and the permissions needed to view it. [[lines 191-214](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/analytics.md?plain=1#L191-L214)] [[Source](https://code.claude.com/docs/en/analytics#access-analytics-for-api-customers)]

#### [authentication](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/authentication.md) [[Source](https://code.claude.com/docs/en/authentication)]

* Expanded the description of `CLAUDE_CODE_OAUTH_TOKEN` in the credential precedence list, including what happens when you run `/login`. [[line 250](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/authentication.md?plain=1#L250)] [[Source](https://code.claude.com/docs/en/authentication#authentication-precedence)]

#### [claude-md](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/claude-md.md) [[Source](https://code.claude.com/docs/en/claude-md)]

* Path-scoped rules also load when Bash views a matching file in a way that counts as a read, such as `cat` or `head`. [[line 205](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/claude-md.md?plain=1#L205)] [[Source](https://code.claude.com/docs/en/claude-md#path-specific-rules)]
* Expanded the glob pattern table (`**/*.ts`, `src/**/*`, `/*.md`, and more). [[lines 218-222](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/claude-md.md?plain=1#L218-L222)] [[Source](https://code.claude.com/docs/en/claude-md#path-specific-rules)]

#### [cli-reference](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* `--max-turns` has no limit by default, and with `--input-format stream-json` a queued message starts a new turn with its own limit. [[line 102](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/cli-reference.md?plain=1#L102)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-flags)]

#### [cloud-environments](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/cloud-environments.md) [[Source](https://code.claude.com/docs/en/cloud-environments)]

* Cloud sessions include Chrome for Testing at `/usr/bin/google-chrome`, with `CHROME_PATH` set. [[line 334](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/cloud-environments.md?plain=1#L334)] [[Source](https://code.claude.com/docs/en/cloud-environments#installed-tools)]

#### [commands](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/commands.md) [[Source](https://code.claude.com/docs/en/commands)]

* `/verify` runs only when you invoke it. [[line 34](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/commands.md?plain=1#L34)] [[Source](https://code.claude.com/docs/en/commands#all-commands)]

#### [costs](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/costs.md) [[Source](https://code.claude.com/docs/en/costs)]

* Explains that `/usage` computes the dollar figure locally at list price unless an admin `modelPricing` table is in effect. [[line 19](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/costs.md?plain=1#L19)] [[Source](https://code.claude.com/docs/en/costs#using-the-usage-command)]
* On Pro, Max and Ultra plans, reaching your spend limit with credits left prompts you to raise or remove the limit in the CLI. [[line 139](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/costs.md?plain=1#L139)] [[Source](https://code.claude.com/docs/en/costs#add-usage-credits-to-your-subscription)]
* Console reporting now points to the Console dashboard and the Claude Code Analytics API. [[lines 150-194](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/costs.md?plain=1#L150-L194)] [[Source](https://code.claude.com/docs/en/costs#manage-costs-for-your-organization)]

#### [desktop](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)]

* Browser pane cookies are lost when you quit Desktop in an SSH session. [[line 130](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/desktop.md?plain=1#L130)] [[Source](https://code.claude.com/docs/en/desktop#preview-your-app)]
* The usage ring sits under the prompt box in both layouts and shows plan usage. [[line 313](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/desktop.md?plain=1#L313)] [[Source](https://code.claude.com/docs/en/desktop#check-usage)]
* Explains the **Worktree** toggle, including with third-party providers. [[lines 410-412](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/desktop.md?plain=1#L410-L412)] [[Source](https://code.claude.com/docs/en/desktop#run-a-session-in-its-own-worktree)]
* SSH: built-in SSH client usage on Windows, which SSH config settings Desktop reads, and a new `ConnectTimeout` table with default timeouts through jump hosts and `ProxyCommand`. [[lines 1095-1220](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/desktop.md?plain=1#L1095-L1220)] [[Source](https://code.claude.com/docs/en/desktop#connect-on-windows-without-the-openssh-client)]
* SSH reconnect behavior: slower retries after a long outage and a message held back when organization settings haven't loaded. [[lines 1378-1383](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/desktop.md?plain=1#L1378-L1383)] [[Source](https://code.claude.com/docs/en/desktop#reconnect-after-sleep-or-a-network-loss)]
* Two new SSH error cards: `[SERVER_NOT_RUNNABLE]`/`[SETUP_DIR_NOEXEC]` and `[DOWNLOAD_BUSY]`. [[lines 2300-2301](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/desktop.md?plain=1#L2300-L2301)] [[Source](https://code.claude.com/docs/en/desktop#ssh-connection-fails-after-you-log-in)]

#### [desktop-changelog](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/desktop-changelog.md) [[Source](https://code.claude.com/docs/en/desktop-changelog)]

* Updated Desktop release notes with the same SSH, Worktree and usage ring changes as the Desktop page.

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* New `CLAUDE_CODE_DISABLE_CFC_PROMPT` omits the Claude in Chrome section of the system prompt while keeping the browser tools. [[line 238](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/env-vars.md?plain=1#L238)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* New `CLAUDE_CODE_GLOB_TIMEOUT_SECONDS` sets the Glob and Grep timeout (20 seconds, 60 on WSL). [[line 306](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/env-vars.md?plain=1#L306)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* Documented `CLAUDE_CODE_OAUTH_REFRESH_TOKEN`, `CLAUDE_CODE_OAUTH_SCOPES` and `CLAUDE_CODE_OAUTH_TOKEN`. [[lines 334-336](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/env-vars.md?plain=1#L334-L336)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* New `FORCE_HYPERLINK` enables OSC 8 hyperlinks in terminals that aren't auto-detected. [[line 468](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/env-vars.md?plain=1#L468)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* Several error entries now suggest checking that an LLM gateway forwards tool search fields (`defer_loading`, `tool_reference`). Update to v2.1.305+ for the automatic retry. [[lines 551-2568](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/errors.md?plain=1#L551-L2568)] [[Source](https://code.claude.com/docs/en/errors#api-error-500-internal-server-error)]
* Usage-limit warnings (such as "used 85% of your session limit") and the `rate_limits` status line fields. [[line 836](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/errors.md?plain=1#L836)] [[Source](https://code.claude.com/docs/en/errors#youve-hit-your-session-limit)]
* The unrecognized-model stderr line adds `query_source` and is written once per model ID per process. [[lines 6201-6208](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/errors.md?plain=1#L6201-L6208)] [[Source](https://code.claude.com/docs/en/errors#unrecognized-model-id-on-a-request)]

#### [fast-mode](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/fast-mode.md) [[Source](https://code.claude.com/docs/en/fast-mode)]

* Console users can group by **Speed (research preview)** on the Usage and Cost pages to see fast mode spend. [[line 94](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/fast-mode.md?plain=1#L94)] [[Source](https://code.claude.com/docs/en/fast-mode#see-where-fast-mode-spend-appears)]

#### [google-vertex-ai](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/google-vertex-ai.md) [[Source](https://code.claude.com/docs/en/google-vertex-ai)]

* Same pin-update prompt as on Bedrock: accepting writes the new model ID to user settings, declining is remembered until the next default change, and managed pins aren't checked. [[lines 191-196](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/google-vertex-ai.md?plain=1#L191-L196)] [[Source](https://code.claude.com/docs/en/google-vertex-ai#startup-model-checks)]
* New sections on starting a session on a specific model and on remembered model refusals. [[lines 200-208](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/google-vertex-ai.md?plain=1#L200-L208)] [[Source](https://code.claude.com/docs/en/google-vertex-ai#start-a-session-on-a-specific-model)]

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* Prompt and agent hooks default to the model used for background functionality. [[lines 579-3946](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/hooks.md?plain=1#L579)] [[Source](https://code.claude.com/docs/en/hooks#prompt-and-agent-hook-fields)]

#### [iam](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/iam.md) [[Source](https://code.claude.com/docs/en/iam)]

* Expanded the `CLAUDE_CODE_OAUTH_TOKEN` precedence entry, same as authentication. [[line 250](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/iam.md?plain=1#L250)] [[Source](https://code.claude.com/docs/en/iam#authentication-precedence)]

#### [interactive-mode](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* `/btw` compared with subagents and forks. New section: with a subagent transcript open, `/btw` answers from that transcript. [[lines 707-713](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/interactive-mode.md?plain=1#L707-L713)] [[Source](https://code.claude.com/docs/en/interactive-mode#side-questions-with-btw)]
* Usage-limit automatic continue still asks for permissions, and stops after three continuations with a notification. Use `/rate-limit-options` to choose next steps. [[lines 754-756](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/interactive-mode.md?plain=1#L754-L756)] [[Source](https://code.claude.com/docs/en/interactive-mode#wait-for-a-usage-limit-to-reset)]

#### [jetbrains](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/jetbrains.md) [[Source](https://code.claude.com/docs/en/jetbrains)]

* Note that the JetBrains Marketplace is third-party software that Anthropic doesn't endorse, maintain or audit. [[line 38](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/jetbrains.md?plain=1#L38)] [[Source](https://code.claude.com/docs/en/jetbrains#installation)]

#### [llm-gateway-protocol](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/llm-gateway-protocol.md) [[Source](https://code.claude.com/docs/en/llm-gateway-protocol)]

* Retry behavior for rejected capabilities: advisor tool, `output_config.effort` and `context_management`. [[lines 236-241](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/llm-gateway-protocol.md?plain=1#L236-L241)] [[Source](https://code.claude.com/docs/en/llm-gateway-protocol#automatic-retry-and-error-forwarding)]
* New "Retry without a rejected beta value" section: which error message forms (`Unexpected value(s)` or a `beta_header:` token) trigger the retry. [[lines 249-272](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/llm-gateway-protocol.md?plain=1#L249-L272)] [[Source](https://code.claude.com/docs/en/llm-gateway-protocol#retry-without-a-rejected-beta-value)]
* New "How long a rejected beta value stays out" table. [[lines 249-272](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/llm-gateway-protocol.md?plain=1#L249-L272)] [[Source](https://code.claude.com/docs/en/llm-gateway-protocol#retry-without-a-rejected-beta-value)]
* Tool search retry on v2.1.305+ after a `400` or `422`. [[lines 275-277](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/llm-gateway-protocol.md?plain=1#L275-L277)] [[Source](https://code.claude.com/docs/en/llm-gateway-protocol#retry-without-tool-search)]

#### [llm-gateway-rollout](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/llm-gateway-rollout.md) [[Source](https://code.claude.com/docs/en/llm-gateway-rollout)]

* `ANTHROPIC_MODEL` and `ANTHROPIC_DEFAULT_HAIKU_MODEL` control which model name is requested for the main session and background traffic. [[line 165](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/llm-gateway-rollout.md?plain=1#L165)] [[Source](https://code.claude.com/docs/en/llm-gateway-rollout#what-to-distribute)]

#### [managed-settings](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/managed-settings.md) [[Source](https://code.claude.com/docs/en/managed-settings)]

* `useAutoModeDuringPlan`, `syncClaudeAiSkills` and `syncClaudeAiPlugins` are deny-only cross-source keys. A `false` from any admin, user or local source turns the behavior off. [[line 170](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/managed-settings.md?plain=1#L170)] [[Source](https://code.claude.com/docs/en/managed-settings#keys-read-from-every-admin-source)]

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* How Claude Code reconnects after an MCP OAuth server returns `401`, with and without a refresh token. [[line 951](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/mcp.md?plain=1#L951)] [[Source](https://code.claude.com/docs/en/mcp#authenticate-with-remote-mcp-servers)]
* New section on answering MCP elicitation requests in a cloud session, in form or URL mode. [[lines 1657-1667](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/mcp.md?plain=1#L1657-L1667)] [[Source](https://code.claude.com/docs/en/mcp#answer-an-elicitation-request-in-a-cloud-session)]
* Tool search through a gateway: expected forwarding of `defer_loading` fields and the v2.1.305+ automatic retry. [[lines 1830-1832](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/mcp.md?plain=1#L1830-L1832)] [[Source](https://code.claude.com/docs/en/mcp#tool-search-through-an-llm-gateway)]

#### [memory](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/memory.md) [[Source](https://code.claude.com/docs/en/memory)]

* Same path-scoped rule loading and glob table updates as claude-md. [[lines 205-222](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/memory.md?plain=1#L205-L222)] [[Source](https://code.claude.com/docs/en/memory#path-specific-rules)]

#### [model-config](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* `ANTHROPIC_DEFAULT_HAIKU_MODEL` is also used for background functionality. [[line 932](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/model-config.md?plain=1#L932)] [[Source](https://code.claude.com/docs/en/model-config#environment-variables)]

#### [network-config](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/network-config.md) [[Source](https://code.claude.com/docs/en/network-config)]

* Which proxy and sign-in variables Claude Code reads from settings files in Claude Desktop sessions, and how conflicts with the launch environment are handled. [[lines 130-135](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/network-config.md?plain=1#L130-L135)] [[Source](https://code.claude.com/docs/en/network-config#mtls-authentication)]

#### [permission-modes](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/permission-modes.md) [[Source](https://code.claude.com/docs/en/permission-modes)]

* New answer option "No, and block reads outside the working directories from now on", which sets `permissions.blockReadsOutsideWorkingDirectories` to `true`. [[line 531](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/permission-modes.md?plain=1#L531)] [[Source](https://code.claude.com/docs/en/permission-modes#the-first-read-outside-the-working-directories)]

#### [plugins/mods/api](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/plugins/mods/api.md) [[Source](https://code.claude.com/docs/en/plugins/mods/api)]

* Timers stop on module reload. `next.signal` is an `AbortSignal` for long-running work in a hook. [[line 255](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/plugins/mods/api.md?plain=1#L255)] [[Source](https://code.claude.com/docs/en/plugins/mods/api#stop-background-work)]

#### [plugins/mods/interface](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/plugins/mods/interface.md) [[Source](https://code.claude.com/docs/en/plugins/mods/interface)]

* The `ui.render` hook runs once a second, and its timer stops on module reload. [[line 737](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/plugins/mods/interface.md?plain=1#L737)] [[Source](https://code.claude.com/docs/en/plugins/mods/interface#redraw-on-a-timer)]

#### [remote-control](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/remote-control.md) [[Source](https://code.claude.com/docs/en/remote-control)]

* Clarified server mode behavior and the QR code toggle (spacebar) in `claude remote-control`. [[lines 50-151](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/remote-control.md?plain=1#L50-L151)] [[Source](https://code.claude.com/docs/en/remote-control#start-a-remote-control-session)]

#### [routines](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/routines.md) [[Source](https://code.claude.com/docs/en/routines)]

* After selecting a repository, a **Cloud environment** picker appears. [[line 104](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/routines.md?plain=1#L104)] [[Source](https://code.claude.com/docs/en/routines#create-from-the-web)]

#### [sandboxing](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/sandboxing.md) [[Source](https://code.claude.com/docs/en/sandboxing)]

* New limitation: services listed in `network.allowMachLookup` on macOS can act outside the sandbox. [[line 1073](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/sandboxing.md?plain=1#L1073)] [[Source](https://code.claude.com/docs/en/sandboxing#security-limitations)]

#### [settings-reference](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/settings-reference.md) [[Source](https://code.claude.com/docs/en/settings-reference)]

* `useAutoModeDuringPlan`: a `false` in any source turns it off, and `true` equals unset. [[lines 924-926](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/settings-reference.md?plain=1#L924-L926)] [[Source](https://code.claude.com/docs/en/settings-reference#useautomodeduringplan)]
* To lift `permissions.blockReadsOutsideWorkingDirectories`, remove the key from every settings file and restart sessions. [[line 1063](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/settings-reference.md?plain=1#L1063)] [[Source](https://code.claude.com/docs/en/settings-reference#permissionsblockreadsoutsideworkingdirectories)]
* `network.allowMachLookup` now describes XPC/Mach lookups, such as the iOS Simulator or Playwright, and the sandbox caveat. [[line 2073](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/settings-reference.md?plain=1#L2073)] [[Source](https://code.claude.com/docs/en/settings-reference#sandboxnetworkallowmachlookup)]
* Claude.ai sign-in variables are ignored in `env` from project settings. [[line 2422](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/settings-reference.md?plain=1#L2422)] [[Source](https://code.claude.com/docs/en/settings-reference#variables-claude-code-ignores-in-env)]
* Idle compaction doesn't run where feature flags can't be fetched on versions before v2.1.314. [[line 2491](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/settings-reference.md?plain=1#L2491)] [[Source](https://code.claude.com/docs/en/settings-reference#idlecompaction)]

#### [settings](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* Removing `permissions.blockReadsOutsideWorkingDirectories` mid-session doesn't lift the block in running sessions. [[line 183](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/settings.md?plain=1#L183)] [[Source](https://code.claude.com/docs/en/settings#when-edits-take-effect)]
* `useAutoModeDuringPlan` added to the restrictive cross-source keys table. [[line 312](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/settings.md?plain=1#L312)] [[Source](https://code.claude.com/docs/en/settings#exceptions-to-managed-settings-precedence)]

#### [sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* Use `/btw` instead of a subagent for questions about your existing conversation. [[line 1047](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/sub-agents.md?plain=1#L1047)] [[Source](https://code.claude.com/docs/en/sub-agents#choose-between-subagents-and-main-conversation)]
* With a subagent transcript open, messages and skills go to that agent and `/btw` answers from its transcript (v2.1.314+). [[line 1241](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/sub-agents.md?plain=1#L1241)] [[Source](https://code.claude.com/docs/en/sub-agents#observe-and-steer-running-forks)]

#### [tools-reference](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/tools-reference.md) [[Source](https://code.claude.com/docs/en/tools-reference)]

* EnterWorktree `path` may name a worktree of a repository nested inside the current one. [[line 302](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/tools-reference.md?plain=1#L302)] [[Source](https://code.claude.com/docs/en/tools-reference#enterworktree-tool-behavior)]

#### [web-scheduled-tasks](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/web-scheduled-tasks.md) [[Source](https://code.claude.com/docs/en/web-scheduled-tasks)]

* After selecting a repository, a **Cloud environment** picker appears. [[line 104](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/claude-code/web-scheduled-tasks.md?plain=1#L104)] [[Source](https://code.claude.com/docs/en/web-scheduled-tasks#create-from-the-web)]

-----

## API changes

### New Documents

None.

### Changed documents

#### [agents-and-tools/tool-use/browser-use-sdk](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/api/agents-and-tools/tool-use/browser-use-sdk.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-sdk)]

* Now in beta on Claude Platform on AWS, Amazon Bedrock and Microsoft Foundry. [[lines 23-26](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/api/agents-and-tools/tool-use/browser-use-sdk.md?plain=1#L23-L26)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-sdk#a-mybrowser-that-also-implements-read_console)]
* On other platforms, create that platform's SDK client instead of the Claude API one. [[line 86](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/api/agents-and-tools/tool-use/browser-use-sdk.md?plain=1#L86)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-sdk#use-a-driver-from-a-provider)]
* Availability table split by platform. [[line 1331](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/api/agents-and-tools/tool-use/browser-use-sdk.md?plain=1#L1331)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-sdk#messages-api)]

#### [agents-and-tools/tool-use/browser-use-tool](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/api/agents-and-tools/tool-use/browser-use-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool)]

* Now stable on Claude Platform on AWS, Amazon Bedrock and Microsoft Foundry. Add one `browser_toolset_20260801` entry, with no `name`, to `tools`. [[lines 26-44](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/api/agents-and-tools/tool-use/browser-use-tool.md?plain=1#L26-L44)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool#placeholder-image-data-a-real-executor-captures-the-viewport-and-returns-the-png-bytes)]
* Availability table split by platform. [[line 1595](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/api/agents-and-tools/tool-use/browser-use-tool.md?plain=1#L1595)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool#messages-api)]

#### [agents-and-tools/tool-use/computer-use-tool](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/api/agents-and-tools/tool-use/computer-use-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool)]

* Computer use is stable on Claude Platform on AWS, Amazon Bedrock and Microsoft Foundry. [[lines 32-36](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/api/agents-and-tools/tool-use/computer-use-tool.md?plain=1#L32-L36)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool#run-the-computer-use-agent-loop-until-claude-stops-requesting-tools)]
* Claude 5.5 and later models use `computer_toolset_20260801` and return a 400 for any computer use tool version they don't accept. [[line 38](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/api/agents-and-tools/tool-use/computer-use-tool.md?plain=1#L38)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool#run-the-computer-use-agent-loop-until-claude-stops-requesting-tools)]
* New guidance for upgrading a `computer_20251124` integration before moving to a model that doesn't accept it. [[lines 2070-2130](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/api/agents-and-tools/tool-use/computer-use-tool.md?plain=1#L2070-L2130)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool#migrate-from-computer_20251124)]
* Earlier tool versions and beta headers reorganized. On Bedrock, Opus 5.5, Sonnet 5.5 and Haiku 5.5 also accept `computer_20251124` with `computer-use-2025-11-24`. [[lines 2134-2137](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/api/agents-and-tools/tool-use/computer-use-tool.md?plain=1#L2134-L2137)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool#earlier-tool-versions)]

#### [api/errors](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/api/api/errors.md) [[Source](https://platform.claude.com/docs/en/api/errors)]

* Claude 5.5 models return a 400 for unsupported computer use tool versions. The same message appears for any unsupported Anthropic-defined tool type. [[lines 525-533](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/api/api/errors.md?plain=1#L525-L533)] [[Source](https://platform.claude.com/docs/en/api/errors#computer-use-tool-version-not-supported)]

#### [api/ip-addresses](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/api/api/ip-addresses.md) [[Source](https://platform.claude.com/docs/en/api/ip-addresses)]

* Added inbound range `153.61.224.0/22` and outbound range `153.61.208.0/20`. [[lines 19-33](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/api/api/ip-addresses.md?plain=1#L19-L33)] [[Source](https://platform.claude.com/docs/en/api/ip-addresses#ipv4)]

#### [build-with-claude/claude-in-amazon-bedrock](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/api/build-with-claude/claude-in-amazon-bedrock.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock)]

* Tool use list now includes the Browser use and Computer use tools. [[line 354](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/api/build-with-claude/claude-in-amazon-bedrock.md?plain=1#L354)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock#supported-feature-highlights)]

#### [build-with-claude/claude-on-amazon-bedrock-legacy](https://github.com/gpambrozo/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/api/build-with-claude/claude-on-amazon-bedrock-legacy.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy)]

* New "Computer use and browser use toolsets on Bedrock" section: available through InvokeModel on several models, with no beta header. [[line 724](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/api/build-with-claude/claude-on-amazon-bedrock-legacy.md?plain=1#L724)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy#features-not-supported)]

#### [build-with-claude/claude-platform-on-aws](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/api/build-with-claude/claude-platform-on-aws.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws)]

* All tool use capabilities are now listed as available. [[line 531](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/api/build-with-claude/claude-platform-on-aws.md?plain=1#L531)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws#feature-support)]

#### [build-with-claude/prompt-engineering/prompting-claude-opus-4-8](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/api/build-with-claude/prompt-engineering/prompting-claude-opus-4-8.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-4-8)]

* Notes support for `computer_toolset_20260801`, `computer_20251124` and the browser use tool. [[line 158](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/api/build-with-claude/prompt-engineering/prompting-claude-opus-4-8.md?plain=1#L158)] [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-4-8#computer-use)]

#### [build-with-claude/prompt-engineering/prompting-claude-sonnet-5](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/api/build-with-claude/prompt-engineering/prompting-claude-sonnet-5.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5)]

* Notes support for `computer_toolset_20260801`, `computer_20251124` and the browser use tool. [[line 152](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/api/build-with-claude/prompt-engineering/prompting-claude-sonnet-5.md?plain=1#L152)] [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5#computer-use)]

#### [cli-sdks-libraries/cli/apply](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/api/cli-sdks-libraries/cli/apply.md) [[Source](https://platform.claude.com/docs/en/cli-sdks-libraries/cli/apply)]

* Agent YAML examples disable `web_search` and `web_fetch` through tool `configs`. [[lines 112-204](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/api/cli-sdks-libraries/cli/apply.md?plain=1#L112-L204)] [[Source](https://platform.claude.com/docs/en/cli-sdks-libraries/cli/apply#grow-it-into-a-project)]

#### [cli-sdks-libraries/cli/using](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/api/cli-sdks-libraries/cli/using.md) [[Source](https://platform.claude.com/docs/en/cli-sdks-libraries/cli/using)]

* Explains inlining a file into a string field of a stdin document with an `@`-prefixed, quoted path, and updated structured flag examples. [[lines 151-160](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/api/cli-sdks-libraries/cli/using.md?plain=1#L151-L160)] [[Source](https://platform.claude.com/docs/en/cli-sdks-libraries/cli/using#file-references)]

#### [manage-claude/cmek-coverage-claude-enterprise](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/api/manage-claude/cmek-coverage-claude-enterprise.md) [[Source](https://platform.claude.com/docs/en/manage-claude/cmek-coverage-claude-enterprise)]

* Claude Security (beta) and cloud scheduled tasks (formerly routines) are listed as off under CMEK. [[line 42](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/api/manage-claude/cmek-coverage-claude-enterprise.md?plain=1#L42)] [[Source](https://platform.claude.com/docs/en/manage-claude/cmek-coverage-claude-enterprise#turned-off-or-changed)]

#### [manage-claude/compliance-content-data](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/api/manage-claude/compliance-content-data.md) [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-content-data)]

* Message example adds `claude_file_` entries. Documents `files`, `generated_files` and `artifacts`, and says to pick the endpoint by ID prefix. [[lines 147-178](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/api/manage-claude/compliance-content-data.md?plain=1#L147-L178)] [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-content-data#retrieve-chats-and-messages)]
* File downloads always use the RFC 5987 `filename*` form in `Content-Disposition`. curl's `-J` doesn't read it, so use `--output`. [[lines 195-208](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/api/manage-claude/compliance-content-data.md?plain=1#L195-L208)] [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-content-data#retrieve-files-and-artifacts)]

#### [manage-claude/compliance-errors](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/api/manage-claude/compliance-errors.md) [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-errors)]

* New "Invalid file ID" error, caused by sending an ID to an endpoint that expects a different prefix. [[line 135](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/api/manage-claude/compliance-errors.md?plain=1#L135)] [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-errors#invalid-file-id)]

#### [manage-claude/compliance-faq](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/api/manage-claude/compliance-faq.md) [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-faq)]

* Local session capture covers only requests that reach the Claude API. No endpoint lists Cowork scheduled tasks or Claude Code cloud scheduled tasks. [[lines 73-112](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/api/manage-claude/compliance-faq.md?plain=1#L73-L112)] [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-faq#data-coverage-and-retention)]

#### [manage-claude/compliance-sessions](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/api/manage-claude/compliance-sessions.md) [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-sessions)]

* Claude Code cloud sessions, including cloud scheduled tasks, are listed as captured sessions. [[line 36](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/api/manage-claude/compliance-sessions.md?plain=1#L36)] [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-sessions#compliance-sessions)]

#### [manage-claude/inference-hooks-configuration](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/api/manage-claude/inference-hooks-configuration.md) [[Source](https://platform.claude.com/docs/en/manage-claude/inference-hooks-configuration)]

* Changes to **Inspect** and the inspected roles are recorded in the Activity Feed. [[line 124](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/api/manage-claude/inference-hooks-configuration.md?plain=1#L124)] [[Source](https://platform.claude.com/docs/en/manage-claude/inference-hooks-configuration#inspect-only-selected-roles)]

#### [managed-agents/github](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/api/managed-agents/github.md) [[Source](https://platform.claude.com/docs/en/managed-agents/github)]

* Agent creation examples in every SDK now add an `agent_toolset_20260401` with `web_search` and `web_fetch` disabled, and use Opus 5.5. [[lines 66-294](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/api/managed-agents/github.md?plain=1#L66-L294)] [[Source](https://platform.claude.com/docs/en/managed-agents/github#github-mcp-and-session-resources)]

#### [managed-agents/multiagent-orchestration](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/api/managed-agents/multiagent-orchestration.md) [[Source](https://platform.claude.com/docs/en/managed-agents/multiagent-orchestration)]

* The contract review example now disables web search and web fetch, since reviewing contracts doesn't use the web. [[lines 849-965](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/api/managed-agents/multiagent-orchestration.md?plain=1#L849-L965)] [[Source](https://platform.claude.com/docs/en/managed-agents/multiagent-orchestration#turn-on-dynamic-workflows)]

#### [managed-agents/quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/api/managed-agents/quickstart.md) [[Source](https://platform.claude.com/docs/en/managed-agents/quickstart)]

* Quickstart examples now configure the agent toolset with web search and web fetch disabled.

#### [managed-agents/self-hosted-sandboxes-custom-tools](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/api/managed-agents/self-hosted-sandboxes-custom-tools.md) [[Source](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-custom-tools)]

* Agent examples in all SDKs now disable `web_search` and `web_fetch` alongside custom tools. [[lines 259-630](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/api/managed-agents/self-hosted-sandboxes-custom-tools.md?plain=1#L259-L630)] [[Source](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-custom-tools#declare-and-serve-the-tools)]

#### [managed-agents/tools](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/api/managed-agents/tools.md) [[Source](https://platform.claude.com/docs/en/managed-agents/tools)]

* The custom tool example now creates an agent with one custom tool, `get_weather`, and no built-in tools. PHP and Ruby examples use the Opus 5.5 model constant. [[lines 189-462](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/api/managed-agents/tools.md?plain=1#L189-L462)] [[Source](https://platform.claude.com/docs/en/managed-agents/tools#configuring-the-toolset)]

#### [models/haiku-5-5/whats-new-haiku-5-5](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/api/models/haiku-5-5/whats-new-haiku-5-5.md) [[Source](https://platform.claude.com/docs/en/models/haiku-5-5/whats-new-haiku-5-5)]

* The change table adds the browser use tool and a breaking change: `computer_20250124` now returns an error, so use `computer_toolset_20260801` (`computer_20251124` also works on Bedrock). [[lines 17-34](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/api/models/haiku-5-5/whats-new-haiku-5-5.md?plain=1#L17-L34)] [[Source](https://platform.claude.com/docs/en/models/haiku-5-5/whats-new-haiku-5-5#summary-of-changes-from-claude-haiku-45)]

#### [models/opus-5-5/overview](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/api/models/opus-5-5/overview.md) [[Source](https://platform.claude.com/docs/en/models/opus-5-5/overview)]

* Summarizes Opus 5.5 as built for long-running agentic coding and knowledge work, and lists breaking changes compared with Opus 5. [[line 21](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/api/models/opus-5-5/overview.md?plain=1#L21)] [[Source](https://platform.claude.com/docs/en/models/opus-5-5/overview#overview)]

#### [models/opus-5-5/migration-guide, whats-new-opus-5-5; models/sonnet-5-5/migration-guide, overview, whats-new-sonnet-5-5; models/haiku-5-5/migration-guide](https://github.com/gpambrozio/ClaudeDocs/blob/7f18f0fb515a154b6908d82d05beda57aa5206a8/docs-md/api/models/opus-5-5/migration-guide.md) [[Source](https://platform.claude.com/docs/en/models/opus-5-5/migration-guide)]

* Migration guides and what's new pages for the 5.5 models gain computer use toolset migration notes (`computer_toolset_20260801`).
