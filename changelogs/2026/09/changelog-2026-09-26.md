# [Claude docs changes for September 26th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/7801578b358e9e48ac6b406957c9c4abb5d1c625) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/7801578b358e9e48ac6b406957c9c4abb5d1c625)]

## Executive Summary

- Auto mode is now the built-in starting permission mode for interactive terminal and VS Code sessions on **every** plan and provider (not just Pro/Max/Team), and critical-path `rm`/`rmdir` removals in auto mode now prompt in the terminal with a two-minute countdown instead of always going to the classifier.
- Projects gained **"Run a thread on your own computer"**: a project thread can now run locally through Remote Control (from the Desktop app or `claude remote-control`) when a task needs your filesystem, MCP servers, or local tools.
- New managed model-restriction settings `deniedModels` and `availableModelsMatch` let admins block a specific model version (e.g. Opus 5.5) even when a broader `availableModels` entry would otherwise permit it.
- Claude Code gained a per-session **scratchpad directory** for Claude's temporary files (replacing ad hoc use of `/tmp`), and MCP tool image results are now saved to disk so other tools can reuse the full-resolution file.
- Anthropic's plugin **community marketplace submission process was replaced by a new "directory"** submitted through a developer portal, which lists a plugin on claude.ai, Cowork, and Claude Code together.

## New Claude Code versions

### [2.1.283](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/versions/2.1.283.md)

#### New features

* Added `x-claude-code-prompt-id` to the gateway hint headers so LLM gateways can group the requests that serve one user prompt; opt in with `CLAUDE_CODE_GATEWAY_HINT_HEADERS=1`
* Added `availableModelsMatch` managed setting: with `"exact"`, an `availableModels` entry allows only the model version it names, so new releases stay blocked until listed
* Added `deniedModels` managed setting to block specific models, even when `availableModels` allows them
* Added MCP tool, WebFetch, and WebSearch outputs to the `tool.output` OpenTelemetry span event when `OTEL_LOG_TOOL_CONTENT=1`
* Added `/doctor prompt-audit` (also `/checkup prompt-audit`) to audit CLAUDE.md files, skills, agents, and commands for prompting patterns written for older models
* Added click-to-expand for truncated messages from your other sessions in fullscreen mode
* Added `path` to `--plugin-dir` load-failure entries in the stream-json `system/init` `plugin_errors`, naming the directory that didn't load
* Added an opt-in `load_test_mode` block to the Claude apps gateway config so a deployment can be load tested without calling a model provider
* Added a `mantle` upstream provider to the Claude apps gateway for Amazon Bedrock's Mantle endpoint

#### Existing feature improvements

* Improved the `/mcp` tool list: shows more tools at once, scrolls with the page keys and mouse, and marks org-blocked tools
* Improved MCP tool results: images returned by MCP tools are now also saved to a file so Bash, Read, and other tools can open them
* Improved `/tasks` and other pickers (`/help`, `/hooks`, `/copy`, `/chrome`, `/memory`, `/ide`, `/release-notes`, `/rewind`, `/diff`, `/remote-env`, `/plugin`, `/skills`, `/artifacts`) with page keys, mouse wheel, and clicks
* Improved the compaction spinner: timer starts when compaction begins and counts the summary's tokens as they stream
* Improved the Skill tool's reply when a skill's plugin failed to load, so Claude reports the plugin failure instead of calling the skill uninstalled
* Improved first-reply and first-request latency, and startup time for `claude -p`, Remote Control, and cold claude.ai accounts
* Changed interactive sessions on third-party providers or with telemetry off to start in auto mode when no permission mode is configured
* Changed `--system-prompt` and `--append-system-prompt` to accept their text and `-file` forms together
* Changed artifact watching: an auto-armed watch now ends after 3.5 hours with no activity

#### Major bug fixes

* Fixed SDK sessions losing a deferred tool call or finished tool result when a turn ended early
* Fixed MCP progress notifications being discarded once a long-running tool call moved to the background
* Fixed stdio MCP servers being left running when the session ended while they were still starting
* Fixed a brief HTTP 404 from a stateless remote MCP server leaving that server unusable for the rest of the session
* Fixed the weekly Fable limit not appearing in `/usage` and the VS Code usage meters when telemetry is disabled
* Fixed dynamic workflows started during a model fallback running every agent on the fallback model instead of retrying the configured model
* Fixed `DISABLE_PROMPT_CACHING_HAIKU` having no effect when Haiku is the session's main model
* Fixed several `claude plugin` bugs: `validate` accepting names it can't install and skipping `outputStyles`/`lspServers`/`monitors`/`themes` paths, `details` showing 0 MCP servers, `marketplace remove` not naming uninstalled plugins, `uninstall` removing the wrong of two case-differing plugin ids, and `installed_plugins.json` losing records or showing no plugins when it holds a bad entry
* Fixed `/context` not counting MCP server instructions
* Fixed `claude mcp add`, `add-json`, and `remove` reporting success when the config file couldn't actually be written
* Fixed Remote Control being unavailable on paid plans when telemetry is turned off with `DISABLE_TELEMETRY` or `DO_NOT_TRACK`
* Fixed managed `sandbox` settings being ignored entirely when one nested value was invalid
* Windows: Fixed the PowerShell tool letting `cmd /c rd`, `rmdir`, `del`, or `erase` delete drive roots and other protected folders
* [VSCode] Fixed a session teleported from the web dropping messages sent while Claude was working
* [Code Review] Fixed "@claude review" requests going silent when GitHub failed to return the pull request
* [Code Review] Fixed billing for a review that stopped at its time limit with nothing verified

-----

## Claude Code changes

### Changed documents

#### [accessibility](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/accessibility.md) [[Source](https://code.claude.com/docs/en/accessibility)]

* The screen-reader prompt for menus and permission dialogs changed from `Enter selection` to `Select with numbers`. [[line 95](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/accessibility.md?plain=1#L95)] [[Source](https://code.claude.com/docs/en/accessibility#jump-between-turns)]

#### [advisor](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/advisor.md) [[Source](https://code.claude.com/docs/en/advisor)]

* Added an **Unavailable** advisor status line for when the advisor call itself fails, showing the error code. [[line 140](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/advisor.md?plain=1#L140)] [[Source](https://code.claude.com/docs/en/advisor#what-you-see-during-a-session)]

#### [agent-sdk/hosting](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/agent-sdk/hosting.md) [[Source](https://code.claude.com/docs/en/agent-sdk/hosting)]

* Documented the new TypeScript `prewarm()` call for pre-warming a container process before a session's working directory is known. [[line 105](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/agent-sdk/hosting.md?plain=1#L105)] [[Source](https://code.claude.com/docs/en/agent-sdk/hosting#long-running-sessions)]

#### [agent-sdk/mcp](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/agent-sdk/mcp.md) [[Source](https://code.claude.com/docs/en/agent-sdk/mcp)]

* In-process SDK MCP servers now have an explicit `MCP_TIMEOUT` first-turn wait per connect attempt, instead of no documented timeout. [[line 134](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/agent-sdk/mcp.md?plain=1#L134)] [[Source](https://code.claude.com/docs/en/agent-sdk/mcp#connection-timing)]

#### [agent-sdk/observability](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/agent-sdk/observability.md) [[Source](https://code.claude.com/docs/en/agent-sdk/observability)]

* `OTEL_LOG_TOOL_CONTENT=1` now also captures what MCP tools, WebFetch, and WebSearch return (Claude Code v2.1.283+). [[line 220](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/agent-sdk/observability.md?plain=1#L220)] [[Source](https://code.claude.com/docs/en/agent-sdk/observability#control-sensitive-data-in-exports)]

#### [agent-sdk/permissions](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/agent-sdk/permissions.md) [[Source](https://code.claude.com/docs/en/agent-sdk/permissions)]

* Clarified that `rm`/`rmdir` removals targeting a critical path are never auto-approved and, in an Agent SDK session in `auto` mode, are denied by default without reaching `canUseTool`. [[lines 35-45](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/agent-sdk/permissions.md?plain=1#L35-L45)] [[Source](https://code.claude.com/docs/en/agent-sdk/permissions#how-permissions-are-evaluated)]

#### [agent-sdk/plugins](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/agent-sdk/plugins.md) [[Source](https://code.claude.com/docs/en/agent-sdk/plugins)]

* "Plugin not loading" troubleshooting now points first at the init message's new `plugin_errors` field. [[line 285](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/agent-sdk/plugins.md?plain=1#L285)] [[Source](https://code.claude.com/docs/en/agent-sdk/plugins#troubleshooting)]

#### [agent-sdk/python](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/agent-sdk/python.md) [[Source](https://code.claude.com/docs/en/agent-sdk/python)]

* Added the `verbatim_prompts` option: deliver every prompt as written (`client_composed: True`) instead of expanding `@` mentions or running `/` commands. Requires Python Agent SDK 0.2.158+ and Claude Code v2.1.248+. [[line 810](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/agent-sdk/python.md?plain=1#L810)] [[Source](https://code.claude.com/docs/en/agent-sdk/python#claudeagentoptions)]

#### [agent-sdk/typescript](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* Added a new `@anthropic-ai/claude-agent-sdk/core` entry point for apps that bundle the Agent SDK, which drops `zod`/MCP SDK inlining and some root-only exports. [[line 44](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L44)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#compile-to-a-single-executable)]
* Added `prewarm()`, `SpareProcess`, and `.claim()` (alpha): start a spare Claude Code process before you know which session or folder it will serve. [[line 117](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L117)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#example)]
* Added the `verbatimPrompts` option and `client_composed` message field, matching the Python SDK's `verbatim_prompts`. [[line 519](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L519)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#options)]
* Added `SpareProcess` (`claim`, `claimed`, `exited`, `close`) as the return type of `prewarm()`. [[line 698](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L698)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#methods)]
* Documented `SDKSystemMessage.plugin_errors`, listing which plugin failed to load and why. [[line 1626](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L1626)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#sdksystemmessage)]
* `SDKTaskProgressMessage.summary` now also carries an MCP server's latest reported progress for a backgrounded MCP tool call, not just subagent progress summaries. [[line 5104](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L5104)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#sdktaskstartedmessage)]
* `SDKCommandsChangedMessage` is now also emitted when an MCP server's prompts join or leave the command list (v2.1.281+). [[line 5255](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L5255)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#sdkcommandschangedmessage)]
* `SDKConversationResetMessage` gained optional `trigger`, `user_message_uuid`, and `timestamp` fields describing what caused the reset (v2.1.281+). [[line 5290](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L5290)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#sdkconversationresetmessage)]

#### [agent-teams](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/agent-teams.md) [[Source](https://code.claude.com/docs/en/agent-teams)]

* Teammates now inherit a `--setting-sources` restriction from the lead; before v2.1.281, split-pane teammates loaded every settings source. [[line 283](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/agent-teams.md?plain=1#L283)] [[Source](https://code.claude.com/docs/en/agent-teams#messages-between-agents)]

#### [agent-view](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/agent-view.md) [[Source](https://code.claude.com/docs/en/agent-view)]

* Added `--setting-sources` as a configuration flag agent view carries through to dispatched sessions. [[line 428](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/agent-view.md?plain=1#L428)] [[Source](https://code.claude.com/docs/en/agent-view#from-your-shell)]
* `claude --bg` (and background-session restarts) now check workspace trust for the target directory before starting. [[line 428](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/agent-view.md?plain=1#L428)] [[Source](https://code.claude.com/docs/en/agent-view#from-your-shell)]
* A worktree with only uncommitted changes in a verifiable checked-out submodule no longer blocks "delete again to remove the directory anyway". [[line 544](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/agent-view.md?plain=1#L544)] [[Source](https://code.claude.com/docs/en/agent-view#what-deleting-a-session-removes)]

#### [agents](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/agents.md) [[Source](https://code.claude.com/docs/en/agents)]

* The "Projects" row now notes threads can run in the cloud or, when asked, on your computer through Remote Control. [[line 4](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/agents.md?plain=1#L4)] [[Source](https://code.claude.com/docs/en/agents#run-agents-in-parallel)]

#### [authentication](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/authentication.md) [[Source](https://code.claude.com/docs/en/authentication)] / [iam](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/iam.md)

* Added Windows PowerShell and CMD examples for setting `CLAUDE_CODE_OAUTH_TOKEN`, alongside the existing bash example. [[line 245](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/authentication.md?plain=1#L245)] [[Source](https://code.claude.com/docs/en/authentication#generate-a-long-lived-token)]

#### [best-practices](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/best-practices.md) [[Source](https://code.claude.com/docs/en/best-practices)]

* Auto mode is now the built-in starting permission mode on **every** plan with Claude Code v2.1.283+, not just Pro/Max/Team. [[line 175](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/best-practices.md?plain=1#L175)] [[Source](https://code.claude.com/docs/en/best-practices#configure-permissions)]
* The Stop hook's fixed 8-consecutive-block cap is now described as configurable rather than hardcoded. [[line 38](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/best-practices.md?plain=1#L38)] [[Source](https://code.claude.com/docs/en/best-practices#give-claude-a-way-to-verify-its-work)]

#### [claude-apps-gateway-config](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/claude-apps-gateway-config.md) [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config)]

* Added "Add your own labels": `telemetry.resource_attributes` lets a gateway operator push fixed OpenTelemetry resource labels (like `service.namespace`) with every session's telemetry (v2.1.281+ on the gateway server). [[line 888](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/claude-apps-gateway-config.md?plain=1#L888)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config#telemetry)]
* Clarified `load_test_mode`: a replica's CPU-per-request estimate reads lower than production since no request actually leaves for the provider. [[line 998](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/claude-apps-gateway-config.md?plain=1#L998)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config#load_test_mode)]

#### [claude-code-on-the-web](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/claude-code-on-the-web.md) [[Source](https://code.claude.com/docs/en/claude-code-on-the-web)]

* In Anthropic-hosted environments, GitHub credentials now stay encrypted on Anthropic's servers and never enter the session VM; traffic goes through a server-side GitHub proxy instead. [[line 49](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L49)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#github-authentication-options)]
* Added a "Time limits" constraint pointing to the new cloud-environments time-limits section. [[line 351](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L351)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#limitations)]

#### [claude-directory](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/claude-directory.md) [[Source](https://code.claude.com/docs/en/claude-directory)]

* Added a **Session scratchpad directory**: a per-session temp directory Claude uses instead of `/tmp` for intermediate files, helper scripts, and drafts, without a permission prompt. [[line 1342](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/claude-directory.md?plain=1#L1342)] [[Source](https://code.claude.com/docs/en/claude-directory#cleaned-up-automatically)]
* `tool-results/` now also holds full-size copies of images MCP tools return. [[line 1314](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/claude-directory.md?plain=1#L1314)] [[Source](https://code.claude.com/docs/en/claude-directory#cleaned-up-automatically)]

#### [claude-md](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/claude-md.md) [[Source](https://code.claude.com/docs/en/claude-md)] / [memory](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/memory.md)

* A `.claude/rules/` or `CLAUDE.md` symlink pointed at a network path (UNC share, `/net`, `/Network`) is no longer followed, to avoid contacting the host it names. [[line 237](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/claude-md.md?plain=1#L237)] [[Source](https://code.claude.com/docs/en/claude-md#share-rules-across-projects-with-symlinks)]
* Added a startup/`​/status` warning when an instruction file exceeds the recommended length, or several files together exceed a combined limit. [[line 569](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/claude-md.md?plain=1#L569)] [[Source](https://code.claude.com/docs/en/claude-md#my-claudemd-is-too-large)]

#### [claude-projects](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/claude-projects.md) [[Source](https://code.claude.com/docs/en/claude-projects)]

* Added **"Run a thread on your own computer"**: choose **Work locally** in a project conversation to run that task's thread through Remote Control on a connected machine (Desktop app or `claude remote-control`, v2.1.280+), instead of in the cloud. Covers connecting the folder, the approval card, auto mode behavior, and the "Lost contact with your folder" and new error states. [[line 245](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/claude-projects.md?plain=1#L245)] [[Source](https://code.claude.com/docs/en/claude-projects#run-a-thread-on-your-own-computer)]

#### [cli-reference](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* `--agents` can now take the path to a JSON file (with `--print`), for definitions too large for the command line (v2.1.281+). [[line 324](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/cli-reference.md?plain=1#L324)] [[Source](https://code.claude.com/docs/en/cli-reference#see-also)]
* `--bg` now checks workspace trust for the target directory before it starts. [[line 334](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/cli-reference.md?plain=1#L334)] [[Source](https://code.claude.com/docs/en/cli-reference#see-also)]

#### [cloud-environments](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/cloud-environments.md) [[Source](https://code.claude.com/docs/en/cloud-environments)]

* Added a **Time limits** section: command timeouts, `SessionStart` hook's 600s default, the setup-script ~5-minute caching cutoff, and idle-session expiry, plus `BASH_DEFAULT_TIMEOUT_MS`/`BASH_MAX_TIMEOUT_MS` to raise them. [[line 351](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/cloud-environments.md?plain=1#L351)] [[Source](https://code.claude.com/docs/en/cloud-environments#time-limits)]

#### [code-review](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/code-review.md) [[Source](https://code.claude.com/docs/en/code-review)]

* Code Review now automatically retries some interrupted reviews; check the run's summary before manually retriggering. Check-run titles changed to e.g. **Code review failed**. [[line 255](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/code-review.md?plain=1#L255)] [[Source](https://code.claude.com/docs/en/code-review#pricing)]

#### [costs](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/costs.md) [[Source](https://code.claude.com/docs/en/costs)]

* New "Subagents and workflows" note: every subagent and workflow-spawned agent sends its own requests, which count toward usage; the attribution breakdown shows the subagent share. [[line 344](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/costs.md?plain=1#L344)] [[Source](https://code.claude.com/docs/en/costs#why-usage-climbs-in-a-long-session)]

#### [data-usage](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/data-usage.md) [[Source](https://code.claude.com/docs/en/data-usage)]

* Clarified cloud-session data handling: Anthropic stores the session transcript, and GitHub credentials are encrypted server-side and never enter the VM. [[line 88](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/data-usage.md?plain=1#L88)] [[Source](https://code.claude.com/docs/en/data-usage#cloud-execution-data-flow-and-dependencies)]

#### [discover-plugins](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/discover-plugins.md) [[Source](https://code.claude.com/docs/en/discover-plugins)]

* Clarified that committing a project-scope plugin entry turns it on for collaborators but doesn't download it; each collaborator must also run `claude plugin install` once. [[line 125](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/discover-plugins.md?plain=1#L125)] [[Source](https://code.claude.com/docs/en/discover-plugins#choose-an-install-scope)]

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* Added `CLAUDE_CODE_DISABLE_DANGEROUS_RM_TIMEOUT`, `CLAUDE_CODE_DISABLE_POWERSHELL_CMD_RM_DENY`, and `CLAUDE_CODE_DISABLE_SUBSTITUTION_RM_PROMPT` to opt out of the new critical-path removal checks. [[line 9](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/env-vars.md?plain=1#L9)] [[Source](https://code.claude.com/docs/en/env-vars#environment-variables)]
* `DISABLE_PROMPT_CACHING_HAIKU` now disables caching for the default Haiku model wherever it runs, including as your main model. [[line 26](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/env-vars.md?plain=1#L26)] [[Source](https://code.claude.com/docs/en/env-vars#in-your-shell)]
* With feature-flag fetching off, Remote Control's availability now depends on the specific variable set, rather than blanket unavailability. [[line 46](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/env-vars.md?plain=1#L46)] [[Source](https://code.claude.com/docs/en/env-vars#in-your-shell)]

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* Documented dozens of new/changed error messages, including: `Couldn't save your login` (macOS keychain locked) and `Could not refresh your login because another Claude Code process is refreshing it`; `Part of the response never arrived` / `The response stream was malformed` for dropped or duplicated stream events; new disk-quota/temp-filesystem-full errors (EDQUOT/ENOSPC); a reserved-name notice for skills/commands/workflows named inside the `anthropic-skills` namespace; `Claude Code can't start: your organization's managed settings block the default model`; and Desktop-app-specific wording for several auth and usage-limit messages. [[line 231](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/errors.md?plain=1#L231)] [[Source](https://code.claude.com/docs/en/errors#find-your-error)]

#### [fullscreen](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/fullscreen.md) [[Source](https://code.claude.com/docs/en/fullscreen)]

* Overflowing list panels (`/skills`, `/mcp`, `/plugin`'s Installed list) now show a clickable/draggable scrollbar (v2.1.281+). [[line 91](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/fullscreen.md?plain=1#L91)] [[Source](https://code.claude.com/docs/en/fullscreen#use-the-mouse)]
* A dim `Message from @<sender>` line from a teammate or other running agent is now click-to-expand. [[line 87](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/fullscreen.md?plain=1#L87)] [[Source](https://code.claude.com/docs/en/fullscreen#use-the-mouse)]

#### [headless](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/headless.md) [[Source](https://code.claude.com/docs/en/headless)]

* Resuming a `-p`/SDK session interrupted by SIGTERM no longer auto-continues the unfinished turn by default; set `CLAUDE_CODE_RESUME_INTERRUPTED_TURN=1` to restore the old behavior. [[line 75](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/headless.md?plain=1#L75)] [[Source](https://code.claude.com/docs/en/headless#stop-a-run-with-sigterm)]
* Added a new warning message when a `-p`/SDK session's working directory is deleted mid-session; shell commands fail until it exists again. [[line 149](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/headless.md?plain=1#L149)] [[Source](https://code.claude.com/docs/en/headless#get-structured-output)]
* `plugin_errors` entries for a failed `--plugin-dir` directory/archive now include the resolved `path` (v2.1.283+). [[line 165](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/headless.md?plain=1#L165)] [[Source](https://code.claude.com/docs/en/headless#stream-responses)]

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* The Stop hook's 8-consecutive-block cap is now configurable via `CLAUDE_CODE_STOP_HOOK_BLOCK_CAP`. [[line 2491](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/hooks.md?plain=1#L2491)] [[Source](https://code.claude.com/docs/en/hooks#stop)]

#### [ide-integrations](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/ide-integrations.md) [[Source](https://code.claude.com/docs/en/ide-integrations)] / [vs-code](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/vs-code.md)

* The Resume dialog's Web tab now also lists Remote Control sessions and opens a matching local conversation directly instead of downloading a copy, with clearer download-failure errors. [[line 264](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/ide-integrations.md?plain=1#L264)] [[Source](https://code.claude.com/docs/en/ide-integrations#choose-where-claude-lives)]
* A message queued with an editor selection attached now keeps that selection even if you select something else afterward. [[line 295](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/ide-integrations.md?plain=1#L295)] [[Source](https://code.claude.com/docs/en/ide-integrations#manage-plugins)]

#### [interactive-mode](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* Added vim-mode commands `r{char}`, `dj`/`dk`, `dgg`/`dG`, and `d0`/`c0`/`y0` (v2.1.281+). [[line 27](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/interactive-mode.md?plain=1#L27)] [[Source](https://code.claude.com/docs/en/interactive-mode#general-controls)]
* Documented that a command reaching its timeout is auto-moved to the background instead of stopped, unless it starts with `sleep`. [[line 296](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/interactive-mode.md?plain=1#L296)] [[Source](https://code.claude.com/docs/en/interactive-mode#how-backgrounding-works)]

#### [keybindings](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/keybindings.md) [[Source](https://code.claude.com/docs/en/keybindings)]

* Pressing `Ctrl+C` or `Ctrl+D` twice in most dialogs now closes the dialog instead of exiting Claude Code. [[line 148](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/keybindings.md?plain=1#L148)] [[Source](https://code.claude.com/docs/en/keybindings#confirmation-actions)]
* `footer:dismiss` was removed in v2.1.281 (existing bindings become no-ops). [[line 256](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/keybindings.md?plain=1#L256)] [[Source](https://code.claude.com/docs/en/keybindings#footer-actions)]
* The rewind menu's message list and the diff file list now use the generic `Select` actions/bindings instead of their own dedicated `MessageSelector`/`diff:viewDetails` actions (v2.1.283+). [[lines 271-301](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/keybindings.md?plain=1#L271-L301)] [[Source](https://code.claude.com/docs/en/keybindings#footer-actions)]

#### [llm-gateway-protocol](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/llm-gateway-protocol.md) [[Source](https://code.claude.com/docs/en/llm-gateway-protocol)]

* New stricter streaming requirements for gateways: deliver the full event sequence without dropping/duplicating/reordering, and relay each response through its final `message_delta`/`message_stop` before closing the body. [[line 59](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/llm-gateway-protocol.md?plain=1#L59)] [[Source](https://code.claude.com/docs/en/llm-gateway-protocol#streaming)]
* Added the `x-claude-code-prompt-id` gateway hint header (v2.1.283+). [[line 145](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/llm-gateway-protocol.md?plain=1#L145)] [[Source](https://code.claude.com/docs/en/llm-gateway-protocol#gateway-hint-headers)]

#### [managed-settings](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/managed-settings.md) [[Source](https://code.claude.com/docs/en/managed-settings)]

* Added the new `deniedModels` and `availableModelsMatch` managed settings to the merge and fail-closed-enforcement tables. [[lines 245-263](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/managed-settings.md?plain=1#L245-L263)] [[Source](https://code.claude.com/docs/en/managed-settings#keep-cowork-folder-access-when-only-managed-rules-apply)]

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Only an SDK host application can register an in-process `"type": "sdk"` server; such an entry in `.mcp.json`/settings is now skipped with a clear message. [[line 76](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/mcp.md?plain=1#L76)] [[Source](https://code.claude.com/docs/en/mcp#option-1-add-a-remote-http-server)]
* Duplicate-server detection now normalizes URL case, default ports, and trailing slashes when comparing endpoints. [[line 587](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/mcp.md?plain=1#L587)] [[Source](https://code.claude.com/docs/en/mcp#scope-hierarchy-and-precedence)]
* Added "Images in tool results": MCP-returned images are now also saved full-resolution to the session's `tool-results` directory (v2.1.283+). [[line 1252](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/mcp.md?plain=1#L1252)] [[Source](https://code.claude.com/docs/en/mcp#raise-the-limit-for-a-specific-tool)]
* MCP Apps UI resources (`ui://` or `text/html;profile=mcp-app`) no longer appear in `@` suggestions or the resource list tool. [[line 1370](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/mcp.md?plain=1#L1370)] [[Source](https://code.claude.com/docs/en/mcp#reference-mcp-resources)]
* Prompts from a server named `anthropic-skills` no longer appear, since that name is reserved for synced skills. [[line 1463](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/mcp.md?plain=1#L1463)] [[Source](https://code.claude.com/docs/en/mcp#use-mcp-prompts-as-commands)]

#### [model-config](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* Added "Block specific models or versions": use `deniedModels` or `availableModelsMatch: "exact"` to keep a newer release (e.g. Opus 5.5) blocked even though a broader `availableModels` entry permits it (v2.1.283+). [[line 336](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/model-config.md?plain=1#L336)] [[Source](https://code.claude.com/docs/en/model-config#block-specific-models-or-versions)]
* Opus 5.5 defaults to effort `medium`, one level below Opus 5's `high` default; start at `medium` rather than carrying over an Opus 5 level. [[line 614](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/model-config.md?plain=1#L614)] [[Source](https://code.claude.com/docs/en/model-config#choose-an-effort-level)]

#### [monitoring-usage](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* Troubleshooting OTEL export now points to `claude --debug-file <path>` rather than `claude --debug`. [[line 33](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/monitoring-usage.md?plain=1#L33)] [[Source](https://code.claude.com/docs/en/monitoring-usage#quick-start)]
* The `tool.output` span event now also fires for MCP tools, WebFetch, and WebSearch (v2.1.283+). [[line 272](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/monitoring-usage.md?plain=1#L272)] [[Source](https://code.claude.com/docs/en/monitoring-usage#span-attributes)]
* On Amazon Bedrock, `request_id` now falls back to the `x-amzn-requestid` header when there's no `request-id` header (v2.1.282+). [[line 651](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/monitoring-usage.md?plain=1#L651)] [[Source](https://code.claude.com/docs/en/monitoring-usage#event-correlation-attributes)]

#### [permission-modes](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/permission-modes.md) [[Source](https://code.claude.com/docs/en/permission-modes)]

* Auto mode is now the built-in starting permission mode for terminal/VS Code sessions on **every** plan and provider with Claude Code v2.1.283+, not just Pro/Max/Team. [[line 4](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/permission-modes.md?plain=1#L4)] [[Source](https://code.claude.com/docs/en/permission-modes#choose-a-permission-mode)]
* Critical-path `rm`/`rmdir` handling changed (v2.1.281+): in `auto` mode Claude Code now asks in the terminal with a two-minute countdown (denying elsewhere, such as `-p`, SDK, VS Code chat) instead of always routing to the classifier; `bypassPermissions` also gets a timed terminal prompt. [[lines 621-656](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/permission-modes.md?plain=1#L621-L656)] [[Source](https://code.claude.com/docs/en/permission-modes#critical-paths)]
* Added new critical-path detection cases: a shell variable followed by a top-level directory name, a variable assigned from a directory-printing substitution in the same command, a backslash-only target, and a target that is entirely a command substitution. [[line 656](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/permission-modes.md?plain=1#L656)] [[Source](https://code.claude.com/docs/en/permission-modes#critical-paths)]
* `Remove-Item`'s system-path denial now also covers the `cmd` built-ins `rd`, `rmdir`, `del`, and `erase` run through `cmd /c` (v2.1.283+), matching the Windows PowerShell tool security fix. [[line 372](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/permission-modes.md?plain=1#L372)] [[Source](https://code.claude.com/docs/en/permission-modes#what-the-classifier-blocks-by-default)]

#### [permissions](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/permissions.md) [[Source](https://code.claude.com/docs/en/permissions)]

* Documented the new workspace-trust check before starting or restarting a background session. [[line 625](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/permissions.md?plain=1#L625)] [[Source](https://code.claude.com/docs/en/permissions#project-allow-rules-and-workspace-trust)]

#### [platforms](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/platforms.md) [[Source](https://code.claude.com/docs/en/platforms)]

* Remote Control now also runs from the Claude Desktop app, not just the CLI and VS Code. [[line 43](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/platforms.md?plain=1#L43)] [[Source](https://code.claude.com/docs/en/platforms#work-when-you-are-away-from-your-terminal)]

#### [plugin-evals](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/plugin-evals.md) [[Source](https://code.claude.com/docs/en/plugin-evals)]

* `claude plugin eval` now requires git 2.31+ when git is installed, and stops with a new error before running any case on an older git. [[line 21](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/plugin-evals.md?plain=1#L21)] [[Source](https://code.claude.com/docs/en/plugin-evals#requirements)]

#### [plugins-reference](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/plugins-reference.md) [[Source](https://code.claude.com/docs/en/plugins-reference)] / [plugins/manifest-reference](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/plugins/manifest-reference.md)

* `claude plugin validate` now also checks `outputStyles`, `lspServers`, `monitors`, and `themes` paths for containment/existence (v2.1.283+). [[line 341](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/plugins-reference.md?plain=1#L341)] [[Source](https://code.claude.com/docs/en/plugins-reference#path-rules)]

#### [plugins/create](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/plugins/create.md) [[Source](https://code.claude.com/docs/en/plugins/create)]

* Added guidance to use Anthropic's `plugin-dev` plugin (`/plugin-dev:create-plugin`) to have Claude scaffold and validate a larger plugin. [[line 120](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/plugins/create.md?plain=1#L120)] [[Source](https://code.claude.com/docs/en/plugins/create#create-your-first-plugin)]

#### [plugins/publish](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/plugins/publish.md) [[Source](https://code.claude.com/docs/en/plugins/publish)] (+ [plugin-marketplaces](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/plugin-marketplaces.md), [plugins/anthropic-marketplaces](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/plugins/anthropic-marketplaces.md), [plugins/create-marketplace](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/plugins/create-marketplace.md), [plugins.md](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/plugins.md), [plugins/overview](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/plugins/overview.md))

* Submitting a plugin to Anthropic's public community marketplace is being replaced by submitting to **Anthropic's directory** through a new developer portal at claude.ai/directory/manage; a listing there reaches claude.ai, Cowork, and Claude Code together, and requires a paid claude.ai plan. [[line 471](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/plugins/publish.md?plain=1#L471)] [[Source](https://code.claude.com/docs/en/plugins/publish#next-steps)]

#### [prompt-caching](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/prompt-caching.md) [[Source](https://code.claude.com/docs/en/prompt-caching)]

* Added a table detailing exactly which mid-session MCP server changes (connect, drop out, auto-reconnect, deliberate removal) invalidate the cache when tool definitions load into the prefix. [[line 100](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/prompt-caching.md?plain=1#L100)] [[Source](https://code.claude.com/docs/en/prompt-caching#turning-on-fast-mode)]
* `DISABLE_PROMPT_CACHING_HAIKU` now covers the main conversation when Haiku is your main model (v2.1.283+). [[line 336](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/prompt-caching.md?plain=1#L336)] [[Source](https://code.claude.com/docs/en/prompt-caching#disable-prompt-caching)]

#### [remote-control](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/remote-control.md) [[Source](https://code.claude.com/docs/en/remote-control)]

* Remote Control can now be started from the Claude Desktop app's Code tab with `/remote-control` or `/rc`, in addition to the CLI and VS Code. [[line 248](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/remote-control.md?plain=1#L248)] [[Source](https://code.claude.com/docs/en/remote-control#trusted-devices)]
* Server mode gained a `-d`/`--debug[=<filter>]` flag (v2.1.282+). [[line 232](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/remote-control.md?plain=1#L232)] [[Source](https://code.claude.com/docs/en/remote-control#trusted-devices)]
* `DISABLE_TELEMETRY`/`DO_NOT_TRACK` alone no longer block Remote Control unless your organization requires Trusted Devices (v2.1.283+). [[line 208](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/remote-control.md?plain=1#L208)] [[Source](https://code.claude.com/docs/en/remote-control#resume-sessions-after-stopping-the-server)]
* `/focus on`/`off` is now supported from mobile and web (v2.1.281+). [[line 389](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/remote-control.md?plain=1#L389)] [[Source](https://code.claude.com/docs/en/remote-control#remote-control-is-disabled-by-your-organizations-policy)]

#### [routines](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/routines.md) [[Source](https://code.claude.com/docs/en/routines)] / [web-scheduled-tasks](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/web-scheduled-tasks.md)

* A schedule set exactly on the hour can now start several minutes late; pick a few minutes past the hour (e.g. 9:07) to start closer to the scheduled time. [[line 130](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/routines.md?plain=1#L130)] [[Source](https://code.claude.com/docs/en/routines#add-a-schedule-trigger)]

#### [sandboxing](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/sandboxing.md) [[Source](https://code.claude.com/docs/en/sandboxing)]

* The sandbox's default writable temp directory changed from a per-session directory to a per-user temp directory. [[line 34](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/sandboxing.md?plain=1#L34)] [[Source](https://code.claude.com/docs/en/sandboxing#get-started)]

#### [server-managed-settings](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/server-managed-settings.md) [[Source](https://code.claude.com/docs/en/server-managed-settings)]

* Detailed how a startup that reads the cached remote settings now preserves fail-closed (stricter) values, not just dropping invalid entries. [[line 188](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/server-managed-settings.md?plain=1#L188)] [[Source](https://code.claude.com/docs/en/server-managed-settings#invalid-entries-in-delivered-settings)]

#### [settings-reference](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/settings-reference.md) [[Source](https://code.claude.com/docs/en/settings-reference)]

* Added `availableModelsMatch` and `deniedModels` managed settings for blocking specific model versions (v2.1.283+). [[lines 570-833](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/settings-reference.md?plain=1#L570-L833)] [[Source](https://code.claude.com/docs/en/settings-reference#settings-index)]
* Added `maxProseWidth` to cap the width of prose in Claude's responses in a wide terminal (v2.1.282+). [[line 3174](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/settings-reference.md?plain=1#L3174)] [[Source](https://code.claude.com/docs/en/settings-reference#keybindingflavor)]
* The `trailers` (git commit attribution) default now names the subagent's model when a subagent makes the commit, not the session's active model. [[line 3796](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/settings-reference.md?plain=1#L3796)] [[Source](https://code.claude.com/docs/en/settings-reference#attributioncommit)]

#### [skills](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)] / [slash-commands](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/slash-commands.md)

* The frontmatter `name` field now sets the actual invocable command for a personal or project skill directory, not just its display label. [[line 383](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/skills.md?plain=1#L383)] [[Source](https://code.claude.com/docs/en/skills#using-skill-frontmatter-outside-claude-code)]
* Added "Names reserved for synced skills": `anthropic-skills` and everything inside that namespace is now reserved for claude.ai-synced skills, replacing the earlier `claude-ai` reservation. [[line 231](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/skills.md?plain=1#L231)] [[Source](https://code.claude.com/docs/en/skills#when-a-synced-skill-name-matches-another-command)]
* Picking up a newly created top-level skills directory now requires running `/reload-skills` instead of restarting Claude Code. [[line 260](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/skills.md?plain=1#L260)] [[Source](https://code.claude.com/docs/en/skills#how-claude-code-handles-the-body-of-a-synced-skill)]

#### [sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* Subagent requests now count toward the same usage limits as the main conversation, noted alongside model-selection guidance. [[line 4](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/sub-agents.md?plain=1#L4)] [[Source](https://code.claude.com/docs/en/sub-agents#create-custom-subagents)]
* An `--agents` JSON definition can now have an empty `prompt`, which leaves the session's system prompt unchanged when selected with `--agent` (v2.1.281+). [[line 208](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/sub-agents.md?plain=1#L208)] [[Source](https://code.claude.com/docs/en/sub-agents#choose-the-subagent-scope)]

#### [terminal-config](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/terminal-config.md) [[Source](https://code.claude.com/docs/en/terminal-config)]

* Added "Cap response width in wide terminals", documenting the new `maxProseWidth` setting. [[line 297](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/terminal-config.md?plain=1#L297)] [[Source](https://code.claude.com/docs/en/terminal-config#switch-to-fullscreen-rendering)]

#### [troubleshoot-install](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/troubleshoot-install.md) [[Source](https://code.claude.com/docs/en/troubleshoot-install)]

* Added recovery steps for `claude.exe missing after an update on Windows` (rename the `.old.` backup back). [[line 546](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/troubleshoot-install.md?plain=1#L546)] [[Source](https://code.claude.com/docs/en/troubleshoot-install#the-process-cannot-access-the-file-during-windows-install)]
* Added a new `Claude Code access has not been granted for this account` entry for Enterprise custom-role sign-in failures. [[line 925](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/troubleshoot-install.md?plain=1#L925)] [[Source](https://code.claude.com/docs/en/troubleshoot-install#403-forbidden-after-login)]
* Added macOS-specific `PATH` fix instructions (`~/.bash_profile` instead of `~/.bashrc`, since Terminal starts Bash as a login shell). [[line 124](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/troubleshoot-install.md?plain=1#L124)] [[Source](https://code.claude.com/docs/en/troubleshoot-install#verify-your-path)]

#### [workflows](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/workflows.md) [[Source](https://code.claude.com/docs/en/workflows)]

* Clarified that ultracode tokens draw on subscription usage limits, and that turning it on already opts out of the "Large workflow" warning, the concurrent-subagent limit, and the auto-mode first-launch approval. [[line 143](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/workflows.md?plain=1#L143)] [[Source](https://code.claude.com/docs/en/workflows#let-claude-decide-with-ultracode)]

#### [worktrees](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/worktrees.md) [[Source](https://code.claude.com/docs/en/worktrees)]

* Exiting with unfinished work now prints the exact `claude --worktree <name> --resume` command to return to it later. [[line 44](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/claude-code/worktrees.md?plain=1#L44)] [[Source](https://code.claude.com/docs/en/worktrees#clean-up-worktrees)]

-----

## API changes

### Changed documents

#### [agent-skills/overview](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/api/agents-and-tools/agent-skills/overview.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)]

* Noted a Microsoft Foundry-specific exception: the Skill version download endpoint (`GET /v1/skills/{skill_id}/versions/{version}/content`) isn't supported there. [[line 137](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/api/agents-and-tools/agent-skills/overview.md?plain=1#L137)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview#where-skills-work)]

#### [build-with-claude/claude-platform-on-aws](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/api/build-with-claude/claude-platform-on-aws.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws)]

* Agent Skills on Claude Platform on AWS moved out of beta to **Available**. [[line 27](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/api/build-with-claude/claude-platform-on-aws.md?plain=1#L27)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws#claude-platform-on-aws-versus-amazon-bedrock)]

#### [build-with-claude/files](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/api/build-with-claude/files.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/files)]

* The Files API moved from beta to GA on both Claude Platform on AWS and Microsoft Foundry. [[line 9](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/api/build-with-claude/files.md?plain=1#L9)] [[Source](https://platform.claude.com/docs/en/build-with-claude/files#read-the-text-file)]

#### [build-with-claude/mid-conversation-system-messages](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/api/build-with-claude/mid-conversation-system-messages.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages)]

* Clarified beta-header requirements for mid-conversation tool changes: `inline-tools-2026-09-15` (Claude API) also covers inline tool definitions, and adding an MCP server mid-conversation needs `mcp-client-2026-09-15` as a second header on the Claude API. [[line 16](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/api/build-with-claude/mid-conversation-system-messages.md?plain=1#L16)] [[Source](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages#keep-at-least-one-non-deferred-tool-in-tools-so-a-tool-defined)]

#### [build-with-claude/overview](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/api/build-with-claude/overview.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/overview)]

* Updated the feature-availability table to reflect Agent Skills and Files API reaching GA on Claude Platform on AWS and Microsoft Foundry. [[line 82](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/api/build-with-claude/overview.md?plain=1#L82)] [[Source](https://platform.claude.com/docs/en/build-with-claude/overview#tool-infrastructure)]

#### [manage-claude/analytics-api](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/api/manage-claude/analytics-api.md) [[Source](https://platform.claude.com/docs/en/manage-claude/analytics-api)]

* Engagement/adoption endpoint data now typically lands by ~13:00–13:30 UTC the following day, earlier than the previously documented ~17:00 UTC. [[line 75](https://github.com/gpambrozio/ClaudeDocs/blob/7801578b358e9e48ac6b406957c9c4abb5d1c625/docs-md/api/manage-claude/analytics-api.md?plain=1#L75)] [[Source](https://platform.claude.com/docs/en/manage-claude/analytics-api#data-availability-and-freshness)]
