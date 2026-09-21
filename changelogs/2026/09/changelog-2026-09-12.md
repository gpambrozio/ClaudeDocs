# [Claude docs changes for September 12th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/a8905ddd46628feab3e79423cc6c150d518c5031) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/a8905ddd46628feab3e79423cc6c150d518c5031)]

## Executive Summary
- **`claude plugin eval` arrives with a 625-line manual of its own.** Write realistic prompts plus graders, run each case three times with your plugin and three times without, and read the `Δ` that says what the plugin actually contributed — with CI gating, cost ceilings, MCP mocking and a documented sandbox
- **Glob and Grep are no longer in the default tool set on macOS, Linux and WSL.** Claude searches with `find` and `grep` through Bash instead (running embedded `bfs` and `ugrep`), so those searches now reach your hooks and permission rules as `Bash` calls
- OpenTelemetry gains repository identity: `OTEL_METRICS_INCLUDE_REPOSITORY=true` tags metrics and events with `vcs.*` attributes derived from the `origin` remote, alongside a set of new "safe" bounded attributes (`tool_name_safe`, `query_source_safe`, `bash_argv0`, `error_class`) that carry no user-chosen names
- Cloud sessions' GitHub access rewritten: a browser GitHub App connection now reaches private repositories only where the App is installed, while `/web-setup` reaches anything your `gh` token can. `claude --cloud` falls back to uploading a local bundle in more cases, including a github.com repo without the App
- Claude Desktop no longer puts every session in a worktree — it's a **worktree** option next to the branch name — and Windows no longer requires Git just to open the Code tab

## New Claude Code versions

### [2.1.269](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/versions/2.1.269.md)

#### New features

* Added `claude plugin eval`: run a plugin's eval suite and get scored, reproducible results as JSON and an HTML report
* Added `/output-style [name]` to list and switch output styles, including over Remote Control and in cloud and other headless sessions
* Added a diff of the files a Bash command changed to the Bash tool result, under the `bashEditDiffEnabled` setting
* Added `OTEL_METRICS_INCLUDE_REPOSITORY` for `vcs.*` repository attributes; commit events get `vcs.ref.head.*` with `OTEL_LOG_TOOL_DETAILS`
* Added `CLAUDE_CODE_GATEWAY_MODEL_DISCOVERY_TIMEOUT_MS` to extend the LLM gateway `/v1/models` discovery timeout past its 3s default
* Added `CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS` (1–256) to raise the Workflow tool's per-run concurrent agent limit

#### Existing feature improvements

* Improved keyboard support over SSH and in unrecognized terminals: terminals answering the kitty keyboard query, such as foot and Alacritty 0.16+, now get Shift+Enter and Ctrl+Shift shortcuts without `/terminal-setup`
* Improved responsiveness in long sessions by no longer re-processing the whole conversation to build collapsed tool-use summaries
* Improved prompt suggestion filtering for Japanese, Chinese and Korean text
* Changed `/ultrareview --post` to post the PR comment directly when findings arrive instead of starting a second cloud session
* Changed skills synced from claude.ai in cloud sessions to be named `anthropic-skills:<name>`, matching Claude Desktop
* [VSCode] Added an agent map behind an "N agents" footer pill, with per-agent cards, Stop agent, and read-only transcripts
* [VSCode] Added Hooks and Permission rules dialogs for viewing and editing user, project and local settings; managed, plugin and session entries stay read-only

#### Major bug fixes

* Fixed a deny or ask permission rule starting with `!` applying beyond the settings source that wrote it; such a rule now applies only within its own source, and a bare `!` negation is ignored
* Fixed `Edit()` deny rules and the write-path check not applying to the file a Bash `tee` command writes
* Fixed plugin archives extracted for a session being readable by other local users, files keeping world-writable bits, and stale files surviving re-extraction
* Fixed the prompt cache being partially invalidated on the turn after a response was cut off at the output-token limit and resumed
* Fixed sessions getting permanently stuck on "Prompt is too long" when auto-compaction had no complete earlier exchange to summarize
* Fixed `/goal` runs silently stalling after API errors, network drops or token limits; the goal now retries with backoff or pauses and says why
* Fixed the git status Claude is told after a compaction being the one from session start rather than the current status
* Fixed the attribution reminder overriding a CLAUDE.md or memory rule against commit and pull request attribution
* Fixed `permission_denials` in `--output-format stream-json` omitting Read, Edit and Write calls blocked by a path-scoped deny rule
* Fixed F1/F2/F4 in kitty-protocol terminals, Delete in st, Alt+arrows in rxvt-unicode, and Shift+punctuation in WezTerm (a 2.1.247 regression)
* Fixed `CLAUDE_CODE_RESUME_INTERRUPTED_TURN` re-running a turn that had failed more than six hours earlier
* Fixed organization plugins enabled through managed settings not loading in headless sessions and on Claude Desktop
* Fixed `/btw` answers containing made-up tool calls and output
* Fixed CMYK JPEG images failing to attach with "cannot decode"

-----

## Claude Code changes

### New Documents

#### [plugin-evals](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/plugin-evals.md) [[Source](https://code.claude.com/docs/en/plugin-evals)]

A complete guide to `claude plugin eval`, the new command for measuring whether a plugin actually steers Claude to the right outcome. It covers the whole surface:

* **The scoring model.** Each case is a prompt plus graders. A case runs three times by default, a run's score is the weighted fraction of graders that passed, and the case's score is the mean across runs. Crucially, every case also runs the same number of times *without* the plugin, producing `WITH`, `W/OUT` and `Δ` columns — a case scoring 1.0 in both arms proves the plugin isn't what made it pass.
* **Six grader types.** `regex`, `tool_used`, `tool_order` and `file_exists` are computed from the transcript and cost nothing; `llm` and `baseline` call a judge model. There are no custom-code graders. Guidance favours `regex` over long output and `llm` only over short output with concrete PASS/FAIL rubrics.
* **Baseline fairness.** A `tool_used: Skill` grader can never pass without the plugin, so Claude Code excludes it from the score in both arms and reports it as an indicator only — otherwise `Δ` would be inflated. `arm: with-only` and `arm: both` control this per grader.
* **Hard tool isolation.** Runs never stop to ask for permission: ungranted tools such as `Bash`, `Write` and `WebFetch` are removed from the session entirely. Granting `Bash` puts every command under Claude Code's OS-level sandbox, and on a machine with no sandbox backend Claude Code refuses the run rather than running it unconfined — so native Windows needs WSL2 and Linux needs `bubblewrap` and `socat`.
* **What a run can access.** Each run gets a throwaway home, working directory and configuration, with no user settings, `CLAUDE.md`, MCP servers, memory or other plugins. The case definitions are hidden from the agent. The page is blunt that this isolates the *agent under test*, not the plugin's own code: "a suite that passes says nothing about whether the plugin is safe."
* **CI usage**, with `--trust-plugin` to skip the trust prompt, `--threshold` to gate the exit code, `--max-cost-usd` as a ceiling (exit 2 on a partial run), and pinned `--model` and `--judge-model` so a model rollout isn't mistaken for a plugin regression.

### Changed documents

#### [admin-setup](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/admin-setup.md) [[Source](https://code.claude.com/docs/en/admin-setup)]

* The WSL `/status` interpretation guide was replaced with a link to the managed-settings page's new "Read the source in /status" section. [[line 74](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/admin-setup.md?plain=1#L74)] [[Source](https://code.claude.com/docs/en/admin-setup#wsl-sessions-in-claude-code-desktop)]

#### [advisor](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/advisor.md) [[Source](https://code.claude.com/docs/en/advisor)]

* A Fable 5.1 main model now accepts a Fable 5 advisor; the row no longer restricts it to "the same Fable version". [[line 89](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/advisor.md?plain=1#L89)] [[Source](https://code.claude.com/docs/en/advisor#choose-an-advisor-model)]

#### [agent-sdk/agent-loop](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/agent-sdk/agent-loop.md) [[Source](https://code.claude.com/docs/en/agent-sdk/agent-loop)]

* Permission wording tightened throughout to distinguish *tools* from *calls that need approval*: `dontAsk` now runs calls that need no approval in `default` mode, such as file reads inside your working directories, and denies only what would otherwise prompt. [[lines 168-226](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/agent-sdk/agent-loop.md?plain=1#L168-L226)] [[Source](https://code.claude.com/docs/en/agent-sdk/agent-loop#tool-permissions)]

#### [agent-sdk/permissions](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/agent-sdk/permissions.md) [[Source](https://code.claude.com/docs/en/agent-sdk/permissions)]

* The evaluation flow now documents that a call the tool approves on its own — a file read inside your working directories, a read-only Bash command — resolves without any rule. [[line 38](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/agent-sdk/permissions.md?plain=1#L38)] [[Source](https://code.claude.com/docs/en/agent-sdk/permissions#how-permissions-are-evaluated)]
* New paragraph under the locked-down-agent example spelling out that `dontAsk` plus `allowedTools` still runs read-only Bash commands, `Agent`, and working-directory reads whether or not you list them. To put a tool out of reach entirely, use its bare name in `disallowedTools`. [[line 94](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/agent-sdk/permissions.md?plain=1#L94)] [[Source](https://code.claude.com/docs/en/agent-sdk/permissions#allow-and-deny-rules)]

#### [agent-sdk/typescript](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* New "What `readFile()` can read" section: it serves a narrower set than the Read tool — a regular file inside the session's working directories, plus a few of Claude Code's own session files. `Read` deny and ask rules still block a path, and a broad `Read` allow rule doesn't widen it. Anything else resolves `null`. [[lines 820-829](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L820-L829)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#sdkcontrolreadfileresponse)]
* `artifactRead` documented as Claude Code's own bookkeeping that your code needn't act on, with `ver` absent when no version was recorded. [[line 3669](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L3669)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#webfetch)]
* Correction: Claude Code doesn't emit the local-command-output message type at all. Sending `/context` or `/usage` as a prompt returns an `SDKAssistantMessage`. [[line 5017](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L5017)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#sdklocalcommandoutputmessage)]

#### [artifacts](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/artifacts.md) [[Source](https://code.claude.com/docs/en/artifacts)]

* A bare `WebFetch` deny or ask rule no longer turns artifacts off or blocks artifact reads — you need a `WebFetch(domain:claude.ai)` rule. [[line 316](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/artifacts.md?plain=1#L316)] [[Source](https://code.claude.com/docs/en/artifacts#disable-artifacts)]

#### [authentication](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/authentication.md) [[Source](https://code.claude.com/docs/en/authentication)]

* The list of per-key exceptions was replaced by a link, and the keys needing duplication narrowed to `forceLoginOrgUUID` plus the `"claudeai"` and `"console"` values of `forceLoginMethod`. [[line 149](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/authentication.md?plain=1#L149)] [[Source](https://code.claude.com/docs/en/authentication#restrict-login-to-your-organization)]

#### [claude-apps-gateway](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/claude-apps-gateway.md) [[Source](https://code.claude.com/docs/en/claude-apps-gateway)]

* Two new unavailability rows: `/design-sync` and `/design-login` need claude.ai, which the CLI doesn't contact on gateway sessions, and every feature that needs feature-flag fetching (such as `/import`) is off there too. [[lines 408-409](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/claude-apps-gateway.md?plain=1#L408-L409)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway#availability-and-limitations)]

#### [claude-code-on-the-web](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/claude-code-on-the-web.md) [[Source](https://code.claude.com/docs/en/claude-code-on-the-web)]

* **Reversal of a documented behavior.** The page previously said a cloud session could access any repository the connecting account could see and that App installation "is not a session-level access control". The GitHub-authentication table now has a "Repositories sessions can reach" column: the GitHub App reaches any public repository plus private repositories it's installed on, while `/web-setup` reaches anything the `gh` token can. [[lines 33-38](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L33-L38)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#github-authentication-options)]
* The local-bundle fallback now also triggers for a github.com repository the Claude GitHub App isn't installed on — not just a repo with no remote — and applies even if you connected with `/web-setup`. [[line 98](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L98)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#send-local-repositories-without-github)]
* Bundle-created sessions can push back to a GitHub remote when your connection has push access, replacing the flat "can't push back". [[line 113](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L113)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#send-local-repositories-without-github)]
* Sending a GitLab or Bitbucket repository to a cloud session now explicitly requires `CCR_FORCE_BUNDLE=1`. [[line 332](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L332)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#limitations)]

#### [cli-reference](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* `--tools "default"` now means "the default set" rather than "all", because that set leaves out `Glob` and `Grep` on macOS, Linux and WSL. [[line 131](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/cli-reference.md?plain=1#L131)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-flags)]

#### [commands](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/commands.md) [[Source](https://code.claude.com/docs/en/commands)]

* `/design-sync` and `/import` are now also unavailable through a Claude apps gateway, and `/design-sync`'s restriction is explained as needing claude.ai rather than as a tool limitation. [[lines 74-91](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/commands.md?plain=1#L74-L91)] [[Source](https://code.claude.com/docs/en/commands#all-commands)]

#### [corporate-launcher](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/corporate-launcher.md) [[Source](https://code.claude.com/docs/en/corporate-launcher)]

* Corrected: with a launcher configured the helper processes simply lose their `claude bg-pty-host` labels rather than showing the versioned binary name. [[line 40](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/corporate-launcher.md?plain=1#L40)] [[Source](https://code.claude.com/docs/en/corporate-launcher#helper-process-names-in-process-monitors)]

#### [costs](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/costs.md) [[Source](https://code.claude.com/docs/en/costs)]

* New admin-facing bullet for the spend-limit family of messages, pointing at **Admin settings > Usage** and noting that a named plan reset time is an alternative to raising the limit. [[line 188](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/costs.md?plain=1#L188)] [[Source](https://code.claude.com/docs/en/costs#when-a-developer-asks-about-a-limit)]

#### [desktop](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)]

* Worktrees are now opt-in per session: select the **worktree** option next to the branch name, rather than every Git-repository session automatically getting one. [[line 305](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/desktop.md?plain=1#L305)] [[Source](https://code.claude.com/docs/en/desktop#work-in-parallel-with-sessions)]
* Git is no longer required to open the Code tab on Windows — only sessions that run in their own worktree need it. Desktop versions before 1.49585.0 asked for Git before any local session. [[lines 21-928](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/desktop.md?plain=1#L21-L928)] [[Source](https://code.claude.com/docs/en/desktop#desktop-application)]

#### [desktop-changelog](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/desktop-changelog.md) [[Source](https://code.claude.com/docs/en/desktop-changelog)]

* Carries the same worktree opt-in and Windows Git changes. [[lines 21-928](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/desktop-changelog.md?plain=1#L21-L928)] [[Source](https://code.claude.com/docs/en/desktop-changelog#desktop-application)]

#### [desktop-quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/desktop-quickstart.md) [[Source](https://code.claude.com/docs/en/desktop-quickstart)]

* Dropped the Windows Git prerequisite from the getting-started steps, and softened parallel sessions to "optionally each in its own Git worktree". [[lines 53-117](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/desktop-quickstart.md?plain=1#L53-L117)] [[Source](https://code.claude.com/docs/en/desktop-quickstart#start-your-first-session)]

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* Added `OTEL_METRICS_INCLUDE_REPOSITORY`, requiring v2.1.269. [[line 458](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/env-vars.md?plain=1#L458)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* `CCR_FORCE_BUNDLE` reworded from "even when GitHub access is available" to "instead of cloning from its remote", matching the broader fallback. [[line 179](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/env-vars.md?plain=1#L179)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* New "You've hit your monthly spend limit" section covering five message variants — individual, org monthly, team's shared budget, channel's monthly, and the usage-based-billing spelling `individual usage limit`. Each variant's text after the `·` names the route to a higher limit, and a named plan-window reset time means access returns without anyone raising anything. Before v2.1.268 a pooled group budget produced the `individual spend limit` message instead. [[line 211](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/errors.md?plain=1#L211)] [[Source](https://code.claude.com/docs/en/errors#find-your-error)]
* New "plugin eval is currently in early access" section: the first message means a build older than v2.1.269, the second means Anthropic switched the command off server-side and nothing local re-enables it. [[line 211](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/errors.md?plain=1#L211)] [[Source](https://code.claude.com/docs/en/errors#find-your-error)]
* The `claude import` unavailability list now includes Claude apps gateway sessions. [[line 211](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/errors.md?plain=1#L211)] [[Source](https://code.claude.com/docs/en/errors#find-your-error)]
* The marketplace entry-path refusal text gained "backslash-containing" and "or opens outside its tree" to its list of rejected shapes. [[line 211](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/errors.md?plain=1#L211)] [[Source](https://code.claude.com/docs/en/errors#find-your-error)]

#### [headless](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/headless.md) [[Source](https://code.claude.com/docs/en/headless)]

* `dontAsk` rewritten for CI: actions needing no approval in Manual mode still run, including the read-only command set. [[line 261](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/headless.md?plain=1#L261)] [[Source](https://code.claude.com/docs/en/headless#auto-approve-tools)]

#### [hooks-guide](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/hooks-guide.md) [[Source](https://code.claude.com/docs/en/hooks-guide)]

* New troubleshooting for a hook whose JSON parses but does nothing. Two causes: extra stdout before the JSON (usually an `echo` in your shell profile), or a field at the wrong level — `permissionDecision` belongs inside `hookSpecificOutput`. Misplaced fields are silently ignored; find them with `claude --debug` and search the log for `Hook JSON output had unrecognized keys`. [[lines 996-1019](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/hooks-guide.md?plain=1#L996-L1019)] [[Source](https://code.claude.com/docs/en/hooks-guide#hook-json-has-no-effect)]

#### [iam](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/iam.md) [[Source](https://code.claude.com/docs/en/iam)]

* Same per-key exception rewrite as the authentication page. [[line 149](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/iam.md?plain=1#L149)] [[Source](https://code.claude.com/docs/en/iam#restrict-login-to-your-organization)]

#### [ide-integrations](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/ide-integrations.md) [[Source](https://code.claude.com/docs/en/ide-integrations)]

* New "Share a plugin install link" section documenting a `vscode://anthropic.claude-code/install-plugin` URL that opens VS Code on a plugin's scope choice. Nothing installs until a scope is picked, `marketplace` defaults to `anthropics/claude-plugins-official`, and the section warns that GitHub strips non-`http` schemes so the URL needs a code block there. [[lines 233-253](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/ide-integrations.md?plain=1#L233-L253)] [[Source](https://code.claude.com/docs/en/ide-integrations#share-a-plugin-install-link)]

#### [managed-settings](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/managed-settings.md) [[Source](https://code.claude.com/docs/en/managed-settings)]

* The gateway login keys follow a separate rule: never read from server-managed settings, so the highest-ranked admin source carrying a policy key supplies them regardless. [[line 169](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/managed-settings.md?plain=1#L169)] [[Source](https://code.claude.com/docs/en/managed-settings#keys-read-from-every-admin-source)]

#### [model-config](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* Documents pressing `s` in the model picker for a session-only switch (rebindable as `modelPicker:thisSessionOnly`), and clarifies that `/model <name>` typed directly behaves like `Enter`. [[lines 117-121](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/model-config.md?plain=1#L117-L121)] [[Source](https://code.claude.com/docs/en/model-config#setting-your-model)]

#### [monitoring-usage](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* New "Repository attributes" section: `OTEL_METRICS_INCLUDE_REPOSITORY=true` derives `vcs.repository.url.full`, `vcs.owner.name`, `vcs.repository.name` and `vcs.provider.name` once per session from the `origin` remote, with HTTPS and SSH remotes producing identical values. Credentials, query strings and fragments never appear; the attributes are omitted with no `origin`, a non-URL remote, or when the only enclosing repository is your home directory. **These flow only to your own exporters — Anthropic's telemetry drops every `vcs.*` key.** [[lines 481-498](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/monitoring-usage.md?plain=1#L481-L498)] [[Source](https://code.claude.com/docs/en/monitoring-usage#repository-attributes)]
* A batch of new bounded "safe" attributes that carry no user-chosen names, all requiring v2.1.268: `query_source_safe` (user-named agents collapse to `agent.custom`), `tool_name_safe` (MCP tools become `mcp_other` apart from a few fixed shapes), `bash_command_class`, `bash_argv0`, `error_class` and `first_content_ms`. [[lines 213-249](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/monitoring-usage.md?plain=1#L213-L249)] [[Source](https://code.claude.com/docs/en/monitoring-usage#span-attributes)]
* `vcs.ref.head.*` attributes on commit events under `OTEL_LOG_TOOL_DETAILS=1`, giving the SHA, branch and `branch` type of a successful `git commit`, omitted on a detached HEAD. [[lines 691-694](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/monitoring-usage.md?plain=1#L691-L694)] [[Source](https://code.claude.com/docs/en/monitoring-usage#tool-result-event)]
* New `parent.source` span attribute distinguishing `env` (parented under an inbound `TRACEPARENT`) from `none`. [[line 203](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/monitoring-usage.md?plain=1#L203)] [[Source](https://code.claude.com/docs/en/monitoring-usage#span-attributes)]
* Custom `OTEL_RESOURCE_ATTRIBUTES` keys still never override standard attributes — with `vcs.*` now the documented exception. [[line 358](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/monitoring-usage.md?plain=1#L358)] [[Source](https://code.claude.com/docs/en/monitoring-usage#multi-team-organization-support)]

#### [permission-modes](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/permission-modes.md) [[Source](https://code.claude.com/docs/en/permission-modes)]

* `dontAsk` restated as "reads and pre-approved tools; anything that would prompt is denied", and its section now names PreToolUse hook approvals as another thing that still runs. [[lines 19-489](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/permission-modes.md?plain=1#L19-L489)] [[Source](https://code.claude.com/docs/en/permission-modes#available-modes)]

#### [permissions](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/permissions.md) [[Source](https://code.claude.com/docs/en/permissions)]

* Symlink deny rules now apply when *either* the symlink path or its target matches, with a worked example: `./project/key` pointing at `~/.ssh/id_rsa` is blocked. A rule written through a symlinked directory also applies at the real location — before v2.1.268 it didn't. [[lines 404-406](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/permissions.md?plain=1#L404-L406)] [[Source](https://code.claude.com/docs/en/permissions#read-and-edit)]
* Artifact reads carved out of bare `WebFetch` rules: you now need a `domain:` rule covering `claude.ai` or `*.claudeusercontent.com`, or an `Artifact` rule. Before v2.1.268 a bare deny rule blocked every artifact read. [[lines 435-437](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/permissions.md?plain=1#L435-L437)] [[Source](https://code.claude.com/docs/en/permissions#allow-or-deny-every-fetch)]

#### [plugins](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/plugins.md) [[Source](https://code.claude.com/docs/en/plugins)]

* New pointer from plugin development to `claude plugin eval` for measuring how often Claude actually reaches for the plugin. [[lines 299-454](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/plugins.md?plain=1#L299-L454)] [[Source](https://code.claude.com/docs/en/plugins#test-your-plugins-locally)]

#### [plugins-reference](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/plugins-reference.md) [[Source](https://code.claude.com/docs/en/plugins-reference)]

* New `plugin eval` and `plugin eval init` command reference sections with their full option tables and exit codes: 0 when every case meets the threshold, 1 on a failing case or untrusted directory, 2 on a partial run, 130 interrupted, 143 terminated. [[lines 1246-1293](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/plugins-reference.md?plain=1#L1246-L1293)] [[Source](https://code.claude.com/docs/en/plugins-reference#plugin-eval)]
* New `experimental.evals` manifest field for a non-default eval directory. [[line 540](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/plugins-reference.md?plain=1#L540)] [[Source](https://code.claude.com/docs/en/plugins-reference#component-path-fields)]
* Every CLI command section gained explicit "The command takes these arguments" / "accepts these options" lead-ins, and the `new`, `remove`/`rm` and `autoremove` aliases are now documented. [[lines 932-1067](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/plugins-reference.md?plain=1#L932-L1067)] [[Source](https://code.claude.com/docs/en/plugins-reference#plugin-init)]

#### [sandbox-environments](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/sandbox-environments.md) [[Source](https://code.claude.com/docs/en/sandbox-environments)]

* Sharpened the boundary: the sandboxed Bash tool restricts Bash only — file tools, MCP servers and hooks still run directly on your host, while every other approach in the table puts the whole process inside the boundary. [[lines 24-68](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/sandbox-environments.md?plain=1#L24-L68)] [[Source](https://code.claude.com/docs/en/sandbox-environments#compare-sandboxing-approaches)]

#### [server-managed-settings](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/server-managed-settings.md) [[Source](https://code.claude.com/docs/en/server-managed-settings)]

* A third class of no-merge exception: gateway sign-in keys, never read from server-managed settings. [[line 144](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/server-managed-settings.md?plain=1#L144)] [[Source](https://code.claude.com/docs/en/server-managed-settings#per-key-exceptions-across-managed-sources)]
* `ANTHROPIC_CUSTOM_HEADERS` approval now depends on the delivered value: tagging headers such as `Accept-Language` apply silently, while anything naming a credential, org selector, routing override or API-behavior header requires approval. The check matches words *inside* the name, so `X-Client-Version` needs approval. Before v2.1.251 any value applied without the dialog. [[line 282](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/server-managed-settings.md?plain=1#L282)] [[Source](https://code.claude.com/docs/en/server-managed-settings#environment-variables-and-the-approval-dialog)]

#### [settings-reference](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/settings-reference.md) [[Source](https://code.claude.com/docs/en/settings-reference)]

* New `managedSourcesBehavior` documentation defining a "policy key" as any settings key other than itself and `wslInheritsWindowsSettings`, and explaining that `"merge"` combines every admin source. Requires v2.1.242. [[line 5571](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/settings-reference.md?plain=1#L5571)] [[Source](https://code.claude.com/docs/en/settings-reference#managedsourcesbehavior)]
* New table row listing the keys read only from the highest-priority source, and a following list of keys with extra conditions. [[lines 5598-5608](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/settings-reference.md?plain=1#L5598-L5608)] [[Source](https://code.claude.com/docs/en/settings-reference#managedsourcesbehavior)]
* `/effort ultracode` documented as a per-session override needing no settings key. [[line 1247](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/settings-reference.md?plain=1#L1247)] [[Source](https://code.claude.com/docs/en/settings-reference#ultracode)]

#### [setup](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/setup.md) [[Source](https://code.claude.com/docs/en/setup)]

* How to confirm `DISABLE_AUTOUPDATER` took effect: `claude doctor` should show `disabled (set by env: DISABLE_AUTOUPDATER)`. [[line 259](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/setup.md?plain=1#L259)] [[Source](https://code.claude.com/docs/en/setup#disable-auto-updates)]

#### [skills](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)]

* Distinguishes the two eval tools: `claude plugin eval` for a skill that ships in a plugin, and the skill-creator plugin's own `evals/evals.json` for iterating inside a conversation. **The two formats aren't interchangeable.** [[lines 790-1029](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/skills.md?plain=1#L790-L1029)] [[Source](https://code.claude.com/docs/en/skills#evaluate-and-iterate-on-a-skill)]

#### [slash-commands](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/slash-commands.md) [[Source](https://code.claude.com/docs/en/slash-commands)]

* Carries the same eval-tooling guidance as the skills page.

#### [terminal-config](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/terminal-config.md) [[Source](https://code.claude.com/docs/en/terminal-config)]

* Terminals speaking the kitty keyboard protocol, such as foot and Alacritty 0.16+, now work without `/terminal-setup` on v2.1.269. Alacritty before 0.16 and Zed still need it, and the page warns to run it in the host terminal rather than inside tmux or screen. [[lines 26-30](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/terminal-config.md?plain=1#L26-L30)] [[Source](https://code.claude.com/docs/en/terminal-config#enter-multiline-prompts)]

#### [tools-reference](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/tools-reference.md) [[Source](https://code.claude.com/docs/en/tools-reference)]

* **Glob and Grep are absent by default on macOS, Linux and WSL.** Claude searches with `find` and `grep` through the Bash tool, which run embedded `bfs` and `ugrep`, so searches now arrive at your hooks and permission rules as `Bash` calls rather than `Glob`/`Grep` calls. On Windows both remain in the default set. [[lines 28-256](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/tools-reference.md?plain=1#L28-L256)] [[Source](https://code.claude.com/docs/en/tools-reference#tools-reference)]
* Three ways to get them back: name them in `--tools` or `--allowedTools` at startup (naming either in `--allowedTools` restores both, and an allow rule in a settings file does **not** have this effect); remove `Bash` from the session with a deny rule, `--disallowedTools` or `--restricted`; or have a subagent list them in `tools` while leaving out `Bash`. [[lines 258-262](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/tools-reference.md?plain=1#L258-L262)] [[Source](https://code.claude.com/docs/en/tools-reference#glob-tool-behavior)]

#### [troubleshoot-install](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/troubleshoot-install.md) [[Source](https://code.claude.com/docs/en/troubleshoot-install)]

* Added a next step when `downloads.claude.ai` is reachable but the install failed: the failure was likely intermittent, so retry or try another install method. [[line 378](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/troubleshoot-install.md?plain=1#L378)] [[Source](https://code.claude.com/docs/en/troubleshoot-install#curl-56-failure-writing-output-to-destination)]

#### [vs-code](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/vs-code.md) [[Source](https://code.claude.com/docs/en/vs-code)]

* Carries the same `install-plugin` deep-link section as the IDE integrations page.

#### [web-quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/web-quickstart.md) [[Source](https://code.claude.com/docs/en/web-quickstart)]

* Onboarding now states plainly that a browser GitHub connection clones any public repository but reaches a private one only where the Claude GitHub App is installed — and that an organization owner may need to approve the installation. [[line 61](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/web-quickstart.md?plain=1#L61)] [[Source](https://code.claude.com/docs/en/web-quickstart#connect-github)]
* New "Remove the `/web-setup` token" section: disconnecting GitHub at claude.ai/customize/connectors deletes the stored credentials but leaves your local `gh` signed in and the token valid on GitHub. To invalidate it, revoke the **GitHub CLI** OAuth app entry — which also signs `gh` out on your machines. [[lines 108-114](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/web-quickstart.md?plain=1#L108-L114)] [[Source](https://code.claude.com/docs/en/web-quickstart#connect-from-your-terminal)]
* Spells out what `/web-setup` does with your token: Claude Code reads `gh auth token`, asks you to confirm, and sends it to Anthropic, which stores it encrypted against your claude.ai account. On Team and Enterprise it's available only after an Owner turns on Quick web setup. [[lines 78-82](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/web-quickstart.md?plain=1#L78-L82)] [[Source](https://code.claude.com/docs/en/web-quickstart#connect-from-your-terminal)]
* `/web-setup` now creates a cloud environment with Trusted network access if you have none. [[line 106](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/web-quickstart.md?plain=1#L106)] [[Source](https://code.claude.com/docs/en/web-quickstart#connect-from-your-terminal)]
* New troubleshooting for "No repositories appear after connecting GitHub", split by connection method. [[lines 185-187](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/claude-code/web-quickstart.md?plain=1#L185-L187)] [[Source](https://code.claude.com/docs/en/web-quickstart#no-repositories-appear-after-connecting-github)]

-----

## API changes

### Changed documents

#### [agents-and-tools/tool-use/browser-use-tool](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/api/agents-and-tools/tool-use/browser-use-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool)]

* New "Report downloads" behavior: the API renders each download entry into a line of text for Claude, after the result's text and before the Tab Context footer, carrying `download_id`, `url`, and `path`/`size_bytes` or `error`. A result with no text block gets them as a text block of its own. [[lines 1405-1437](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/api/agents-and-tools/tool-use/browser-use-tool.md?plain=1#L1405-L1437)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool#report-downloads)]
* Expanded prompt-injection guidance: tab URLs render **verbatim**, so sanitize them yourself, while titles are escaped by the API — meaning a pre-escaped title reaches Claude double-escaped. A download's `url`, `path` and `error` are untrusted too, and the API's length limits are "a floor, not a defense". [[lines 1108-1291](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/api/agents-and-tools/tool-use/browser-use-tool.md?plain=1#L1108-L1291)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool#security-considerations)]
* Clarified that an image-only result renders nothing and defers tab context to the next result carrying text — unless it reports a download event. [[line 1359](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/api/agents-and-tools/tool-use/browser-use-tool.md?plain=1#L1359)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool#tab-context-on-other-results)]

#### [api/errors](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/api/api/errors.md) [[Source](https://platform.claude.com/docs/en/api/errors)]

* The thinking-block signature error now names the `thinking-binding-controls-2026-08-01` beta header when it's absent, and points at `prefix_mismatch_behavior: "drop_block"` as the way to continue. A block from a model the target can't read is dropped rather than rejected. [[line 504](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/api/api/errors.md?plain=1#L504)] [[Source](https://platform.claude.com/docs/en/api/errors#thinking-block-no-longer-matches-the-conversation)]

#### [build-with-claude/context-editing](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/api/build-with-claude/context-editing.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/context-editing)]

* On Fable 5.1, server-side context management never invalidates thinking blocks, but client-side edits to earlier turns invalidate every later assistant turn's. For accounts created on or after August 31, 2026, replaying an invalidated block is rejected unless you opt into dropping it. [[line 59](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/api/build-with-claude/context-editing.md?plain=1#L59)] [[Source](https://platform.claude.com/docs/en/build-with-claude/context-editing#context-editing-happens-server-side)]

#### [build-with-claude/thinking](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/api/build-with-claude/thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/thinking)]

* New guidance on switching models mid-conversation: keep passing thinking blocks back unchanged. A block is readable only by its producing model or a newer one, so switching **up** to Fable 5.1 or Mythos 5.1 keeps the conversation's reasoning while switching down drops it. Never strip blocks when redeeming a fallback credit, which requires the body unchanged. [[line 989](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/api/build-with-claude/thinking.md?plain=1#L989)] [[Source](https://platform.claude.com/docs/en/build-with-claude/thinking#thinking-block-preservation-by-model)]

#### [cli-sdks-libraries/cli/apply](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/api/cli-sdks-libraries/cli/apply.md) [[Source](https://platform.claude.com/docs/en/cli-sdks-libraries/cli/apply)]

* Documents that resources refer to each other by relative file path wherever the API expects an ID, and that `ant apply` creates them in dependency order and fills in the real IDs. [[line 105](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/api/cli-sdks-libraries/cli/apply.md?plain=1#L105)] [[Source](https://platform.claude.com/docs/en/cli-sdks-libraries/cli/apply#grow-it-into-a-project)]

#### [manage-claude/cmek](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/api/manage-claude/cmek.md) [[Source](https://platform.claude.com/docs/en/manage-claude/cmek)]

* A much fuller list of what CMEK turns off: chat search (titles and content are encrypted under your key, so the **Search and reference chats** toggle stays off), Claude Code on the web and routines, Claude in Slack, organization data and audit log exports, and response ratings. Claude Code Desktop stays available for local sessions but is off until an admin enables it. [[lines 88-93](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/api/manage-claude/cmek.md?plain=1#L88-L93)] [[Source](https://platform.claude.com/docs/en/manage-claude/cmek#disabled-or-modified)]
* Claude Science data sent to users' own compute, such as SSH hosts or cloud accounts, is held on those systems and isn't covered. [[line 72](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/api/manage-claude/cmek.md?plain=1#L72)] [[Source](https://platform.claude.com/docs/en/manage-claude/cmek#encrypted-with-cmek-key)]

#### [manage-claude/inference-hooks](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/api/manage-claude/inference-hooks.md) [[Source](https://platform.claude.com/docs/en/manage-claude/inference-hooks)]

* Added a flow diagram and a walkthrough of which points are hooked — step 1 where the prompt arrives and step 6 where the tool result returns, each triggering a validation exchange with your AI security server. [[lines 26-28](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/api/manage-claude/inference-hooks.md?plain=1#L26-L28)] [[Source](https://platform.claude.com/docs/en/manage-claude/inference-hooks#how-inference-hooks-work)]

#### [models/fable-5-1/migration-guide](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/api/models/fable-5-1/migration-guide.md) [[Source](https://platform.claude.com/docs/en/models/fable-5-1/migration-guide)]

* When a Fable 5.1 conversation lands on an older model through a router switch, retry or classifier fallback, the API removes unreadable blocks, the request succeeds, and you aren't billed for the dropped tokens — but the target re-plans without that reasoning, raising first-turn cost and latency. The `thinking-binding-controls-2026-08-01` header surfaces each drop in an `input_transformations` array. [[line 929](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/api/models/fable-5-1/migration-guide.md?plain=1#L929)] [[Source](https://platform.claude.com/docs/en/models/fable-5-1/migration-guide#breaking-changes)]

#### [models/fable-5-1/whats-new-fable-5-1](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/api/models/fable-5-1/whats-new-fable-5-1.md) [[Source](https://platform.claude.com/docs/en/models/fable-5-1/whats-new-fable-5-1)]

* Without the beta header the drop is **silent**, which is the operative warning here. [[line 47](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/api/models/fable-5-1/whats-new-fable-5-1.md?plain=1#L47)] [[Source](https://platform.claude.com/docs/en/models/fable-5-1/whats-new-fable-5-1#earlier-models-cant-read-claude-fable-51-thinking-blocks)]
* Practical recipe for keeping thinking valid across a long session: treat the conversation as append-only, add instructions via mid-conversation system messages, change tools via mid-conversation tool changes, and trim with server-side context editing or compaction, which don't count as edits. To find out whether your integration edits history, run with `prefix_mismatch_behavior: "drop_block"` and log `input_transformations`. [[line 64](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/api/models/fable-5-1/whats-new-fable-5-1.md?plain=1#L64)] [[Source](https://platform.claude.com/docs/en/models/fable-5-1/whats-new-fable-5-1#editing-earlier-turns-invalidates-thinking-blocks)]

#### [models/fable-5/migration-guide](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/api/models/fable-5/migration-guide.md) [[Source](https://platform.claude.com/docs/en/models/fable-5/migration-guide)]

* The "strip thinking blocks before replaying on an earlier model" advice now carries an exception in both places: keep them when moving a conversation **up** to Fable 5.1 or Mythos 5.1, and never strip when redeeming a fallback credit. [[lines 319-687](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/api/models/fable-5/migration-guide.md?plain=1#L319-L687)] [[Source](https://platform.claude.com/docs/en/models/fable-5/migration-guide#migration-checklist)]

#### [api/compliance](https://github.com/gpambrozio/ClaudeDocs/blob/a8905ddd46628feab3e79423cc6c150d518c5031/docs-md/api/api/compliance.md) [[Source](https://platform.claude.com/docs/en/api/compliance)]

* An upstream generation fix removed thousands of lines of repeated boilerplate ("Automated background processing performed by Anthropic systems…" and its asserting-party note) from the compliance reference and its `activities` pages. No described behavior changed. The same de-duplication trimmed repeated tool and content-block descriptions from the `beta/messages` and `messages` reference pages across every SDK language.
