# [Claude docs changes for Sept, 30th 2026](https://github.com/gpambrozio/ClaudeDocs/tree/c46bbc2fb0614a46a28fa191956606140712ec9b) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/c46bbc2fb0614a46a28fa191956606140712ec9b)]

## Executive Summary
- Claude Code 2.1.285 adds an `allowedProviders` managed setting, `claude --desktop`, `claude plugin configure`, and a `CLAUDE_CODE_DISABLE_WEB_FETCH` variable. It also puts a time limit on background shell commands and hardens `/ultrareview` uploads and the Artifact tool.
- Permission modes docs now spell out the critical-path `rm` checks. They cover which targets count, a rewrite guide, and per-mode outcomes, plus a new Amazon Bedrock guardrail option for the Claude Apps gateway.
- A new "Open agent view by default" setting (`defaultToAgentsView`) lets `claude` start in agent view, and managed-MCP admins can now allow Claude in Chrome alongside `managed-mcp.json`.
- The self-hosted runner docs gain guidance on runner exits and failed starts and on private CAs with Anthropic-managed git. Routine hourly limits and public artifact sharing are also documented.
- API docs add a `/claude-api preserved-thinking-migration` skill workflow and MCP helper functions for SDKs. The tool-runner and streaming docs were also expanded.

## New Claude Code versions

### [2.1.285](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/versions/2.1.285.md)

#### New features

* Added `CLAUDE_CODE_DISABLE_WEB_FETCH` environment variable to turn off the WebFetch tool
* Added `claude --desktop` to open the Claude desktop app on the current directory or on a session (with `--continue` / `--resume <id>`)
* Added `claude plugin configure <plugin>` to show a plugin's options and save values from stdin with `--values-stdin`
* Added `<server>.<key>=<value>` to `claude plugin install --config` so a bundled `.mcpb` MCP server can be configured at install time
* Added `allowedProviders` managed setting to limit which API providers a machine may use
* Added `CLAUDE_CODE_NONSTREAMING_TIMEOUT_RETRIES` to cap re-sends of a timed-out non-streaming fallback request
* VS Code: added a plugin options form in Manage plugins, an on-demand diagnostics tool that reads the Problems panel, and a note on tabs interrupted by a window reload
* Claude Tag: added direct messages with Claude for Enterprise Standard or Usage-Based Chat seats that also have Cowork

#### Existing feature improvements

* `/resume` and `claude --resume` now open a session running in the background, and `claude --resume <id> "prompt"` sends the prompt to it as its next turn
* Bedrock and Vertex AI sessions fall back to an older model of the same tier when an admin removes access to the default model
* Sessions behind a custom `ANTHROPIC_BASE_URL` now use the 1M context window of models that have one (run `/autocompact 200k` if your gateway stops at 200K)
* Background Bash and PowerShell commands now stop after a time limit (default 30 min, max 2 h) and Claude is notified
* `claude -p` and Python Agent SDK sessions on third-party providers or with telemetry off now start in auto mode when no permission mode is configured
* Subagents in auto mode end their run as soon as they hand back a report
* Sandbox settings: project settings can no longer widen or turn off an admin-required sandbox or reopen managed read-denies
* `/tasks` folds Claude Code's own background work under one "System tasks" row
* `claude mcp list` now lists WebSocket servers, and `claude mcp get` hides command, args and env values of plugin-provided stdio servers
* `/ultrareview` on macOS and Linux now requires git 2.31+ for local uploads and refuses symbolic-ref checkouts
* The MCP server name `widgets` is reserved in cloud sessions and on self-hosted runners
* Plugin marketplace errors name why a git address was refused, and git URL validation is stricter

#### Major bug fixes

* Fixed Claude Code refusing to start when the OS denies reading the managed settings file (it now warns and continues)
* Fixed model switches through `set_model` (e.g. the Agent SDK's `setModel`) keeping the old output-token limit and auto-compact window
* Fixed fork subagents not keeping the parent's plan mode or `dontAsk` mode
* Fixed several Artifact tool issues: overwriting newer content after a rewind, `Artifact` allow rules covering files outside the working directories, and auto mode skipping its classifier
* Fixed synchronous hooks hanging while a background process kept the hook's output open
* Fixed the PowerShell tool skipping deny and ask rules when its command parser failed to start
* Fixed a failing API request being retried up to 21 times when streaming kept failing
* Fixed redacted logs showing part of a URL password containing `@`
* Fixed plugin and marketplace installs over SSH ignoring `GIT_SSH` / `core.sshCommand`

-----

## Claude Code changes

### Changed documents

#### [agent-sdk/file-checkpointing](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/claude-code/agent-sdk/file-checkpointing.md) [[Source](https://code.claude.com/docs/en/agent-sdk/file-checkpointing)]

* The page was condensed around a single lead example. It now shows capturing the checkpoint UUID and session ID, then resuming with an empty prompt and calling `rewind_files()` / `rewindFiles()`. [[lines 5-27](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/claude-code/agent-sdk/file-checkpointing.md?plain=1#L5-L27)] [[Source](https://code.claude.com/docs/en/agent-sdk/file-checkpointing#rewind-file-changes-with-checkpointing)]
* The rewind must be called on the resumed session, which needs checkpointing enabled in its options too. [[line 148](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/claude-code/agent-sdk/file-checkpointing.md?plain=1#L148)] [[Source](https://code.claude.com/docs/en/agent-sdk/file-checkpointing#implement-checkpointing)]

#### [agent-view](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/claude-code/agent-view.md) [[Source](https://code.claude.com/docs/en/agent-view)]

* New "Open agent view by default" section: turn on `defaultToAgentsView` in `/config` so `claude` with no arguments opens agent view. Passing a prompt starts a regular session. [[lines 59-82](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/claude-code/agent-view.md?plain=1#L59-L82)] [[Source](https://code.claude.com/docs/en/agent-view#open-agent-view-by-default)]

#### [artifacts](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/claude-code/artifacts.md) [[Source](https://code.claude.com/docs/en/artifacts)]

* Artifacts are private until shared. After a public share, Claude asks for approval once per conversation before changing it. [[line 42](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/claude-code/artifacts.md?plain=1#L42)] [[Source](https://code.claude.com/docs/en/artifacts#create-an-artifact)]
* Public sharing (a link viewable without sign-in) is documented and is off by default on Team and Enterprise until an Owner enables it. Public viewers can't see or add comments. [[lines 83-106](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/claude-code/artifacts.md?plain=1#L83-L106)] [[Source](https://code.claude.com/docs/en/artifacts#share-an-artifact)]
* Connector-backed pages can be shared, but connector calls don't run for public viewers. [[line 166](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/claude-code/artifacts.md?plain=1#L166)] [[Source](https://code.claude.com/docs/en/artifacts#how-connector-calls-work-for-viewers)]
* Admin controls were reorganized under Organization settings (Artifacts, Capabilities, Data and privacy retention). [[lines 343-359](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/claude-code/artifacts.md?plain=1#L343-L359)] [[Source](https://code.claude.com/docs/en/artifacts#manage-artifacts-for-your-organization)]

#### [claude-apps-gateway-config](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/claude-code/claude-apps-gateway-config.md) [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config)]

* New "Apply an Amazon Bedrock guardrail" section: a `guardrail` block (id, version) on Bedrock upstreams. It must be set on all Bedrock upstreams or none, and requires `bedrock:ApplyGuardrail`. Input tags are not supported. [[lines 283-307](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/claude-code/claude-apps-gateway-config.md?plain=1#L283-L307)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config#apply-an-amazon-bedrock-guardrail)]
* Non-interactive runs apply pushed settings for that run only without recording approval, and a declined dialog exits the session. [[line 757](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/claude-code/claude-apps-gateway-config.md?plain=1#L757)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config#what-goes-in-cli)]
* Several desktop policy keys require Claude Code v2.1.281+ on the gateway server. [[line 817](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/claude-code/claude-apps-gateway-config.md?plain=1#L817)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config#claude-desktop-overlay)]
* Telemetry exports from `/login` sessions carry `user.id`, `user.email` and `user.groups` for per-developer attribution. [[line 842](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/claude-code/claude-apps-gateway-config.md?plain=1#L842)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config#telemetry)]

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* Settings-file `env` values override shell values only "in most sessions", with a link to the new interaction section. [[line 97](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/claude-code/env-vars.md?plain=1#L97)] [[Source](https://code.claude.com/docs/en/env-vars#precedence)]
* `CLAUDE_CODE_MAX_OUTPUT_TOKENS`: for a model ID Claude Code can't resolve, the default is 32000 and the cap is 128000. [[line 298](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/claude-code/env-vars.md?plain=1#L298)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* `DISABLE_PROMPT_CACHING_OPUS` / `_SONNET` now apply to the default Opus / Sonnet model. [[lines 427-428](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/claude-code/env-vars.md?plain=1#L427-L428)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* New entries: "Failed to start OAuth callback server" (with a `claude setup-token` workaround), PDF errors including a missing `pdftoppm`, "Couldn't confirm model with the API", "Can't switch to the default model" (managed `deniedModels` / `availableModels`), and the `/ultrareview` "upload cannot follow that setting" error. [[line 1229](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/claude-code/errors.md?plain=1#L1229)] [[Source](https://code.claude.com/docs/en/errors#failed-to-start-oauth-callback-server)]
* The "not a recognized model id" section is rewritten. Model switches from the Agent SDK or an app are now confirmed with the provider on the first switch. [[lines 2205-2241](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/claude-code/errors.md?plain=1#L2205-L2241)] [[Source](https://code.claude.com/docs/en/errors#model-is-not-a-recognized-model-id)]
* The minimum-version API error now has a table of how to update each kind of binary (CLI, desktop app, VS Code extension, SDK). [[lines 2309-2318](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/claude-code/errors.md?plain=1#L2309-L2318)] [[Source](https://code.claude.com/docs/en/errors#claude-code-does-not-support-this-model)]
* The Fable usage-credits consent prompt can time out via `dialogExpiry` in non-terminal sessions. [[lines 696-711](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/claude-code/errors.md?plain=1#L696-L711)] [[Source](https://code.claude.com/docs/en/errors#the-prompt-to-confirm-went-unanswered)]

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* New "What a blocked prompt leaves behind" section: a blocked `UserPromptSubmit` prompt never reaches Claude, but its text is still written to the transcript unless `suppressOriginalPrompt` is set. It can still appear in local files and prompt history. [[line 1348](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/claude-code/hooks.md?plain=1#L1348)] [[Source](https://code.claude.com/docs/en/hooks#what-a-blocked-prompt-leaves-behind)]
* Blocked prompts are no longer described as "erased". [[line 834](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/claude-code/hooks.md?plain=1#L834)] [[Source](https://code.claude.com/docs/en/hooks#exit-code-2-behavior-per-event)]
* The `SessionStart` `fork` matcher now covers conversations moved to the background. [[line 1084](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/claude-code/hooks.md?plain=1#L1084)] [[Source](https://code.claude.com/docs/en/hooks#sessionstart)]
* The `agent_needs_input` notification also fires for auto mode's classifier-billing notice. [[line 2211](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/claude-code/hooks.md?plain=1#L2211)] [[Source](https://code.claude.com/docs/en/hooks#notification)]

#### [keybindings](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/claude-code/keybindings.md) [[Source](https://code.claude.com/docs/en/keybindings)]

* New `Task` context. `footer:dismiss` is now unbound by default. [[lines 52-266](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/claude-code/keybindings.md?plain=1#L52-L266)] [[Source](https://code.claude.com/docs/en/keybindings#contexts)]
* `select:*` bindings are honored in list panels such as `/skills`, `/mcp` and `/tasks`. [[line 370](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/claude-code/keybindings.md?plain=1#L370)] [[Source](https://code.claude.com/docs/en/keybindings#select-actions)]
* Keybinding validation warnings now go to the debug log (`--debug`). Misspelled modifiers such as `ctl+k` are dropped. [[lines 610-620](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/claude-code/keybindings.md?plain=1#L610-L620)] [[Source](https://code.claude.com/docs/en/keybindings#validation)]

#### [managed-mcp](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/claude-code/managed-mcp.md) [[Source](https://code.claude.com/docs/en/managed-mcp)]

* New `allowClaudeInChromeWithManagedMcp` device-level setting lets Claude in Chrome run alongside `managed-mcp.json`. It is otherwise blocked, and `claude --chrome` exits at startup. [[lines 144-152](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/claude-code/managed-mcp.md?plain=1#L144-L152)] [[Source](https://code.claude.com/docs/en/managed-mcp#allow-claude-in-chrome-alongside-the-managed-set)]
* The allowlist bypass now covers three groups: the organization's own servers, built-in servers, and a Claude Tag session's Slack tools. [[line 293](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/claude-code/managed-mcp.md?plain=1#L293)] [[Source](https://code.claude.com/docs/en/managed-mcp#how-a-server-is-evaluated)]

#### [model-config](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* Fable consent prompt behavior in Agent SDK hosts is clarified, including expiry via `dialogExpiry`. [[line 102](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/claude-code/model-config.md?plain=1#L102)] [[Source](https://code.claude.com/docs/en/model-config#fable-and-usage-credits)]
* Model-switch validation is rewritten: the SDK or an app confirms the ID with the provider. Remote Control checks locally. `--model`, `ANTHROPIC_MODEL` and `model` are not checked up front. [[lines 149-156](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/claude-code/model-config.md?plain=1#L149-L156)] [[Source](https://code.claude.com/docs/en/model-config#setting-your-model)]
* Cowork remote sessions: the server rejects models outside the server-managed `availableModels`. [[line 272](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/claude-code/model-config.md?plain=1#L272)] [[Source](https://code.claude.com/docs/en/model-config#surface-coverage)]
* Thinking can't be turned off on Opus 5.5, Sonnet 5.5 and Fable. The toggle now shows "Thinking can't be turned off". [[line 676](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/claude-code/model-config.md?plain=1#L676)] [[Source](https://code.claude.com/docs/en/model-config#extended-thinking)]
* A pinned `ANTHROPIC_DEFAULT_*_MODEL` replaces the picker's 1M rows. Use `/model opus[1m]` or `/model sonnet[1m]` to reach the 1M window. [[line 860](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/claude-code/model-config.md?plain=1#L860)] [[Source](https://code.claude.com/docs/en/model-config#pin-models-for-third-party-deployments)]

#### [permission-modes](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/claude-code/permission-modes.md) [[Source](https://code.claude.com/docs/en/permission-modes)]

* The critical-path `rm`/`rmdir` section is restructured into subsections: which paths are critical, other targets that count, nested commands and inline scripts, how to rewrite a flagged command, per-mode outcomes, and time limits. [[lines 637-708](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/claude-code/permission-modes.md?plain=1#L637-L708)] [[Source](https://code.claude.com/docs/en/permission-modes#critical-paths)]
* New targets are documented: positional parameters like `$1`, `sh -c` inline scripts, and double-quoted `find -exec sh -c` scripts. [[lines 654-688](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/claude-code/permission-modes.md?plain=1#L654-L688)] [[Source](https://code.claude.com/docs/en/permission-modes#other-targets-that-count-as-critical-paths)]
* Bypass-permissions warning: accepting sets `skipDangerousModePermissionPrompt` in `~/.claude/settings.json`. Declining exits. [[line 570](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/claude-code/permission-modes.md?plain=1#L570)] [[Source](https://code.claude.com/docs/en/permission-modes#skip-all-checks-with-bypasspermissions-mode)]
* Auto mode fallback is reorganized. New "No verdict from the classifier" case, "Repeated-block thresholds" subsection, and "How auto mode evaluates actions" heading. [[lines 454-489](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/claude-code/permission-modes.md?plain=1#L454-L489)] [[Source](https://code.claude.com/docs/en/permission-modes#when-auto-mode-falls-back)]

#### [plugin-evals](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/claude-code/plugin-evals.md) [[Source](https://code.claude.com/docs/en/plugin-evals)]

* Expanded eval documentation, including the `--ablation none|with-without` baseline comparison (see the CLI reference).

#### [plugins/cli-reference](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/claude-code/plugins/cli-reference.md) [[Source](https://code.claude.com/docs/en/plugins/cli-reference)]

* New `--ablation <mode>` option for `claude plugin eval`. `eval init` runs from the plugin root and takes a case name. [[lines 409-450](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/claude-code/plugins/cli-reference.md?plain=1#L409-L450)] [[Source](https://code.claude.com/docs/en/plugins/cli-reference#plugin-eval)]
* Removing a marketplace from its last scope also deletes its cache and uninstalls its plugins, along with their options and data. Use `update` to refresh instead. [[line 663](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/claude-code/plugins/cli-reference.md?plain=1#L663)] [[Source](https://code.claude.com/docs/en/plugins/cli-reference#plugin-marketplace-remove)]
* `/plugin install <source>` in a session reports "marketplace not found" and installs nothing. [[line 726](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/claude-code/plugins/cli-reference.md?plain=1#L726)] [[Source](https://code.claude.com/docs/en/plugins/cli-reference#plugin-marketplace-update)]
* Session-only plugins (`--plugin-dir`) show in `plugin list` only when the flag precedes the subcommand. [[line 791](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/claude-code/plugins/cli-reference.md?plain=1#L791)] [[Source](https://code.claude.com/docs/en/plugins/cli-reference#flags-that-load-a-plugin-for-one-session)]

#### [plugins/troubleshooting](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/claude-code/plugins/troubleshooting.md) [[Source](https://code.claude.com/docs/en/plugins/troubleshooting)]

* New entry for an `installed_plugins.json` record this version can't read. [[line 630](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/claude-code/plugins/troubleshooting.md?plain=1#L630)] [[Source](https://code.claude.com/docs/en/plugins/troubleshooting#plugin-installed-but-not-working)]
* The "marketplace not found" entry now distinguishes the `<plugin>@<name>` form from `/plugin install <source>`. [[line 138](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/claude-code/plugins/troubleshooting.md?plain=1#L138)] [[Source](https://code.claude.com/docs/en/plugins/troubleshooting#add-a-marketplace)]

#### [routines](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/claude-code/routines.md) [[Source](https://code.claude.com/docs/en/routines)]

* New hourly limits table: scheduled runs 100/hour per account, Run now and API fires 30/hour per routine and 100/hour per account, with no overage. GitHub events have their own per-routine and per-account caps. [[lines 362-372](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/claude-code/routines.md?plain=1#L362-L372)] [[Source](https://code.claude.com/docs/en/routines#usage-and-limits)]
* Routines belong to an individual account and aren't shared with teammates. [[line 59](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/claude-code/routines.md?plain=1#L59)] [[Source](https://code.claude.com/docs/en/routines#create-a-routine)]

#### [self-hosted-environments-deploy](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/claude-code/self-hosted-environments-deploy.md) [[Source](https://code.claude.com/docs/en/self-hosted-environments-deploy)]

* New "Trust a private certificate authority with Anthropic-managed git" section: how `GIT_SSL_CAINFO` and `GIT_SSL_NO_VERIFY` are handled for the runner's clone, in-session git, and hooks. Requires v2.1.283+. [[lines 163-187](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/claude-code/self-hosted-environments-deploy.md?plain=1#L163-L187)] [[Source](https://code.claude.com/docs/en/self-hosted-environments-deploy#trust-a-private-certificate-authority-with-anthropic-managed-git)]
* New "When the runner exits" section: how to recognize a failed start (`[runner:fatal]` or `error:` lines) and how to restart with a growing wait. It covers Kubernetes `CrashLoopBackOff` and Docker restarts. [[lines 520-581](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/claude-code/self-hosted-environments-deploy.md?plain=1#L520-L581)] [[Source](https://code.claude.com/docs/en/self-hosted-environments-deploy#when-the-runner-exits)]
* The Anthropic git proxy requires `--capacity 1`, but the sample recipes use `--capacity 4`. Sessions sharing a container lack per-session isolation. [[lines 159-201](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/claude-code/self-hosted-environments-deploy.md?plain=1#L159-L201)] [[Source](https://code.claude.com/docs/en/self-hosted-environments-deploy#use-the-anthropic-git-proxy)]
* Keep programs named in `GIT_SSH_COMMAND` / `GIT_ASKPASS` out of sessions' write access. A pinned version may be too old for a model. [[lines 145-429](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/claude-code/self-hosted-environments-deploy.md?plain=1#L145-L429)] [[Source](https://code.claude.com/docs/en/self-hosted-environments-deploy#ship-git-config-in-your-image)]

#### [settings-reference](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/claude-code/settings-reference.md) [[Source](https://code.claude.com/docs/en/settings-reference)]

* Updated for `defaultToAgentsView`, `allowClaudeInChromeWithManagedMcp` and `allowedProviders`, and a new "How `env` values interact with your shell" section.

#### [skills](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)]

* Additions related to the `/claude-api` skill, including its preserved-thinking migration subcommand.

-----

## API changes

### Changed documents

#### [agents-and-tools/agent-skills/claude-api-skill](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/api/agents-and-tools/agent-skills/claude-api-skill.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/claude-api-skill)]

* New `/claude-api preserved-thinking-migration` subcommand and a five-step workflow (scope, find, measure, fix, report) for finding history edits that invalidate `thinking` blocks. It runs real, billed API requests. [[lines 136-155](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/api/agents-and-tools/agent-skills/claude-api-skill.md?plain=1#L136-L155)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/claude-api-skill#checking-an-integration-for-preserved-thinking)]
* Beta header cleanup is now listed among the skill's migration tasks. [[line 126](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/api/agents-and-tools/agent-skills/claude-api-skill.md?plain=1#L126)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/claude-api-skill#migrating-to-a-newer-claude-model)]

#### [agents-and-tools/mcp-connector](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/api/agents-and-tools/mcp-connector.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/mcp-connector)]

* SDK helpers that convert between MCP types and Claude API types are now listed in a multi-language table: tools, messages, resource-to-content and resource-to-file. [[lines 1187-1317](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/api/agents-and-tools/mcp-connector.md?plain=1#L1187-L1317)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/mcp-connector#client-side-mcp-helpers)]

#### [agents-and-tools/tool-use/tool-runner](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/api/agents-and-tools/tool-use/tool-runner.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-runner)]

* Documents inspecting and modifying tool results via `generate_tool_call_response()` / `generateToolResponse()`. Ruby has no such hook, so read `runner.params[:messages]`. [[lines 1148-1547](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/api/agents-and-tools/tool-use/tool-runner.md?plain=1#L1148-L1547)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-runner#intercepting-tool-errors)]
* The TypeScript and Ruby runners support automatic compaction. [[line 1096](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/api/agents-and-tools/tool-use/tool-runner.md?plain=1#L1096)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-runner#automatic-context-management)]

#### [agents-and-tools/tool-use/memory-tool](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/api/agents-and-tools/tool-use/memory-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)]

* Memory tool helpers exist in four SDKs. The first `view` of `/memories` on an empty store is not an error when using the local-filesystem helper. [[lines 284-748](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/api/agents-and-tools/tool-use/memory-tool.md?plain=1#L284-L748)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool#implement-the-memory-handler)]

#### [build-with-claude/preserved-thinking](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/api/build-with-claude/preserved-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking)]

* Added a pointer to automate the prefix-edit check with `/claude-api preserved-thinking-migration`. [[line 429](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/api/build-with-claude/preserved-thinking.md?plain=1#L429)] [[Source](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking#check-whether-your-code-edits-the-prefix)]

#### [build-with-claude/streaming](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/api/build-with-claude/streaming.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/streaming)]

* Added SDK helpers to stream internally and return the full message: C# `Aggregate()` and PHP `MessageAccumulator`. Also documents accumulating partial tool-input JSON deltas. [[lines 141-335](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/api/build-with-claude/streaming.md?plain=1#L141-L335)] [[Source](https://platform.claude.com/docs/en/build-with-claude/streaming#get-the-final-message-without-handling-events)]

#### [build-with-claude/thinking](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/api/build-with-claude/thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/thinking)]

* Ruby note: plain hashes take `display:` while the typed class spells it `display_`. The SDK requires streaming when `max_tokens` is above 21,333, a client-side check. [[lines 284-1198](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/api/build-with-claude/thinking.md?plain=1#L284-L1198)] [[Source](https://platform.claude.com/docs/en/build-with-claude/thinking#configuring-thinking)]

#### [cli-sdks-libraries/cli/apply](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/api/cli-sdks-libraries/cli/apply.md) [[Source](https://platform.claude.com/docs/en/cli-sdks-libraries/cli/apply)]

* `ant apply` now supports vaults as YAML files in `vaults/` (CLI 1.34.0+). Any resource except a skill can be YAML, JSON or Markdown. [[lines 9-104](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/api/cli-sdks-libraries/cli/apply.md?plain=1#L9-L104)] [[Source](https://platform.claude.com/docs/en/cli-sdks-libraries/cli/apply#pr-summary)]

#### [build-with-claude/structured-outputs](https://github.com/gpambrozio/ClaudeDocs/blob/c46bbc2fb0614a46a28fa191956606140712ec9b/docs-md/api/build-with-claude/structured-outputs.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)]

* Large restructuring of the page (about 1,500 lines changed). No new feature is evident from the diff.

#### Other changes

* The API reference pages under `docs-md/api/api/` were regenerated with formatting churn, mostly reindented lists (for example, beta header enums). No substantive changes were found there.
* Smaller edits went into managed-agents docs (memory, vaults, self-hosted sandboxes, migration), compliance docs, rate-limits-api, Foundry/Platform-on-AWS pages and the model migration guides.
