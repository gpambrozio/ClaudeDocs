# [Claude docs changes for October 15th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/ba5bc9af122d35723f67730a3dd53cfbd28113d4) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/ba5bc9af122d35723f67730a3dd53cfbd28113d4)]

## Executive Summary
- Claude Code 2.1.300 adds new mod hooks and APIs (`prompt.change`, `virtualText`, `$.ui.view({ agentId })`), OpenTelemetry GenAI span attributes, and a long list of fixes for worktrees, reftable repos, cloud sessions, and hooks.
- OpenTelemetry export for the Claude API and Managed Agents launched in beta. New guides cover SDK tracing, API tracing through a Console "destination", and a span reference. The Admin API also gains telemetry destination endpoints.
- Subagents can now set `autoCompactWindow` (100k to 1M tokens) in frontmatter, in the Agent SDK `AgentDefinition`, and for agent-team teammates.
- Claude Desktop SSH sessions got extensive new docs: proxy and CA setup, containers via `ProxyCommand`, AWS credentials, port forwarding, helper files and processes, fail2ban notes, and a troubleshooting table.
- New `CLAUDE_CODE_DISABLE_FILE_MENTIONS` setting stops `@` references from inlining file contents. Network secrets for cloud environments now cover Team and Enterprise plans.

## New Claude Code versions

### [2.1.300](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/versions/2.1.300.md)

#### New features

* Mods: added `virtualText` prompt decorations, `$.ui.view({ agentId })` to show an agent's transcript in the main view, a `dir` prop on `Text` for right-to-left text, and a `prompt.change` hook for non-typed prompt changes (history recall, clear, undo, plugin fill)
* The `agent.spawn` mod hook can now rewrite a workflow agent's `prompt` and `model`
* OpenTelemetry: `api_request` events now include `cache_creation_5m_tokens` and `cache_creation_1h_tokens`, and trace spans carry GenAI semantic-convention attributes (`gen_ai.provider.name`, `gen_ai.conversation.id`, `gen_ai.tool.name`, `error.type`)
* Added `/advisor` on Claude Platform on AWS (opt in with `/advisor`, `advisorModel` or `--advisor`; `CLAUDE_CODE_DISABLE_ADVISOR_TOOL=1` turns it off)
* VS Code: added the `claudeCode.attachSelection` setting to stop editor selections being added to messages
* Claude Tag: Slack Connect channel support (off by default), a private Allow once / Deny card for connector approvals, and Slack voice clip transcripts

#### Existing feature improvements

* Artifact updates: small changes are applied and republished in one call
* WebFetch in Cowork cloud sessions tells Claude that a page failed moments ago instead of refetching it
* Hook `updatedInput` from PreToolUse and PermissionRequest hooks is now validated like Claude's own input: unknown keys are dropped and rejected input denies the call
* Large requests to api.anthropic.com use gzip even with telemetry disabled (`CLAUDE_CODE_GZIP_REQUEST_BODIES=0` turns it off)
* Exit force-kills background commands still running after 1.5 seconds
* Local transcripts now record each API request's system prompt, tools and parameters
* `claude gateway` stops at start on a `desktop:` policy key Claude Desktop can't use from a gateway
* Removed the no-op `--sandbox` and `--no-sandbox` flags from `claude remote-control`; passing either now exits with an error

#### Major bug fixes

* Fixed agent hooks ignoring their `model` setting
* Fixed `--worktree` starting from the wrong commit, failing in bare-repo worktrees, and misbehaving in reftable repositories
* Fixed a conversation failing on every turn with a 400 when the API rejected an MCP tool's input schema
* Fixed resuming headless or Agent SDK sessions losing compaction summaries or recent messages
* Fixed SessionEnd hooks sometimes not running when exiting with a background command running
* Fixed automatic tool search turning off mid-conversation while MCP servers reconnect
* Fixed `claude daemon stop` reporting success while a stuck service kept running
* Fixed cloud sessions hanging 5 minutes per turn when the organization's policy can't be read, and several Remote Control and Cowork cloud session issues
* Fixed several VS Code issues, including fast mode staying on after credits ran out and drag-and-drop file mentions on Windows and WSL

-----

## Claude Code changes

### New Documents

None.

### Changed documents

#### [agent-sdk/modifying-system-prompts](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/agent-sdk/modifying-system-prompts.md) [[Source](https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts)]

* Clarified that most, not all, system reminders reach Claude with a custom `systemPrompt`. [[line 371](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/agent-sdk/modifying-system-prompts.md?plain=1#L371)] [[Source](https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts#context-claude-code-adds-outside-the-system-prompt)]
* `includeGitInstructions: false` keeps out the built-in commit and PR instructions. With the minimal default, a custom prompt, or a custom main-thread agent, the session starts without the git status snapshot. [[line 410](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/agent-sdk/modifying-system-prompts.md?plain=1#L410)] [[Source](https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts#turn-off-the-context-your-agent-replaces)]
* Documented `CLAUDE_CODE_DISABLE_FILE_MENTIONS=1` (v2.1.299+) to stop only `@` file mentions from expanding. [[line 412](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/agent-sdk/modifying-system-prompts.md?plain=1#L412)] [[Source](https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts#turn-off-the-context-your-agent-replaces)]

#### [agent-sdk/observability](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/agent-sdk/observability.md) [[Source](https://code.claude.com/docs/en/agent-sdk/observability)]

* Added a pointer to the new OpenTelemetry for the Claude API guide. [[line 16](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/agent-sdk/observability.md?plain=1#L16)] [[Source](https://code.claude.com/docs/en/agent-sdk/observability#observability-with-opentelemetry)]

#### [agent-sdk/subagents](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/agent-sdk/subagents.md) [[Source](https://code.claude.com/docs/en/agent-sdk/subagents)]

* New `autoCompactWindow` field on `AgentDefinition` (100000 to 1000000; TypeScript SDK v0.3.296+; not in Python). [[line 149](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/agent-sdk/subagents.md?plain=1#L149)] [[Source](https://code.claude.com/docs/en/agent-sdk/subagents#agentdefinition-configuration)]

#### [agent-sdk/typescript](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* Added `autoCompactWindow` to the `AgentDefinition` type and table. [[lines 1099-1120](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L1099-L1120)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#agentdefinition)]
* Peer message `body` is absent when several teammate messages are merged (behavior change in v2.1.299). [[line 2233](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L2233)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#peer-origin-fields)]

#### [agent-teams](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/agent-teams.md) [[Source](https://code.claude.com/docs/en/agent-teams)]

* In-process teammates apply the subagent definition's `autoCompactWindow`; split-pane teammates ignore it (v2.1.296+). [[line 268](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/agent-teams.md?plain=1#L268)] [[Source](https://code.claude.com/docs/en/agent-teams#use-subagent-definitions-for-teammates)]

#### [artifacts](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/artifacts.md) [[Source](https://code.claude.com/docs/en/artifacts)]

* Small edits to an artifact's file can be made and published in one step. In Manual or `acceptEdits` mode, Claude asks before publishing if the edit needs approval, even when an allow rule covers `Artifact`. [[lines 65-69](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/artifacts.md?plain=1#L65-L69)] [[Source](https://code.claude.com/docs/en/artifacts#when-claude-code-asks-before-publishing)]

#### [claude-code-on-the-web](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/claude-code-on-the-web.md) [[Source](https://code.claude.com/docs/en/claude-code-on-the-web)]

* Network secrets are no longer described as Pro/Max only. [[line 353](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L353)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#security-and-isolation)]

#### [claude-directory](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/claude-directory.md) [[Source](https://code.claude.com/docs/en/claude-directory)]

* `autoCompactWindow` added to the supported `agents/*.md` frontmatter keys. [[line 1294](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/claude-directory.md?plain=1#L1294)] [[Source](https://code.claude.com/docs/en/claude-directory#frontmatter-fields-by-file)]

#### [claude-projects](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/claude-projects.md) [[Source](https://code.claude.com/docs/en/claude-projects)]

* Removed the Environment "Connectors" link from project settings. [[lines 353-372](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/claude-projects.md?plain=1#L353-L372)] [[Source](https://code.claude.com/docs/en/claude-projects#get-skills-plugins-connectors-and-tools-into-threads)]

#### [cloud-environments](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/cloud-environments.md) [[Source](https://code.claude.com/docs/en/cloud-environments)]

* Network secrets now available on Pro, Max, Team, and Enterprise plans, with role-dependent behavior (Enterprise read-only without an admin role, shared environments managed by Owners). [[lines 84-103](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/cloud-environments.md?plain=1#L84-L103)] [[Source](https://code.claude.com/docs/en/cloud-environments#set-environment-variables)]
* New section on adding a secret on a Team plan without an admin role (one host, name, secret type). [[lines 125-135](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/cloud-environments.md?plain=1#L125-L135)] [[Source](https://code.claude.com/docs/en/cloud-environments#requirements)]
* Rewrote the environment selector steps (New environment dialog, editing a running session's environment, Archive environment). [[lines 35-48](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/cloud-environments.md?plain=1#L35-L48)] [[Source](https://code.claude.com/docs/en/cloud-environments#configure-your-environment)]

#### [common-workflows](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/common-workflows.md) [[Source](https://code.claude.com/docs/en/common-workflows)]

* Documented `CLAUDE_CODE_DISABLE_FILE_MENTIONS=1` (v2.1.299+, ignored in project and local settings). [[line 360](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/common-workflows.md?plain=1#L360)] [[Source](https://code.claude.com/docs/en/common-workflows#reference-files-and-directories)]

#### [context-window](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/context-window.md) [[Source](https://code.claude.com/docs/en/context-window)]

* The git status snapshot is re-read after compaction only if the session started with one. [[line 1158](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/context-window.md?plain=1#L1158)] [[Source](https://code.claude.com/docs/en/context-window#what-survives-compaction)]

#### [desktop](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)]

* Large expansion of SSH session docs: proxy/CA settings for Linux remote machines, reaching containers with `ProxyCommand`, AWS credentials in `ProxyCommand`, shell variables in `ProxyCommand`, `Match host` quirks, forwarding settings Desktop disables, and forwarding a port with `ssh -L`. [[lines 732-940](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/desktop.md?plain=1#L732-L940)] [[Source](https://code.claude.com/docs/en/desktop#remote-machine-requirements-for-ssh-sessions)]
* New sections on files and processes Desktop installs on the remote machine, removing the helper, who connected, and connections that close before login (OpenSSH log patterns, `PerSourcePenaltyExemptList`, fail2ban). [[lines 1096-1218](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/desktop.md?plain=1#L1096-L1218)] [[Source](https://code.claude.com/docs/en/desktop#files-and-processes-on-the-remote-machine)]
* New troubleshooting table for SSH failures after login and how to get Desktop's `ssh.log`. [[lines 1636-1664](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/desktop.md?plain=1#L1636-L1664)] [[Source](https://code.claude.com/docs/en/desktop#ssh-connection-fails-after-you-log-in)]
* Dev server `autoPort` default changed: servers now get the next free port instead of Claude asking (Desktop v2.37337.0+), with an exception for hardcoded npm/yarn/pnpm/bun script ports. [[lines 586-600](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/desktop.md?plain=1#L586-L600)] [[Source](https://code.claude.com/docs/en/desktop#port-conflicts)]
* Archive approval card is not shown in Auto or Bypass permissions mode. [[line 380](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/desktop.md?plain=1#L380)] [[Source](https://code.claude.com/docs/en/desktop#work-across-sessions)]
* In SSH sessions the Browser pane isn't available and `git`/`gh` must be set up on the remote for Create PR. [[lines 112-187](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/desktop.md?plain=1#L112-L187)] [[Source](https://code.claude.com/docs/en/desktop#preview-your-app)]
* Linux remotes need glibc 2.17+ or musl. Managed settings files must be readable by each developer's account. [[line 727](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/desktop.md?plain=1#L727)] [[Source](https://code.claude.com/docs/en/desktop#remote-machine-requirements-for-ssh-sessions)]

#### [desktop-changelog](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/desktop-changelog.md) [[Source](https://code.claude.com/docs/en/desktop-changelog)]

* Received the same edits as `desktop` (SSH session documentation, `autoPort` default, archive approval behavior). See above.

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* New `CLAUDE_CODE_ARTIFACT_PUBLISH_EDITS`: set to `0` to stop applying artifact edits during publishing (v2.1.300+). [[line 208](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/env-vars.md?plain=1#L208)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* New entry: "Hook needs quotes around a path with a space" for `asyncRewake` hooks. [[lines 5196-5211](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/errors.md?plain=1#L5196-L5211)] [[Source](https://code.claude.com/docs/en/errors#configuration-warnings)]
* New entry: "Skill or command name refused", with debug steps. [[lines 5232-5249](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/errors.md?plain=1#L5232-L5249)] [[Source](https://code.claude.com/docs/en/errors#configuration-warnings)]

#### [github-enterprise-server](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/github-enterprise-server.md) [[Source](https://code.claude.com/docs/en/github-enterprise-server)]

* Troubleshooting for "Authentication failed while accessing the repository": connect your own GitHub Enterprise account from the repository picker. [[line 193](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/github-enterprise-server.md?plain=1#L193)] [[Source](https://code.claude.com/docs/en/github-enterprise-server#cloud-session-fails-to-clone-repository)]

#### [headless](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/headless.md) [[Source](https://code.claude.com/docs/en/headless)]

* Replacing the system prompt in `-p` runs also drops the git status snapshot. [[line 358](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/headless.md?plain=1#L358)] [[Source](https://code.claude.com/docs/en/headless#customize-the-system-prompt)]

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* `CLAUDE_CODE_DISABLE_FILE_MENTIONS=1` makes `@` paths go through file tools, so matching PreToolUse hooks run. [[lines 1670-1675](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/hooks.md?plain=1#L1670-L1675)] [[Source](https://code.claude.com/docs/en/hooks#pretooluse)]

#### [ide-integrations](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/ide-integrations.md) [[Source](https://code.claude.com/docs/en/ide-integrations)]

* New troubleshooting section: a resumed conversation can be blank at first ("Waiting for your plugins…"). [[line 783](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/ide-integrations.md?plain=1#L783)] [[Source](https://code.claude.com/docs/en/ide-integrations#a-resumed-conversation-is-blank-at-first)]

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* `/mcp` status guidance updated to describe a checkmark or ✘ instead of `connected`/`failed`. [[line 701](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/mcp.md?plain=1#L701)] [[Source](https://code.claude.com/docs/en/mcp#example-connect-to-github-for-code-reviews)]

#### [model-config](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* Added per-subagent auto-compact window to the places you can set it. [[line 776](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/model-config.md?plain=1#L776)] [[Source](https://code.claude.com/docs/en/model-config#set-the-auto-compact-window)]

#### [monitoring-usage](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* Added a pointer to OpenTelemetry for the Claude API / Managed Agents. [[line 7](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/monitoring-usage.md?plain=1#L7)] [[Source](https://code.claude.com/docs/en/monitoring-usage#monitoring)]

#### [plugin-evals](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/plugin-evals.md) [[Source](https://code.claude.com/docs/en/plugin-evals)]

* Runs that end on an API error (rate or usage limit) now score 0 without grading and make the command exit non-zero (v2.1.299+). New troubleshooting section. [[lines 408-410](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/plugin-evals.md?plain=1#L408-L410), [lines 729-743](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/plugin-evals.md?plain=1#L729-L743)]

#### [plugins/cli-reference](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/plugins/cli-reference.md) [[Source](https://code.claude.com/docs/en/plugins/cli-reference)]

* Eval exit codes updated to include API-error runs. [[lines 482-483](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/plugins/cli-reference.md?plain=1#L482-L483)] [[Source](https://code.claude.com/docs/en/plugins/cli-reference#plugin-eval)]

#### [plugins/components](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/plugins/components.md) [[Source](https://code.claude.com/docs/en/plugins/components)]

* Plugin agents support `autoCompactWindow`. [[line 685](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/plugins/components.md?plain=1#L685)] [[Source](https://code.claude.com/docs/en/plugins/components#frontmatter-fields-in-plugin-agents)]

#### [plugins/mods/reference](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/plugins/mods/reference.md) [[Source](https://code.claude.com/docs/en/plugins/mods/reference)]

* New `next.error.cause` field for `re-entry` errors (`rewritten`, `lent`). [[lines 36-37](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/plugins/mods/reference.md?plain=1#L36-L37)] [[Source](https://code.claude.com/docs/en/plugins/mods/reference#the-hook-function)]
* New `skill.prompt` fields: `e.source`, `e.pluginName`, `e.path`, `e.frontmatter`, `e.frontmatterProblem` (v2.1.299+). [[lines 83-100](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/plugins/mods/reference.md?plain=1#L83-L100)] [[Source](https://code.claude.com/docs/en/plugins/mods/reference#prompts-and-what-claude-reads)]

#### [routines](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/routines.md) [[Source](https://code.claude.com/docs/en/routines)]

* Network secrets guidance now refers to Anthropic-hosted environments rather than Pro/Max plans. [[line 74](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/routines.md?plain=1#L74)] [[Source](https://code.claude.com/docs/en/routines#create-from-the-web)]

#### [scheduled-tasks](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/scheduled-tasks.md) [[Source](https://code.claude.com/docs/en/scheduled-tasks)]

* `CronList` now shows next run times, and the `CronCreate` row displays the next run. A dynamic loop's pending wakeup appears as a one-shot task that can run slightly early. [[lines 68-166](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/scheduled-tasks.md?plain=1#L68-L166)] [[Source](https://code.claude.com/docs/en/scheduled-tasks#let-claude-choose-the-interval)]

#### [self-hosted-environments-configuration](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/self-hosted-environments-configuration.md) [[Source](https://code.claude.com/docs/en/self-hosted-environments-configuration)]

* New `CLAUDE_CODE_REMOTE_MCP_CONFIG` variable that wrappers must carry over. [[line 35](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/self-hosted-environments-configuration.md?plain=1#L35)] [[Source](https://code.claude.com/docs/en/self-hosted-environments-configuration#wrapper-scripts)]
* New section on quoting arguments and variables in wrapper and hook scripts. [[lines 47-53](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/self-hosted-environments-configuration.md?plain=1#L47-L53)] [[Source](https://code.claude.com/docs/en/self-hosted-environments-configuration#quote-the-arguments-and-variables-your-script-expands)]
* New "Make on-demand runners exit when idle" section covering `--release-idle-session-min`, `--kill-session-after-min` and `--exit-if-unused-min`. A hook still running at `--hook-timeout` counts as a retryable failure. [[lines 300-324](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/self-hosted-environments-configuration.md?plain=1#L300-L324)] [[Source](https://code.claude.com/docs/en/self-hosted-environments-configuration#the-spawn-runner-hook)]
* Wrappers can pass `--mcp-config` after `"$@"`. [[line 453](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/self-hosted-environments-configuration.md?plain=1#L453)] [[Source](https://code.claude.com/docs/en/self-hosted-environments-configuration#mcp-servers)]

#### [self-hosted-environments-deploy](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/self-hosted-environments-deploy.md) [[Source](https://code.claude.com/docs/en/self-hosted-environments-deploy)]

* `--git-ssh-rewrite` also suits runner hosts that have only an SSH key. [[line 311](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/self-hosted-environments-deploy.md?plain=1#L311)] [[Source](https://code.claude.com/docs/en/self-hosted-environments-deploy#rewrite-git-urls-for-private-networks)]
* New troubleshooting for TLS certificate errors (`RegisterRunner failed:`, `poll failed:`) fixed with `NODE_EXTRA_CA_CERTS`. [[lines 637-642](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/self-hosted-environments-deploy.md?plain=1#L637-L642)] [[Source](https://code.claude.com/docs/en/self-hosted-environments-deploy#troubleshooting)]
* Each person creating sessions must connect their own GitHub, and requeueing after a lost runner can take longer than a few minutes. [[line 185](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/self-hosted-environments-deploy.md?plain=1#L185)] [[Source](https://code.claude.com/docs/en/self-hosted-environments-deploy#use-the-anthropic-git-proxy)]

#### [self-hosted-environments-quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/self-hosted-environments-quickstart.md) [[Source](https://code.claude.com/docs/en/self-hosted-environments-quickstart)]

* Prerequisite changed: an Owner must turn on the GitHub connector, and each developer connects their own GitHub. [[line 18](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/self-hosted-environments-quickstart.md?plain=1#L18)] [[Source](https://code.claude.com/docs/en/self-hosted-environments-quickstart#organization-and-roles)]
* An SSH key alone isn't enough, because the runner clones the `https://` URL. Use a dedicated base directory. The runner exits after serving one session. [[lines 25-121](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/self-hosted-environments-quickstart.md?plain=1#L25-L121)] [[Source](https://code.claude.com/docs/en/self-hosted-environments-quickstart#host-and-network)]

#### [self-hosted-environments-reference](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/self-hosted-environments-reference.md) [[Source](https://code.claude.com/docs/en/self-hosted-environments-reference)]

* Clarified `--startup-timeout-min` and the orchestrator `/healthz` `last_error` field. [[lines 49-143](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/self-hosted-environments-reference.md?plain=1#L49-L143)] [[Source](https://code.claude.com/docs/en/self-hosted-environments-reference#runner-cli-flags)]

#### [settings-reference](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/settings-reference.md) [[Source](https://code.claude.com/docs/en/settings-reference)]

* `includeGitInstructions`: the git status snapshot is omitted when the system prompt is replaced in `-p` runs or the Agent SDK. [[lines 3894-3898](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/settings-reference.md?plain=1#L3894-L3898)] [[Source](https://code.claude.com/docs/en/settings-reference#includegitinstructions)]

#### [skills](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)]

* New section "Characters a skill name can't hold" (zero-width, control, direction-changing, `<`/`>`, etc.) and how plugin skills handle them. [[lines 453-471](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/skills.md?plain=1#L453-L471)] [[Source](https://code.claude.com/docs/en/skills#how-a-skill-gets-its-command-name)]
* Added a troubleshooting step for unrecognized `/skill-name`. [[line 1168](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/skills.md?plain=1#L1168)] [[Source](https://code.claude.com/docs/en/skills#skill-not-triggering)]

#### [slash-commands](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/slash-commands.md) [[Source](https://code.claude.com/docs/en/slash-commands)]

* Same additions as `skills`: refused-name characters section and troubleshooting step. [[lines 453-471](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/slash-commands.md?plain=1#L453-L471)] [[Source](https://code.claude.com/docs/en/slash-commands#how-a-skill-gets-its-command-name)]

#### [sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* New `autoCompactWindow` frontmatter field (v2.1.296+) and a "Set the auto-compact window for one subagent" section (write plain integers, `200k` is misread as 200). [[line 295](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/sub-agents.md?plain=1#L295), [lines 1126-1148](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/sub-agents.md?plain=1#L1126-L1148)]
* How to find misspelled frontmatter fields via `claude --debug`. [[lines 281-284](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/sub-agents.md?plain=1#L281-L284)] [[Source](https://code.claude.com/docs/en/sub-agents#write-subagent-files)]

#### [vs-code](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/vs-code.md) [[Source](https://code.claude.com/docs/en/vs-code)]

* New troubleshooting section for a blank resumed conversation. [[line 783](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/vs-code.md?plain=1#L783)] [[Source](https://code.claude.com/docs/en/vs-code#a-resumed-conversation-is-blank-at-first)]

#### [web-quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/web-quickstart.md) [[Source](https://code.claude.com/docs/en/web-quickstart)]

* You can add multiple repositories to work across them in one session. [[line 125](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/web-quickstart.md?plain=1#L125)] [[Source](https://code.claude.com/docs/en/web-quickstart#start-a-task)]

#### [workflows](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/workflows.md) [[Source](https://code.claude.com/docs/en/workflows)]

* Clarified workflow approval: in plan mode a hook's approval alone doesn't start the workflow. [[lines 178-181](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/claude-code/workflows.md?plain=1#L178-L181)] [[Source](https://code.claude.com/docs/en/workflows#approve-the-plan-before-it-runs)]

-----

## API changes

### New Documents

#### [manage-claude/opentelemetry](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/api/manage-claude/opentelemetry.md) [[Source](https://platform.claude.com/docs/en/manage-claude/opentelemetry)]

Overview of the beta OpenTelemetry export for the Claude API and SDK. It traces Messages API requests, tool uses, and Managed Agents sessions using GenAI semantic conventions. It compares SDK tracing, API tracing, and both together, and includes example traces.

#### [manage-claude/opentelemetry/api](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/api/manage-claude/opentelemetry/api.md) [[Source](https://platform.claude.com/docs/en/manage-claude/opentelemetry/api)]

How to add an OpenTelemetry destination in the Console, Admin API, or CLI. It covers choosing workspaces, verifying that spans arrive, connecting API spans to your own traces, delivery and health, limits, and troubleshooting. It is available on Claude Platform on AWS and is not ZDR eligible for Managed Agents.

#### [manage-claude/opentelemetry/sdk](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/api/manage-claude/opentelemetry/sdk.md) [[Source](https://platform.claude.com/docs/en/manage-claude/opentelemetry/sdk)]

How to trace SDK requests and tool-runner tool uses. Install the SDK, register a tracer provider, and export spans to your platform. Notes that options and span schema can change during the beta.

#### [api/opentelemetry/spans](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/api/api/opentelemetry/spans.md) [[Source](https://platform.claude.com/docs/en/api/opentelemetry/spans)]

Span reference listing span names, kinds, and attributes for SDK spans and API spans (`service.name` `claude-platform`).

#### [api/beta/organization/telemetry_destinations](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/api/api/beta/organization/telemetry_destinations.md) [[Source](https://platform.claude.com/docs/en/api/beta/organization/telemetry_destinations)]

New Admin API reference (plus per-method pages for create, retrieve, list, update, delete, test, and workspaces add/list/remove) for registering OpenTelemetry destinations. An organization can have at most 10 destinations, and each starts enabled. Pages are also added for the CLI and the other SDK languages.

### Changed documents

#### [api/beta (SDK/CLI reference)](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/api/api/beta.md) [[Source](https://platform.claude.com/docs/en/api/beta)]

* Large expansion of the beta reference (thousands of lines), with new pages for `agents`, `sessions`, `sessions/threads`, and `sessions/events`. Matching pages were added for the CLI (`cli/beta`) and C# (`csharp/beta`), and many SDK method pages gained links.

#### [api/claude-platform-on-aws-iam-actions](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/api/api/claude-platform-on-aws-iam-actions.md) [[Source](https://platform.claude.com/docs/en/api/claude-platform-on-aws-iam-actions)]

* Added a "Telemetry destinations" section with nine IAM actions (`CreateAccountTelemetryDestination`, `TestAccountTelemetryDestination`, and others) and their scoping rules. [[lines 215-232](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/api/api/claude-platform-on-aws-iam-actions.md?plain=1#L215-L232)] [[Source](https://platform.claude.com/docs/en/api/claude-platform-on-aws-iam-actions#telemetry-destinations)]

#### [api/compliance/activities/list](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/api/api/compliance/activities/list.md) [[Source](https://platform.claude.com/docs/en/api/compliance/activities/list)]

* New activity type `org_hipaa_artifacts_terms_accepted` (an owner accepted the terms for artifacts with HIPAA configuration). The same change appears in `api/compliance` and `api/compliance/activities`.

#### [api/beta/organization](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/api/api/beta/organization.md) [[Source](https://platform.claude.com/docs/en/api/beta/organization)]

* Added the telemetry destination endpoints to the organization reference.

#### [build-with-claude/claude-platform-on-aws](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/api/build-with-claude/claude-platform-on-aws.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws)]

* Managed Agents scheduled deployments are now listed as available. [[line 538](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/api/build-with-claude/claude-platform-on-aws.md?plain=1#L538)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws#claude-managed-agents)]
* CloudTrail logs telemetry destination operations as Management events. [[line 837](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/api/build-with-claude/claude-platform-on-aws.md?plain=1#L837)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws#monitoring-and-logging)]

#### [managed-agents/scheduled-deployments](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/api/managed-agents/scheduled-deployments.md) [[Source](https://platform.claude.com/docs/en/managed-agents/scheduled-deployments)]

* On Claude Platform on AWS, each run creates its session as an IAM role. Set `execution_identity` to `{"type": "aws_role", ...}` on the agent, with trust policy, role permissions (`aws-external-anthropic:CreateSession`), and `iam:PassRole` requirements. [[lines 27-32](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/api/managed-agents/scheduled-deployments.md?plain=1#L27-L32)] [[Source](https://platform.claude.com/docs/en/managed-agents/scheduled-deployments#create-a-scheduled-deployment)]

#### [manage-claude/cmek](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/api/manage-claude/cmek.md) [[Source](https://platform.claude.com/docs/en/manage-claude/cmek)]

* OpenTelemetry destination request headers are listed among data stored under Anthropic-managed encryption (write-only values).

#### [release-notes/overview](https://github.com/gpambrozio/ClaudeDocs/blob/ba5bc9af122d35723f67730a3dd53cfbd28113d4/docs-md/api/release-notes/overview.md) [[Source](https://platform.claude.com/docs/en/release-notes/overview)]

* October 14, 2026 notes: OpenTelemetry export beta (SDK spans in Python, TypeScript, C#, Go, Java, PHP, Ruby, plus API destinations) and scheduled deployments on Claude Platform on AWS.

#### SDK version bumps and CLI

* Java SDK examples updated from 2.71.0 to 2.72.0 across `cli-sdks-libraries/sdks/java`, `get-started`, `agents-and-tools/mcp-connector`, and the Bedrock, Foundry, Vertex, and Claude Platform on AWS pages.
* The `ant` CLI version in `cli-sdks-libraries/cli/quickstart` and the Managed Agents `quickstart` and `self-hosted-sandboxes-workers` pages moved from 1.40.0 to 1.41.0.

#### Console navigation wording

* Many pages (MCP tunnels, workspaces, API keys, billing, pricing, WIF, CMEK, rate limits, app attest and others) now point to Console pages by name and URL, for example "Billing" and "MCP tunnels", instead of "Settings >" menu paths. "Developer Console" in `intro` is now "Claude Console".
