# [Claude docs changes for November 23rd, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5)]

## Executive Summary
- **Claude Ship** is a new set of GitHub pull request agents: Code Review, **PR Steward** (pushes fixes for failing checks, conflicts and review feedback) and **Claude Approvals** (a policy-file-driven approval check). New `/ship` and `/steward` commands drive this from the CLI
- **Claude Code 2.1.331** adds Code Mode on Bedrock, Google Cloud's Agent Platform, Foundry and Claude Platform on AWS, an API connectivity check in `claude doctor`, richer `gen_ai.*` trace span attributes, and `optionalDependencies` in plugin manifests. It also ships a large batch of VS Code extension features and fixes
- **Enterprise Frontier Safeguards (EFS)** gets a full documentation section in the API docs: Zero Data Retention with Sealed Safety Data stored in your own cloud bucket, customer-managed keys, Safety Cases, and a new External Storage Admin API (beta header `efs-2026-10-01`)
- Claude Opus 4.5 is deprecated, with retirement on January 22, 2027 and `claude-opus-5-5` as the replacement. Prefill docs now say which models still accept it
- New page on sharing cloud and Remote Control sessions by link. Cloud sessions now load plugins synced from your claude.ai account

## New Claude Code versions

### [2.1.331](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/versions/2.1.331.md)

#### New features

* Code Mode support in terminal sessions on Amazon Bedrock, Google Cloud's Agent Platform, Microsoft Foundry and Claude Platform on AWS
* `claude doctor` has a new API connectivity section reporting whether the API can be reached, with the HTTP status or error
* `CLAUDE_CODE_DISABLE_RESPONSE_COMPRESSION` asks for uncompressed model responses behind proxies that cut compressed ones off
* `claude_code.llm_request` trace spans now carry `gen_ai.usage.*`, `gen_ai.response.model` and `gen_ai.operation.name`
* Plugin manifests support `optionalDependencies`: plugins that install with the listing plugin and can be disabled or uninstalled on their own
* Claude apps gateway: `oidc.groups_jsonpath` reads groups from a list of objects with a small JSONPath subset, and `CLAUDE_GATEWAY_IDP_CONNECT_BY_HOSTNAME=1` hands the proxy an `https` IdP's hostname
* Notice when tap-mode voice dictation stops by itself (15 seconds of silence or the 2-minute limit)
* VS Code: "Add Cell to Chat", "Fix with Claude Code" quick fix (also on failed tests), "Add to Chat" in Source Control, and "Resolve Merge Conflicts" for conflicted files
* VS Code: warnings before sending very large selections or text files, and a revoke-page link when logout isn't confirmed

#### Existing feature improvements

* Faster start-up: sessions no longer wait for the model list or on git outside a repository; faster first Bash command on Windows
* Plugin auto-update notice now names plugins newly installed as dependencies separately
* Code Mode tool search shows more of an MCP tool's description, including limits, formats and defaults
* Much shorter Console sign-in link for `/login` and `claude auth login --console`
* Better screen reader typing speed and shorter folder trust prompts in short terminals
* `/ide` auto-connect and subagent-view `/clear`, `/compact`, `/rewind` questions now list Yes first (they still default to No)
* `PermissionDenied` hook `retry: true` now tells Claude to retry only if you asked for that call
* VS Code: large speed and memory improvements for long chats, remote windows (SSH, WSL, containers) and slow disks; the @ menu lists open editor tabs first
* VS Code: saving a proposed diff accepts it only after you click or type in its right side; terminal-session diffs open without taking keyboard focus
* Upcoming (on or after November 30, 2026): marketplaces in managed `extraKnownMarketplaces` will auto-update by default; set `"autoUpdate": false` to opt out
* Windows: check managed settings in the registry before upgrading, since an `HKLM` policy outranks `managed-settings.json`

#### Major bug fixes

* Fixed MCP tool calls hanging up to 30 minutes on some malformed replies
* Fixed /compact and auto-compact losing part of the summary when it quoted certain XML tags
* Fixed turns failing or timing out when a reply went silent during thinking; Claude Code now retries once
* Fixed Esc and Stop waiting a minute or more when a cloud or network file read stalls
* Fixed a rewind deleting files after a failed restore
* Fixed interrupted plugin updates leaving partial plugin folders
* Fixed Code Mode losing thinking and prompt cache on `--resume`/`--continue`, and losing the middle of long script output
* Fixed Stop hooks missing the last reply in Claude Desktop (SubagentStop hooks now wait too)
* Fixed `@file#10-12` mentions attaching the whole file
* Fixed a crash when a custom endpoint returned a tool call with no name
* Windows: fixed startup failure with non-ASCII managed settings in the registry, and `/desktop` downloading an old installer
* VS Code: many fixes, including Escape stopping Claude in dialogs, `@` menu issues, diff and rewind problems, and a forked conversation overwriting the original's plan file. A wrapper, hook or MCP server that runs VS Code as Node must now set `ELECTRON_RUN_AS_NODE=1`

-----

## Claude Code changes

### New Documents

#### [Approvals](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/approvals.md) [[Source](https://code.claude.com/docs/en/approvals)]

Overview of Claude Approvals, a GitHub pull request check that reports who still has to approve. It follows a policy file in your repository. It's in public beta on Team and Enterprise plans.

#### [Approvals Classifiers](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/approvals-classifiers.md) [[Source](https://code.claude.com/docs/en/approvals-classifiers)]

How rules can depend on a judgment about the change. Covers the built-in `claude/code_review` and `claude/diff` classifiers and custom `repo/<name>` classifiers defined in `.claude/classifiers/<name>/def.yml`. Also covers outputs, inputs, tools, budgets and run costs.

#### [Approvals Github Rules](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/approvals-github-rules.md) [[Source](https://code.claude.com/docs/en/approvals-github-rules)]

How the check interacts with required reviews, CODEOWNERS, auto-merge and merge queues. Lists what can merge without human review, includes a rule that asks for one non-author person, and says who can loosen a policy.

#### [Approvals Policy](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/approvals-policy.md) [[Source](https://code.claude.com/docs/en/approvals-policy)]

Reference for `.claude/approvals.yml`: rules, `paths`, `verdict` (`seats`, `claude`), `override`, `reuse`, `advisory`, nested policy files, observe mode, how rules combine and how approvals count.

#### [Approvals Pull Requests](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/approvals-pull-requests.md) [[Source](https://code.claude.com/docs/en/approvals-pull-requests)]

What each check title means and what to do next, the `@claude approvals` comment commands, and handling pull requests from Claude and from forks.

#### [Approvals Setup](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/approvals-setup.md) [[Source](https://code.claude.com/docs/en/approvals-setup)]

Prerequisites and steps to turn on Approvals: start in observe mode, enforce the policy, require the check, set spend limits and turn it off.

#### [Approvals Troubleshooting](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/approvals-troubleshooting.md) [[Source](https://code.claude.com/docs/en/approvals-troubleshooting)]

Fixes for a check that didn't appear or doesn't pass, a policy file Approvals refuses, and a classifier that gives no answer.

#### [Claude Ship](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/claude-ship.md) [[Source](https://code.claude.com/docs/en/claude-ship)]

Introduces Claude Ship, the combination of Code Review, PR Steward and Claude Approvals, available on Team and Enterprise plans, with setup pointers.

#### [PR Steward](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/pr-steward.md) [[Source](https://code.claude.com/docs/en/pr-steward)]

PR Steward is an agent that works on open GitHub pull requests in cloud sessions. It addresses review feedback, fixes failing checks and resolves merge conflicts. It's controlled by the `claude-pr-steward-watching` label or `@claude stop`, and it doesn't approve or merge.

#### [PR Steward Pull Requests](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/pr-steward-pull-requests.md) [[Source](https://code.claude.com/docs/en/pr-steward-pull-requests)]

What PR Steward adds to a pull request (labels, comments, commits), how to instruct, start, stop or limit it, and how to save instructions for a repository.

#### [PR Steward Security](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/pr-steward-security.md) [[Source](https://code.claude.com/docs/en/pr-steward-security)]

The GitHub identity, permissions, repositories and cloud session setup PR Steward uses, and what limits approvals and merges.

#### [PR Steward Setup](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/pr-steward-setup.md) [[Source](https://code.claude.com/docs/en/pr-steward-setup)]

Owner-role setup: prerequisites, adding repositories, spend limits, choosing when it starts and for which authors, and running it in a self-hosted environment.

#### [PR Steward Troubleshooting](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/pr-steward-troubleshooting.md) [[Source](https://code.claude.com/docs/en/pr-steward-troubleshooting)]

Why PR Steward may not start, stop or pause, how to match its comments, and the messages an Owner sees during setup.

#### [Share Sessions](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/share-sessions.md) [[Source](https://code.claude.com/docs/en/share-sessions)]

How to share a cloud or Remote Control session by link: what recipients can read (including credentials, connector results and tool output), who can open the link, and how to stop sharing. Replaces the sharing section previously in the web docs.

#### [Ship Command](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/ship-command.md) [[Source](https://code.claude.com/docs/en/ship-command)]

`/ship` opens a pull request, reviews it with `/code-review`, then keeps a local "watch" that works on feedback, failing checks and conflicts. `/steward` starts the watch on an already-open pull request without the review. CLI only.

#### [Ship Command Troubleshooting](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/ship-command-troubleshooting.md) [[Source](https://code.claude.com/docs/en/ship-command-troubleshooting)]

Symptom table for `/ship` and `/steward`: missing command, nothing committed or pushed, a watch that didn't start or stopped, and unexpected pull request results.

### Changed documents

#### [Agent SDK hooks](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/agent-sdk/hooks.md) [[Source](https://code.claude.com/docs/en/agent-sdk/hooks)]

* `WorktreeCreate` now means the hook creates the worktree instead of git and returns its path in `hookSpecificOutput.worktreePath`; a callback must return one, and a timeout makes worktree creation fail. [[line 170](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/agent-sdk/hooks.md?plain=1#L170)] [[Source](https://code.claude.com/docs/en/agent-sdk/hooks#available-hooks)]

#### [Agent SDK typescript](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* Per-agent `mcpServers` note: put `createSdkMcpServer()` servers in `Options.mcpServers`. [[line 1294](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L1294)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#agentdefinition)]
* `MonitorOutput` gains `keptInSandboxByCheck`. [[line 4267](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L4267)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#monitor)]

#### [Agent view](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/agent-view.md) [[Source](https://code.claude.com/docs/en/agent-view)]

* Troubleshooting entry changed from `Could not resolve authentication method` to a background session showing `Not logged in`, with updated supervisor restart steps. [[lines 985-993](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/agent-view.md?plain=1#L985-L993)] [[Source](https://code.claude.com/docs/en/agent-view#a-background-session-shows-not-logged-in)]

#### [Analytics](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/analytics.md) [[Source](https://code.claude.com/docs/en/analytics)]

* Removed the `claude-code-assisted` GitHub label description. [[line 116](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/analytics.md?plain=1#L116)] [[Source](https://code.claude.com/docs/en/analytics#attribution-process)]

#### [Chrome](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/chrome.md) [[Source](https://code.claude.com/docs/en/chrome)]

* Documented `claude --no-chrome` to skip Chrome for one session while the setting stays on. [[line 110](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/chrome.md?plain=1#L110)] [[Source](https://code.claude.com/docs/en/chrome#enable-chrome-by-default)]

#### [Claude apps gateway config](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/claude-apps-gateway-config.md) [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config)]

* `modelPrefer1mContext` now shows only the 1M option and needs a minimum Claude Desktop version. [[line 1471](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/claude-apps-gateway-config.md?plain=1#L1471)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config#extended-context-in-claude-desktop)]
* `access_control.allow_cidrs` guidance rewritten: recommended IPv4 and IPv6 private ranges, link-local not counted as public, health probes not checked. [[lines 1696-1705](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/claude-apps-gateway-config.md?plain=1#L1696-L1705)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config#http-tuning)]

#### [Claude apps gateway deploy](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/claude-apps-gateway-deploy.md) [[Source](https://code.claude.com/docs/en/claude-apps-gateway-deploy)]

* The gateway writes a startup `WARNING` reminding you to keep it off the public internet; `CLAUDE_GATEWAY_LOG_LEVEL=error` hides it. [[line 184](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/claude-apps-gateway-deploy.md?plain=1#L184)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-deploy#write-operational-logs-as-json)]
* Long-thinking timeout troubleshooting now describes one or two long requests before `502`/`504`, and up to two streams of waiting. [[lines 443-535](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/claude-apps-gateway-deploy.md?plain=1#L443-L535)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-deploy#troubleshooting)]

#### [Claude apps gateway on GCP](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/claude-apps-gateway-on-gcp.md) [[Source](https://code.claude.com/docs/en/claude-apps-gateway-on-gcp)]

* Cloud SQL command adds `--edition=enterprise`, and a note that internal Ingress needs a proxy-only subnet and firewall rule. [[line 117](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/claude-apps-gateway-on-gcp.md?plain=1#L117)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-on-gcp#deploy-the-gateway)]

#### [Claude Code on the web](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/claude-code-on-the-web.md) [[Source](https://code.claude.com/docs/en/claude-code-on-the-web)]

* The session sharing section was replaced by a link to the new Share Sessions page. [[line 334](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L334)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#share-sessions)]
* The Auto-fix toggle is unavailable where PR Steward works on your pull requests. [[line 371](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L371)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#auto-fix-pull-requests)]

#### [Claude projects](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/claude-projects.md) [[Source](https://code.claude.com/docs/en/claude-projects)]

* UI renames: **Library** is now the **Context** tab, thread model and effort merged into **Threads**, **Coordinator** sets only the model, and Pause and Restart Claude moved to **Advanced**. New projects default to medium effort for threads. [[lines 154-245](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/claude-projects.md?plain=1#L154-L245)] [[Source](https://code.claude.com/docs/en/claude-projects#your-first-batch)]
* Plugins now come from your claude.ai account instead of a per-project Plugins setting. [[line 366](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/claude-projects.md?plain=1#L366)] [[Source](https://code.claude.com/docs/en/claude-projects#get-skills-plugins-connectors-and-tools-into-threads)]
* Project memory needs memory turned on in claude.ai settings; the banner is now "Claude's replies aren't getting through". [[lines 288-471](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/claude-projects.md?plain=1#L288-L471)] [[Source](https://code.claude.com/docs/en/claude-projects#give-a-project-standing-context)]

#### [Cloud environments](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/cloud-environments.md) [[Source](https://code.claude.com/docs/en/cloud-environments)]

* Anthropic-hosted sessions don't add marketplaces declared in a repo's `extraKnownMarketplaces`; user-scoped plugins can be used via your claude.ai account. [[line 292](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/cloud-environments.md?plain=1#L292)] [[Source](https://code.claude.com/docs/en/cloud-environments#what-carries-over-from-your-setup)]

#### [Code mode](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/code-mode.md) [[Source](https://code.claude.com/docs/en/code-mode)]

* New "Monitor Code Mode with OpenTelemetry" section: filter `tool_use_id` by `repl_`/`toolu_cc_`, read classifier verdicts on `REPL` events, and `OTEL_LOG_TOOL_DETAILS` caution. [[line 142](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/code-mode.md?plain=1#L142)] [[Source](https://code.claude.com/docs/en/code-mode#monitor-code-mode-with-opentelemetry)]
* Telemetry requirements and error messages updated: OpenTelemetry events and metrics are now allowed, while tracing still blocks Code Mode. [[lines 53-311](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/code-mode.md?plain=1#L53-L311)] [[Source](https://code.claude.com/docs/en/code-mode#requirements)]

#### [Code review costs](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/code-review-costs.md) [[Source](https://code.claude.com/docs/en/code-review-costs)]

* Claude Approvals policies can start extra reviews or stop automatic ones. The admin UI moved to **Organization settings > Claude Ship**. [[lines 29-37](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/code-review-costs.md?plain=1#L29-L37)] [[Source](https://code.claude.com/docs/en/code-review-costs#how-often-reviews-run)]

#### [Code review pull requests](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/code-review-pull-requests.md) [[Source](https://code.claude.com/docs/en/code-review-pull-requests)]

* A review by itself doesn't approve or block; Claude Approvals and PR Steward interactions with resolved threads and findings are described. [[lines 7-33](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/code-review-pull-requests.md?plain=1#L7-L33)] [[Source](https://code.claude.com/docs/en/code-review-pull-requests#read-and-request-reviews-on-a-pull-request)]

#### [Code review setup](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/code-review-setup.md) [[Source](https://code.claude.com/docs/en/code-review-setup)]

* Setup moved to **Organization settings > Claude Ship**, with a new "Choose what Claude does on these repositories" step that includes an optional PR Steward selection. [[lines 5-50](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/code-review-setup.md?plain=1#L5-L50)] [[Source](https://code.claude.com/docs/en/code-review-setup#set-up-code-review)]

#### [Desktop](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)]

* Code review has a "Walk through in changes" action; side chat is documented as local, SSH and WSL only; external links ask whether to open in the Browser pane. [[lines 175-523](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/desktop.md?plain=1#L175-L523)] [[Source](https://code.claude.com/docs/en/desktop#browse-external-sites)]
* Auto-verify can be disabled via `"autoVerify": false` in `.claude/launch.json`. [[line 707](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/desktop.md?plain=1#L707)] [[Source](https://code.claude.com/docs/en/desktop#auto-verify-changes)]

#### [Hooks](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* `PermissionRequest` exit code 2 isn't read as a decision; use the `decision` object. In `-p` runs with no prompt tool, such a request is denied. [[lines 1033-2215](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/hooks.md?plain=1#L1033-L2215)] [[Source](https://code.claude.com/docs/en/hooks#exit-code-2-behavior-per-event)]
* `PostToolUse` `updatedToolOutput` replaces a tool's result, with limits in Cowork cloud sessions. [[line 2331](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/hooks.md?plain=1#L2331)] [[Source](https://code.claude.com/docs/en/hooks#posttooluse-decision-control)]
* `PermissionDenied` clarified: it runs when the auto mode classifier denies a call, including denials with no verdict, but not for dialog denials, `PreToolUse` blocks or `deny` rules. [[line 2509](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/hooks.md?plain=1#L2509)] [[Source](https://code.claude.com/docs/en/hooks#permissiondenied)]
* `WorktreeRemove`: if a hook exits 0 and the directory remains, remove it yourself; non-zero exit with the directory present fails the removal. [[lines 3359-3399](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/hooks.md?plain=1#L3359-L3399)] [[Source](https://code.claude.com/docs/en/hooks#worktreeremove)]

#### [MCP](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* In `claude -p`, Agent SDK and VS Code sessions, claude.ai connectors rank above plugin-provided servers when names collide. [[line 844](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/mcp.md?plain=1#L844)] [[Source](https://code.claude.com/docs/en/mcp#scope-hierarchy-and-precedence)]

#### [Model config](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* Managed-model example now uses `claude-sonnet-5`. A level set with `/effort` in a `-p` run applies to that session only. [[lines 368-684](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/model-config.md?plain=1#L368-L684)] [[Source](https://code.claude.com/docs/en/model-config#control-the-model-users-run-on)]

#### [Monitoring usage](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* `request_id` on tool events can come from Code Mode, and classifier review of Code Mode code is documented. [[lines 866-1057](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/monitoring-usage.md?plain=1#L866-L1057)] [[Source](https://code.claude.com/docs/en/monitoring-usage#tool-result-event)]

#### [Mods admin](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/plugins/mods/admin.md) [[Source](https://code.claude.com/docs/en/plugins/mods/admin)]

* New `allowManagedModsOnly` option on the built-in guard refuses users' mods; includes a policy table row and notes on what the guard skips. [[lines 22-199](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/plugins/mods/admin.md?plain=1#L22-L199)] [[Source](https://code.claude.com/docs/en/plugins/mods/admin#stop-user-installed-mods-from-loading)]

#### [Permission modes](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/permission-modes.md) [[Source](https://code.claude.com/docs/en/permission-modes)]

* Warning that in interactive terminal sessions with bypass permissions available, plan mode doesn't block file edits or shell commands. The auto mode classifier can also review Claude in Chrome actions that an allow rule matches. [[lines 293-685](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/permission-modes.md?plain=1#L293-L685)] [[Source](https://code.claude.com/docs/en/permission-modes#analyze-before-you-edit-with-plan-mode)]
* Stated boundaries are re-read from the transcript on every check and can be lost on compaction. [[line 544](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/permission-modes.md?plain=1#L544)] [[Source](https://code.claude.com/docs/en/permission-modes#boundaries-you-state-in-conversation)]

#### [Plugins install](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/plugins/install.md) [[Source](https://code.claude.com/docs/en/plugins/install)]

* To use a plugin in a cloud session, add it to your claude.ai account at claude.ai/customize/plugins; user or local scope plugins from your computer aren't available there. A **Configure** action is shown for plugins that bundle an MCP server. [[lines 122-279](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/plugins/install.md?plain=1#L122-L279)] [[Source](https://code.claude.com/docs/en/plugins/install#install-a-plugin)]

#### [Plugins loading](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/plugins/loading.md) [[Source](https://code.claude.com/docs/en/plugins/loading)]

* Synced plugins now also load in cloud sessions and project threads. [[line 113](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/plugins/loading.md?plain=1#L113)] [[Source](https://code.claude.com/docs/en/plugins/loading#plugins-synced-from-claudeai)]

#### [Remote control](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/remote-control.md) [[Source](https://code.claude.com/docs/en/remote-control)]

* Automatic reconnect after sleep or network drops. `--permission-mode` accepts `manual` as an alias for `default`. A crashed `claude remote-control` server session restarts on a message from a connected device (v2.1.238+). `/resume` or `/teleport` can disconnect when the session has a share link. [[lines 12-368](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/remote-control.md?plain=1#L12-L368)] [[Source](https://code.claude.com/docs/en/remote-control#continue-local-sessions-from-any-device-with-remote-control)]

#### [Routines](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/routines.md) [[Source](https://code.claude.com/docs/en/routines)]

* Repository, cloud environment and connector settings now sit in new UI locations (below **Trigger** or under **Advanced settings**). [[lines 98-440](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/routines.md?plain=1#L98-L440)] [[Source](https://code.claude.com/docs/en/routines#create-from-the-web)]

#### [Self-hosted environments configuration](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/self-hosted-environments-configuration.md) [[Source](https://code.claude.com/docs/en/self-hosted-environments-configuration)]

* Runners snapshot the host's `~/.claude/` once at startup; sessions on Bedrock and Google Cloud don't download claude.ai account skills or plugins. PR Steward sessions load no `CLAUDE.md` or rules file from the runner. [[lines 617-917](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/self-hosted-environments-configuration.md?plain=1#L617-L917)] [[Source](https://code.claude.com/docs/en/self-hosted-environments-configuration#what-differs-from-sessions-on-the-anthropic-api)]

#### [Setup](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/setup.md) [[Source](https://code.claude.com/docs/en/setup)]

* New "Custom launchers" and "Restore the managed launcher" sections: a replaced `~/.local/bin/claude` script keeps every installed version, and a `ln -sfn` recipe restores the symlink. The native installer prunes old versions, which matters on shared storage. [[lines 198-500](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/setup.md?plain=1#L198-L500)] [[Source](https://code.claude.com/docs/en/setup#custom-launchers)]

#### [Skills](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)]

* Your own skills named `ship`, `ship-local` or `steward` don't override the bundled `/ship` and `/steward` where available. [[line 215](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/skills.md?plain=1#L215)] [[Source](https://code.claude.com/docs/en/skills#resolve-skills-that-share-a-name)]
* If an organization turns Skills off on claude.ai, synced skills move to `~/.claude/skills/.trash/` and can be restored. [[line 271](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/skills.md?plain=1#L271)] [[Source](https://code.claude.com/docs/en/skills#where-synced-skills-load)]
* Skill directories are watched for changes except in bare mode. [[line 321](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/skills.md?plain=1#L321)] [[Source](https://code.claude.com/docs/en/skills#edit-a-skill-during-a-session)]

#### [Statusline](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/statusline.md) [[Source](https://code.claude.com/docs/en/statusline)]

* Scripts receive `COLUMNS` and `LINES` for sizing; keep lines at least four columns narrower to avoid `…` truncation. [[line 162](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/statusline.md?plain=1#L162)] [[Source](https://code.claude.com/docs/en/statusline#size-output-to-the-terminal)]
* New `pr.kind` field (`mr` for GitLab merge requests); `used_percentage` formula documented. [[lines 204-378](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/statusline.md?plain=1#L204-L378)] [[Source](https://code.claude.com/docs/en/statusline#available-data)]

#### [Sub agents](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* Resuming a subagent works through `SendMessage` (no agent teams needed), and a completed subagent can resume in the background. [[lines 1149-1169](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/sub-agents.md?plain=1#L1149-L1169)] [[Source](https://code.claude.com/docs/en/sub-agents#resume-subagents)]

#### [Workflows](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/workflows.md) [[Source](https://code.claude.com/docs/en/workflows)]

* How to use the word `ultracode` without triggering a workflow (backticks, Backspace, `Alt+W`, or the **Ultracode keyword trigger** setting). Workflow `args` is passed as structured data. [[lines 121-232](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/workflows.md?plain=1#L121-L232)] [[Source](https://code.claude.com/docs/en/workflows#dismiss-or-turn-off-the-keyword)]

#### [Terminal config](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/terminal-config.md) [[Source](https://code.claude.com/docs/en/terminal-config)]

* Custom theme color formats listed, themes hot-reload from `~/.claude/themes/`, and pasted text is marked as pasted for Claude. [[lines 168-336](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/claude-code/terminal-config.md?plain=1#L168-L336)] [[Source](https://code.claude.com/docs/en/terminal-config#create-a-custom-theme)]

-----

## API changes

### New Documents

#### [Enterprise Frontier Safeguards overview](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/api/manage-claude/enterprise-frontier-safeguards/overview.md) [[Source](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/overview)]

Beta Enterprise Frontier Safeguards (EFS): Zero Data Retention for eligible organizations using Claude's most capable models, with Sealed Safety Data written to storage you own. The section also adds these pages:
* [customer-owned-storage](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/api/manage-claude/enterprise-frontier-safeguards/customer-owned-storage.md), [external-storage](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/api/manage-claude/enterprise-frontier-safeguards/external-storage.md) and [external-storage-manage](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/api/manage-claude/enterprise-frontier-safeguards/external-storage-manage.md): create and verify a bucket, connect it in the Console, and monitor bucket health
* [customer-managed-keys](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/api/manage-claude/enterprise-frontier-safeguards/customer-managed-keys.md): encrypt data with a key in AWS KMS, Google Cloud KMS or Azure Key Vault; disabling it stops Anthropic from decrypting within about an hour
* [flagged-cases](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/api/manage-claude/enterprise-frontier-safeguards/flagged-cases.md), [safety-case-files](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/api/manage-claude/enterprise-frontier-safeguards/safety-case-files.md) and [safety-cases-api](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/api/manage-claude/enterprise-frontier-safeguards/safety-cases-api.md): how your team reviews Safety Cases (with Anthropic Human Review off) and the beta Safety Cases API under the Compliance API
* [human-review-and-access-transparency](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/api/manage-claude/enterprise-frontier-safeguards/human-review-and-access-transparency.md) and [faq](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/api/manage-claude/enterprise-frontier-safeguards/faq.md)
* Setup guides for [Console](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/api/manage-claude/enterprise-frontier-safeguards/setup-console.md), [Amazon Bedrock](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/api/manage-claude/enterprise-frontier-safeguards/setup-amazon-bedrock.md), [Claude Platform on AWS](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/api/manage-claude/enterprise-frontier-safeguards/setup-claude-platform-on-aws.md), [Google Cloud Agent Platform](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/api/manage-claude/enterprise-frontier-safeguards/setup-google-cloud-agent-platform.md) and [Claude Models on Google Cloud (Anthropic managed)](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/api/manage-claude/enterprise-frontier-safeguards/setup-claude-models-on-google-cloud-anthropic-managed.md)

#### [External Storage API](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/api/api/beta/organization/external_storage.md) [[Source](https://platform.claude.com/docs/en/api/beta/organization/external_storage)]

New beta Admin API at `/v1/organizations/external_storage` (requires `anthropic-beta: efs-2026-10-01`) for registering a bucket in your own cloud account (starts as `pending_configuration`, verified on activation). Per-operation pages: [create](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/api/api/beta/organization/external_storage/create.md), [retrieve](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/api/api/beta/organization/external_storage/retrieve.md), [list](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/api/api/beta/organization/external_storage/list.md), [update](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/api/api/beta/organization/external_storage/update.md), [activate](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/api/api/beta/organization/external_storage/activate.md) and [delete](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/api/api/beta/organization/external_storage/delete.md).

### Changed documents

#### [Beta API overview](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/api/api/beta.md) [[Source](https://platform.claude.com/docs/en/api/beta)]

* New beta header value `efs-2026-10-01`, added across the Messages, Models and token counting endpoints and all language SDK beta references. [[line 115](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/api/api/beta.md?plain=1#L115)] [[Source](https://platform.claude.com/docs/en/api/beta#anthropic-beta)]

#### [API errors and organization beta](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/api/api/beta/organization.md) [[Source](https://platform.claude.com/docs/en/api/beta/organization)]

* New error detail types: `approval_required`, `authorization_check_unavailable` and `human_review_not_available`. [[line 65](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/api/api/beta/organization.md?plain=1#L65)] [[Source](https://platform.claude.com/docs/en/api/beta/organization#domain-types)]

#### [Compliance activities](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/api/api/compliance/activities.md) [[Source](https://platform.claude.com/docs/en/api/compliance/activities)]

* New `org_external_storage_*` activity types (created, activated, updated, draining, deleted). [[line 1536](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/api/api/compliance/activities.md?plain=1#L1536)] [[Source](https://platform.claude.com/docs/en/api/compliance/activities#query-parameters)]

#### [Workspaces and compliance settings (Admin API)](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/api/api/beta/organization/workspaces.md) [[Source](https://platform.claude.com/docs/en/api/beta/organization/workspaces)]

* Workspace endpoints, and [compliance settings](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/api/api/beta/organization/compliance_settings.md), accept the optional `efs-2026-10-01` beta header for additional parameters and response fields. [[line 58](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/api/api/beta/organization/workspaces.md?plain=1#L58)] [[Source](https://platform.claude.com/docs/en/api/beta/organization/workspaces#headers)]

#### [Organization webhooks](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/api/manage-claude/organization-webhooks.md) [[Source](https://platform.claude.com/docs/en/manage-claude/organization-webhooks)]

* New `external_storage.failed` and `external_storage.recovered` events when a bucket fails or passes Anthropic's daily check; also added to the webhook API references. [[line 166](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/api/manage-claude/organization-webhooks.md?plain=1#L166)] [[Source](https://platform.claude.com/docs/en/manage-claude/organization-webhooks#customer-owned-storage-events)]

#### [API and data retention](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/api/manage-claude/api-and-data-retention.md) [[Source](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention)]

* Three data handling arrangements are now offered: Legacy ZDR, HIPAA readiness and EFS ZDR (beta). HIPAA-ready access can be enabled in the Console with the standard BAA, with help for disabled or missing cards. [[lines 11-122](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/api/manage-claude/api-and-data-retention.md?plain=1#L11-L122)] [[Source](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention#api-and-data-retention)]

#### [Model deprecations](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/api/about-claude/model-deprecations.md) [[Source](https://platform.claude.com/docs/en/about-claude/model-deprecations)]

* Claude Opus 4.5 (`claude-opus-4-5-20251101`) is deprecated as of 2026-11-23, retiring January 22, 2027. The replacement is `claude-opus-5-5`. [[line 87](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/api/about-claude/model-deprecations.md?plain=1#L87)] [[Source](https://platform.claude.com/docs/en/about-claude/model-deprecations#model-status)]

#### [Working with messages](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/api/build-with-claude/working-with-messages.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/working-with-messages)]

* Prefill section rewritten (same change in the [Claude API primer](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/api/claude_api_primer.md)): a prefill is a trailing `assistant` message. Claude 4.5 and earlier accept it unless retired, and all other models return a 400. The example now uses Claude Opus 4.5. [[line 361](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/api/build-with-claude/working-with-messages.md?plain=1#L361)] [[Source](https://platform.claude.com/docs/en/build-with-claude/working-with-messages#prefilling-claudes-response)]

#### [Managed agents secure deployment](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/api/managed-agents/secure-deployment.md) [[Source](https://platform.claude.com/docs/en/managed-agents/secure-deployment)]

* New "Limit where your Claude API keys work" section on using the organization IP allowlist (beta), with a table of addresses to add so you don't lock yourself out. [[line 858](https://github.com/gpambrozio/ClaudeDocs/blob/4a98bc6bd8c8f7395bc1f9cb39324a006cb3d6c5/docs-md/api/managed-agents/secure-deployment.md?plain=1#L858)] [[Source](https://platform.claude.com/docs/en/managed-agents/secure-deployment#limit-where-your-claude-api-keys-work)]
