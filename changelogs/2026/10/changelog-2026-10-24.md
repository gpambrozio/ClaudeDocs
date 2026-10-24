# [Claude docs changes for October 24th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/05a393cec14b210835e9a32bb06ef13762e8b314) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/05a393cec14b210835e9a32bb06ef13762e8b314)]

## Executive Summary
- New Claude Tag API (beta) lets Claude Enterprise admins manage Claude Tag Slack channels, workspaces and Access bundles programmatically
- MCP tasks documentation: long-running server-side MCP jobs, with new sections for users and for server authors
- Desktop can now build SSH connections from a command, and the docs add troubleshooting for exported environment variables
- Claude Code 2.1.310 brings the Monitor tool to Bedrock, Vertex and Foundry, plus new cloud-session permissions for Enterprise custom roles
- API SDKs document OpenTelemetry tracing and PHP middleware; `ant apply` gets glob support and a full GitHub Actions workflow

## New Claude Code versions

### [2.1.310](https://github.com/gpambrozio/ClaudeDocs/blob/05a393cec14b210835e9a32bb06ef13762e8b314/versions/2.1.310.md)

#### New features

* Monitor tool and plugin monitors now work on Bedrock, Vertex, and Foundry, and when telemetry or nonessential traffic is disabled; long foreground sleeps are blocked there too
* [Cloud sessions] Claude Code cloud sessions and Remote Control permissions added to Enterprise custom roles
* [Cloud sessions] "Choose file" button to load a cloud environment's setup script from a file

#### Existing feature improvements

* Auto mode's prompt before the first read outside the working directories now says when blocking those reads makes shell commands ask for permission
* Lower memory use in non-interactive sessions (`-p`, Agent SDK) during compaction with very large transcripts
* A mod's `Image` now draws inside tmux (with `allow-passthrough` and `focus-events`), kitty, Ghostty, and iTerm2 3.5+
* Linux: `/sandbox` and the startup warning name Ubuntu's AppArmor user-namespace restriction and how to lift it
* An MCP tool call that times out in a non-interactive session with an unanswered elicitation now tells Claude no answer came and not to repeat the call
* [Cloud sessions] Session start checklist shows setup script output in a scrolling box; the environment dialog opens network access, setup script and variables from rows; enabling Cloud sessions or Remote Control in admin settings asks for confirmation and lists affected custom roles

#### Major bug fixes

* Fixed requests failing behind gateways that reject the `effort-2025-11-24` beta value or mid-conversation system messages (Claude Code now retries without them)
* Fixed background cleanup deleting recent files such as pasted images when `cleanupPeriodDays` is very large
* Fixed compaction after a "Prompt is too long" error keeping too much dense text (base64, SVG), which could make the next request fail again
* Fixed file read permission prompts not showing where a symbolic link leads
* Windows: fixed PreToolUse and PermissionRequest hooks letting a tool call through when Git Bash is missing and the hook command is only quoted strings
* [VSCode] Fixed Enter on "Send feedback and keep planning" approving the plan instead of sending comments back

-----

## Claude Code changes

### New Documents

None. Most of the 300+ other files in this commit only had in-site links rewritten to absolute URLs.

### Changed documents

#### [desktop](https://github.com/gpambrozio/ClaudeDocs/blob/05a393cec14b210835e9a32bb06ef13762e8b314/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)]

* New section on creating an SSH connection from a command (writing the command, connecting to a new host, replacing the host, distributing commands to your team, and troubleshooting a missing or gray command). [[lines 1521-1670](https://github.com/gpambrozio/ClaudeDocs/blob/05a393cec14b210835e9a32bb06ef13762e8b314/docs-md/claude-code/desktop.md?plain=1#L1521-L1670)] [[Source](https://code.claude.com/docs/en/desktop#create-an-ssh-connection-from-a-command)]
* Local environment variables section renamed and expanded with a table of what to do for variables such as `PATH` and `CLAUDE_CONFIG_DIR`. [[lines 830-843](https://github.com/gpambrozio/ClaudeDocs/blob/05a393cec14b210835e9a32bb06ef13762e8b314/docs-md/claude-code/desktop.md?plain=1#L830-L843)] [[Source](https://code.claude.com/docs/en/desktop#environment-variables-in-local-sessions)]
* New troubleshooting steps for an exported variable that is missing or wrong in commands Claude runs on macOS or Linux. [[lines 889-910](https://github.com/gpambrozio/ClaudeDocs/blob/05a393cec14b210835e9a32bb06ef13762e8b314/docs-md/claude-code/desktop.md?plain=1#L889-L910)] [[Source](https://code.claude.com/docs/en/desktop#exported-variable-missing-or-wrong-in-commands-claude-runs)]

#### [desktop-changelog](https://github.com/gpambrozio/ClaudeDocs/blob/05a393cec14b210835e9a32bb06ef13762e8b314/docs-md/claude-code/desktop-changelog.md) [[Source](https://code.claude.com/docs/en/desktop-changelog)]

* Carries the same content changes as `desktop` (SSH connection from a command, local environment variable guidance). [[line 1521](https://github.com/gpambrozio/ClaudeDocs/blob/05a393cec14b210835e9a32bb06ef13762e8b314/docs-md/claude-code/desktop-changelog.md?plain=1#L1521)] [[Source](https://code.claude.com/docs/en/desktop-changelog#create-an-ssh-connection-from-a-command)]

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/05a393cec14b210835e9a32bb06ef13762e8b314/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS` is now described precisely: it removes `run_in_background` from the Bash, PowerShell, and subagent tools, turns off Ctrl+B, and stops background runs of forked skills. [[line 232](https://github.com/gpambrozio/ClaudeDocs/blob/05a393cec14b210835e9a32bb06ef13762e8b314/docs-md/claude-code/env-vars.md?plain=1#L232)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/05a393cec14b210835e9a32bb06ef13762e8b314/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* New entry for "MCP tool call timed out with the server's question unanswered" in non-interactive mode, with the new message text and fixes (Elicitation hook, `onElicitation`, longer `timeout`). Applies from v2.1.310. [[lines 4417-4435](https://github.com/gpambrozio/ClaudeDocs/blob/05a393cec14b210835e9a32bb06ef13762e8b314/docs-md/claude-code/errors.md?plain=1#L4417-L4435)] [[Source](https://code.claude.com/docs/en/errors#mcp-server-connection-closed-before-the-tool-call-was-answered)]

#### [headless](https://github.com/gpambrozio/ClaudeDocs/blob/05a393cec14b210835e9a32bb06ef13762e8b314/docs-md/claude-code/headless.md) [[Source](https://code.claude.com/docs/en/headless)]

* New section: a `claude -p` run doesn't wait for MCP tasks (which continue on remote servers and can be followed by resuming the session) and loses results of auto-backgrounded MCP calls. [[lines 88-94](https://github.com/gpambrozio/ClaudeDocs/blob/05a393cec14b210835e9a32bb06ef13762e8b314/docs-md/claude-code/headless.md?plain=1#L88-L94)] [[Source](https://code.claude.com/docs/en/headless#mcp-work-when-a-non-interactive-run-ends)]

#### [ide-integrations](https://github.com/gpambrozio/ClaudeDocs/blob/05a393cec14b210835e9a32bb06ef13762e8b314/docs-md/claude-code/ide-integrations.md) [[Source](https://code.claude.com/docs/en/ide-integrations)]

* Certificate-error troubleshooting: a log warning naming an untrusted authority points to `NODE_EXTRA_CA_CERTS` behind TLS-inspecting proxies; remote windows (WSL, SSH, dev containers) must edit settings on the remote system. [[lines 1007-1014](https://github.com/gpambrozio/ClaudeDocs/blob/05a393cec14b210835e9a32bb06ef13762e8b314/docs-md/claude-code/ide-integrations.md?plain=1#L1007-L1014)] [[Source](https://code.claude.com/docs/en/ide-integrations#dictation-or-the-web-tab-fails-behind-a-tls-inspecting-proxy)]

#### [jetbrains](https://github.com/gpambrozio/ClaudeDocs/blob/05a393cec14b210835e9a32bb06ef13762e8b314/docs-md/claude-code/jetbrains.md) [[Source](https://code.claude.com/docs/en/jetbrains)]

* Removed the statement that `/ide` installs the plugin for a running IDE that lacks it. [[line 60](https://github.com/gpambrozio/ClaudeDocs/blob/05a393cec14b210835e9a32bb06ef13762e8b314/docs-md/claude-code/jetbrains.md?plain=1#L60)] [[Source](https://code.claude.com/docs/en/jetbrains#connect-from-an-external-terminal)]

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/05a393cec14b210835e9a32bb06ef13762e8b314/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* New "Time limits on MCP tool calls" section covering per-server `timeout` and `MCP_TOOL_TIMEOUT`. [[line 434](https://github.com/gpambrozio/ClaudeDocs/blob/05a393cec14b210835e9a32bb06ef13762e8b314/docs-md/claude-code/mcp.md?plain=1#L434)] [[Source](https://code.claude.com/docs/en/mcp#time-limits-on-mcp-tool-calls)]
* Large new section on MCP tasks that run on the server (public beta, v2.1.304+): stopping a task or getting its result, answering a task's questions, exit/clear/resume behavior, requirements, status messages, time limits, and making Claude wait. [[lines 474-634](https://github.com/gpambrozio/ClaudeDocs/blob/05a393cec14b210835e9a32bb06ef13762e8b314/docs-md/claude-code/mcp.md?plain=1#L474-L634)] [[Source](https://code.claude.com/docs/en/mcp#mcp-tasks-that-run-on-the-server)]
* New guidance for MCP server authors on answering a call with a task and reporting status, results, and questions. [[lines 474-634](https://github.com/gpambrozio/ClaudeDocs/blob/05a393cec14b210835e9a32bb06ef13762e8b314/docs-md/claude-code/mcp.md?plain=1#L474-L634)] [[Source](https://code.claude.com/docs/en/mcp#mcp-tasks-that-run-on-the-server)]

#### [monitoring-usage](https://github.com/gpambrozio/ClaudeDocs/blob/05a393cec14b210835e9a32bb06ef13762e8b314/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* New `agent_id` and `parent_agent_id` event attributes identifying the subagent that raised an event (v2.1.310+). [[line 606](https://github.com/gpambrozio/ClaudeDocs/blob/05a393cec14b210835e9a32bb06ef13762e8b314/docs-md/claude-code/monitoring-usage.md?plain=1#L606)] [[Source](https://code.claude.com/docs/en/monitoring-usage#standard-attributes)]
* The order in which the OpenTelemetry SDK drops `tool_decision` attributes under a low attribute-count limit is now an explicit list including the new attributes and `request_id`. [[lines 1027-1036](https://github.com/gpambrozio/ClaudeDocs/blob/05a393cec14b210835e9a32bb06ef13762e8b314/docs-md/claude-code/monitoring-usage.md?plain=1#L1027-L1036)] [[Source](https://code.claude.com/docs/en/monitoring-usage#tool-decision-event)]

#### [self-hosted-environments-reference](https://github.com/gpambrozio/ClaudeDocs/blob/05a393cec14b210835e9a32bb06ef13762e8b314/docs-md/claude-code/self-hosted-environments-reference.md) [[Source](https://code.claude.com/docs/en/self-hosted-environments-reference)]

* New Prometheus alert rules: `ClaudeRunnersBelowFloor` for fixed fleets, and `ClaudeOrchestratorSessionsWaiting` and `ClaudeOrchestratorQueueWaitHigh` for on-demand runners, with tuning notes. [[lines 305-364](https://github.com/gpambrozio/ClaudeDocs/blob/05a393cec14b210835e9a32bb06ef13762e8b314/docs-md/claude-code/self-hosted-environments-reference.md?plain=1#L305-L364)] [[Source](https://code.claude.com/docs/en/self-hosted-environments-reference#alert-on-lost-runners-and-waiting-sessions)]

#### [settings-reference](https://github.com/gpambrozio/ClaudeDocs/blob/05a393cec14b210835e9a32bb06ef13762e8b314/docs-md/claude-code/settings-reference.md) [[Source](https://code.claude.com/docs/en/settings-reference)]

* New `sshHostCommands` setting that adds Desktop SSH connections whose host comes from a command (user or managed scope, with an example). [[lines 4999-5021](https://github.com/gpambrozio/ClaudeDocs/blob/05a393cec14b210835e9a32bb06ef13762e8b314/docs-md/claude-code/settings-reference.md?plain=1#L4999-L5021)] [[Source](https://code.claude.com/docs/en/settings-reference#sshhostcommands)]

#### [vs-code](https://github.com/gpambrozio/ClaudeDocs/blob/05a393cec14b210835e9a32bb06ef13762e8b314/docs-md/claude-code/vs-code.md) [[Source](https://code.claude.com/docs/en/vs-code)]

* Same certificate-error troubleshooting additions as `ide-integrations` (log warning, `NODE_EXTRA_CA_CERTS`, remote-window note). [[lines 1007-1014](https://github.com/gpambrozio/ClaudeDocs/blob/05a393cec14b210835e9a32bb06ef13762e8b314/docs-md/claude-code/vs-code.md?plain=1#L1007-L1014)] [[Source](https://code.claude.com/docs/en/vs-code#dictation-or-the-web-tab-fails-behind-a-tls-inspecting-proxy)]

-----

## API changes

### New Documents

#### [claude-tag-api](https://github.com/gpambrozio/ClaudeDocs/blob/05a393cec14b210835e9a32bb06ef13762e8b314/docs-md/api/manage-claude/claude-tag-api.md) [[Source](https://platform.claude.com/docs/en/manage-claude/claude-tag-api)]

Documents the Claude Tag API (beta, Claude Enterprise only, header `anthropic-beta: experimental-claude-tag-2026-10-21`). Its 14 endpoints under `/v1/organizations/claude_tag/` cover Slack channels, Slack workspaces, Access bundles (read-only), and bundle targets. They read and change Claude Tag settings, show which settings apply to a channel and where each comes from, and attach or detach bundles. It requires an Admin API key with `read:claude_tag` or `write:claude_tag` scope, and is available through the SDKs and the `ant` CLI.

### Changed documents

#### [analytics-api](https://github.com/gpambrozio/ClaudeDocs/blob/05a393cec14b210835e9a32bb06ef13762e8b314/docs-md/api/manage-claude/analytics-api.md) [[Source](https://platform.claude.com/docs/en/manage-claude/analytics-api)]

* Chat and Cowork unified is no longer labeled beta. [[line 96](https://github.com/gpambrozio/ClaudeDocs/blob/05a393cec14b210835e9a32bb06ef13762e8b314/docs-md/api/manage-claude/analytics-api.md?plain=1#L96)] [[Source](https://platform.claude.com/docs/en/manage-claude/analytics-api#how-metrics-are-defined)]
* New section on Claude Code and Cowork with customer-managed encryption keys: lines of code, commit count, and slash-command skill use can be zero or undercounted. [[lines 128-140](https://github.com/gpambrozio/ClaudeDocs/blob/05a393cec14b210835e9a32bb06ef13762e8b314/docs-md/api/manage-claude/analytics-api.md?plain=1#L128-L140)] [[Source](https://platform.claude.com/docs/en/manage-claude/analytics-api#claude-code-through-amazon-bedrock)]

#### [apply](https://github.com/gpambrozio/ClaudeDocs/blob/05a393cec14b210835e9a32bb06ef13762e8b314/docs-md/api/cli-sdks-libraries/cli/apply.md) [[Source](https://platform.claude.com/docs/en/cli-sdks-libraries/cli/apply)]

* Paths can now be globs: under `skills`, a glob references every matching skill; under an agent's `tools`, files are inserted inline. [[lines 193-226](https://github.com/gpambrozio/ClaudeDocs/blob/05a393cec14b210835e9a32bb06ef13762e8b314/docs-md/api/cli-sdks-libraries/cli/apply.md?plain=1#L193-L226)] [[Source](https://platform.claude.com/docs/en/cli-sdks-libraries/cli/apply#grow-it-into-a-project)]
* Full GitHub Actions workflow for `ant apply` with OIDC identity token, lockfile commit, and concurrency control, replacing a link to the CLI README. [[lines 258-305](https://github.com/gpambrozio/ClaudeDocs/blob/05a393cec14b210835e9a32bb06ef13762e8b314/docs-md/api/cli-sdks-libraries/cli/apply.md?plain=1#L258-L305)] [[Source](https://platform.claude.com/docs/en/cli-sdks-libraries/cli/apply#run-ant-apply-in-ci)]

#### [cmek-aws-kms](https://github.com/gpambrozio/ClaudeDocs/blob/05a393cec14b210835e9a32bb06ef13762e8b314/docs-md/api/manage-claude/cmek-aws-kms.md) [[Source](https://platform.claude.com/docs/en/manage-claude/cmek-aws-kms)]

* The key may now be created in any AWS commercial region, not only a US region. [[line 86](https://github.com/gpambrozio/ClaudeDocs/blob/05a393cec14b210835e9a32bb06ef13762e8b314/docs-md/api/manage-claude/cmek-aws-kms.md?plain=1#L86)] [[Source](https://platform.claude.com/docs/en/manage-claude/cmek-aws-kms#create-the-key)]

#### [cmek-google-cloud-kms](https://github.com/gpambrozio/ClaudeDocs/blob/05a393cec14b210835e9a32bb06ef13762e8b314/docs-md/api/manage-claude/cmek-google-cloud-kms.md) [[Source](https://platform.claude.com/docs/en/manage-claude/cmek-google-cloud-kms)]

* Any Cloud KMS location may now be used. [[line 44](https://github.com/gpambrozio/ClaudeDocs/blob/05a393cec14b210835e9a32bb06ef13762e8b314/docs-md/api/manage-claude/cmek-google-cloud-kms.md?plain=1#L44)] [[Source](https://platform.claude.com/docs/en/manage-claude/cmek-google-cloud-kms#in-google-cloud-create-the-key)]

#### [middleware](https://github.com/gpambrozio/ClaudeDocs/blob/05a393cec14b210835e9a32bb06ef13762e8b314/docs-md/api/cli-sdks-libraries/middleware.md) [[Source](https://platform.claude.com/docs/en/cli-sdks-libraries/middleware)]

* Points to the new PHP-specific middleware section. [[line 150](https://github.com/gpambrozio/ClaudeDocs/blob/05a393cec14b210835e9a32bb06ef13762e8b314/docs-md/api/cli-sdks-libraries/middleware.md?plain=1#L150)] [[Source](https://platform.claude.com/docs/en/cli-sdks-libraries/middleware#registering-middleware)]

#### [opentelemetry](https://github.com/gpambrozio/ClaudeDocs/blob/05a393cec14b210835e9a32bb06ef13762e8b314/docs-md/api/manage-claude/opentelemetry.md) [[Source](https://platform.claude.com/docs/en/manage-claude/opentelemetry)] and [opentelemetry/sdk](https://github.com/gpambrozio/ClaudeDocs/blob/05a393cec14b210835e9a32bb06ef13762e8b314/docs-md/api/manage-claude/opentelemetry/sdk.md)

* Retitled to "OpenTelemetry tracing for the Claude API"; the SDK page now covers Python, TypeScript, C#, Go, Java, PHP, and Ruby. [[line 4](https://github.com/gpambrozio/ClaudeDocs/blob/05a393cec14b210835e9a32bb06ef13762e8b314/docs-md/api/manage-claude/opentelemetry.md?plain=1#L4)] [[Source](https://platform.claude.com/docs/en/manage-claude/opentelemetry#opentelemetry)]

#### [optimizing-for-cost-and-intelligence](https://github.com/gpambrozio/ClaudeDocs/blob/05a393cec14b210835e9a32bb06ef13762e8b314/docs-md/api/about-claude/models/optimizing-for-cost-and-intelligence.md) [[Source](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence)]

* Summary table of levers reworked (new "Saving" column wording, sources now include launch posts and published prices and speeds) and now includes rows such as Fast mode, Orchestrator, and Advisor. [[line 1051](https://github.com/gpambrozio/ClaudeDocs/blob/05a393cec14b210835e9a32bb06ef13762e8b314/docs-md/api/about-claude/models/optimizing-for-cost-and-intelligence.md?plain=1#L1051)] [[Source](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#benchmarks-referenced)]
* Added Claude Haiku 5.5 compaction-trigger pricing details; removed several "not measured" notes for Sonnet 5.5, Opus 5.5, and Managed Agents. [[lines 956-1008](https://github.com/gpambrozio/ClaudeDocs/blob/05a393cec14b210835e9a32bb06ef13762e8b314/docs-md/api/about-claude/models/optimizing-for-cost-and-intelligence.md?plain=1#L956-L1008)] [[Source](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#benchmarks-referenced)]

#### [release-notes/overview](https://github.com/gpambrozio/ClaudeDocs/blob/05a393cec14b210835e9a32bb06ef13762e8b314/docs-md/api/release-notes/overview.md) [[Source](https://platform.claude.com/docs/en/release-notes/overview)]

* New release note announcing the Claude Tag API beta. [[line 29](https://github.com/gpambrozio/ClaudeDocs/blob/05a393cec14b210835e9a32bb06ef13762e8b314/docs-md/api/release-notes/overview.md?plain=1#L29)] [[Source](https://platform.claude.com/docs/en/release-notes/overview#october-20-2026)]

#### [session-observability](https://github.com/gpambrozio/ClaudeDocs/blob/05a393cec14b210835e9a32bb06ef13762e8b314/docs-md/api/managed-agents/session-observability.md) [[Source](https://platform.claude.com/docs/en/managed-agents/session-observability)]

* Points to OpenTelemetry tracing for seeing a session's turns, model requests, and tool uses in your observability platform. [[line 15](https://github.com/gpambrozio/ClaudeDocs/blob/05a393cec14b210835e9a32bb06ef13762e8b314/docs-md/api/managed-agents/session-observability.md?plain=1#L15)] [[Source](https://platform.claude.com/docs/en/managed-agents/session-observability#session-observability)]

#### SDK pages: [csharp](https://github.com/gpambrozio/ClaudeDocs/blob/05a393cec14b210835e9a32bb06ef13762e8b314/docs-md/api/cli-sdks-libraries/sdks/csharp.md), [go](https://github.com/gpambrozio/ClaudeDocs/blob/05a393cec14b210835e9a32bb06ef13762e8b314/docs-md/api/cli-sdks-libraries/sdks/go.md), [java](https://github.com/gpambrozio/ClaudeDocs/blob/05a393cec14b210835e9a32bb06ef13762e8b314/docs-md/api/cli-sdks-libraries/sdks/java.md), [php](https://github.com/gpambrozio/ClaudeDocs/blob/05a393cec14b210835e9a32bb06ef13762e8b314/docs-md/api/cli-sdks-libraries/sdks/php.md), [python](https://github.com/gpambrozio/ClaudeDocs/blob/05a393cec14b210835e9a32bb06ef13762e8b314/docs-md/api/cli-sdks-libraries/sdks/python.md), [ruby](https://github.com/gpambrozio/ClaudeDocs/blob/05a393cec14b210835e9a32bb06ef13762e8b314/docs-md/api/cli-sdks-libraries/sdks/ruby.md), [typescript](https://github.com/gpambrozio/ClaudeDocs/blob/05a393cec14b210835e9a32bb06ef13762e8b314/docs-md/api/cli-sdks-libraries/sdks/typescript.md)

* Each SDK page gains an "OpenTelemetry tracing" section describing the per-request spans (C# requires `AddSource("com.anthropic.sdk.csharp*")`).
* PHP: new Middleware section covering middleware classes, the `RequestOptions` third argument, retries, error responses, exceptions, authentication, and response bodies. [[lines 217-250](https://github.com/gpambrozio/ClaudeDocs/blob/05a393cec14b210835e9a32bb06ef13762e8b314/docs-md/api/cli-sdks-libraries/sdks/php.md?plain=1#L217-L250)] [[Source](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/php#middleware)]
* Java SDK install snippets moved from 3.2.0 to 3.3.0 across the Bedrock, Foundry, Google Cloud, AWS, MCP connector, and get-started pages; `ant` CLI install examples moved from 2.2.0 to 2.3.0.

#### [streaming](https://github.com/gpambrozio/ClaudeDocs/blob/05a393cec14b210835e9a32bb06ef13762e8b314/docs-md/api/build-with-claude/streaming.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/streaming)]

* PHP example gains a comment showing where to call `$accumulator->message()` for a snapshot of the message so far. [[line 266](https://github.com/gpambrozio/ClaudeDocs/blob/05a393cec14b210835e9a32bb06ef13762e8b314/docs-md/api/build-with-claude/streaming.md?plain=1#L266)] [[Source](https://platform.claude.com/docs/en/build-with-claude/streaming#get-the-final-message-without-handling-events)]

#### API reference (`docs-md/api/api/...`)

* File upload parameters in the Files, Skills, plugins, and plugin-marketplace endpoints are now typed as files (`file`, `array of file`, `BinaryContent`, `InputStream`, and so on) instead of `string` across the HTTP, CLI, C#, Java and other language references.
