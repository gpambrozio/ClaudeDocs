# [Claude docs changes for November 13th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d)]

## Executive Summary
- Claude Code 2.1.323 adds **Code Mode**, an experimental opt-in where Claude writes JavaScript that makes several tool calls in one step. It has a new dedicated docs page and touches the hooks, auto mode, permissions and settings docs.
- Plugins gain an `engines["claude-code"]` version range in `plugin.json`, plus TypeScript type checking of hooks modules in `claude plugin validate`.
- A large security hardening pass: stricter Bash permission checks, sandbox changes (worktree git commands, symlinked writes), MCP OAuth redirect blocking, and tighter hook and permission-check failure behavior.
- On Amazon Bedrock and Vertex AI, a session whose model is rejected as unavailable now switches to another model automatically, and `CLAUDE_CODE_DISABLE_MODEL_ACCESS_FALLBACK=1` turns that off.
- API docs add **message threads** (server-side conversation state), deprecate many old beta header values, document hosting options for Claude in Microsoft Foundry, and expand the Managed Agents workflow-run docs.

## New Claude Code versions

### [2.1.323](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/versions/2.1.323.md)

#### New features

* Added Code Mode, an experimental opt-in where Claude writes JavaScript to call its tools. It can be turned off for an organization.
* Added `engines["claude-code"]` to `plugin.json`. Plugins outside their stated Claude Code version range are not installed, updated or loaded, and install and update pick the newest version that fits.
* `claude plugin validate` now type-checks a plugin's TypeScript hooks module and reports the `$` nouns a mod's `engine.create` hook adds, withholds or replaces.
* Support for `CLAUDE_CODE_AUTO_MODE_MODEL` in managed settings for Claude Desktop sessions on third-party providers.
* Options menu (stop, switch to usage credits, upgrade) when a model needs usage credits that are off or used up.
* Progress heartbeat every 30 seconds while hooks run long in `claude -p` and SDK sessions.
* `.docx` support for Artifact tool asset uploads.
* New env vars: `CLAUDE_CODE_DISABLE_AGENT_PROGRESS_SUMMARIES` and `CLAUDE_CODE_RESUME_HINT_COMMAND`.
* Start-up warnings for Bash allow rules with a `*` in a variable's value, and for plugin language servers that can't start.
* `unsetOptionCount` in the `claude plugin install --json` result, and `isPromptCovered` in the props a mod's pane receives.
* VS Code: trust prompt before the first session in an untrusted folder, and live output of running Bash/PowerShell commands in the chat.

#### Existing feature improvements

* Clearer sign-in errors in `/login` and `claude setup-token`.
* More consistent Bash permission checks; some commands that could run differently from how they were checked now ask for permission.
* `/mcp` shows how many of a server's tools were left out because of invalid input schemas.
* Better memory use with many subagents, faster WebFetch on deeply nested pages, and the install script no longer downloads the latest version twice.
* The Claude apps gateway `/v1/models` states `max_input_tokens` where the context window is certain.
* The context window assumed for an unrecognized model ID changed from 200K to 1M. Use `CLAUDE_CODE_DISABLE_1M_CONTEXT=1` to keep 200K.
* Messages sessions can send each other without a prompt rose from about 20 to 100,000.
* `/security-review` now asks before Claude runs it.
* Sandbox: `git worktree add/move/remove` and commits in a worktree the session wasn't started in now fail read-only. Symlinked writes that lead elsewhere are ignored. An invalid `--settings` file with a `sandbox` key stops start-up.
* MCP: project (`.mcp.json`) server approvals match the exact server name, and finishing an MCP sign-in always asks you to confirm.
* "Don't ask again" rules that look like they hold a secret, or that would be saved to a git-tracked `settings.local.json`, last for the session only.
* Permission check failures after a `PreToolUse` "allow" hook, or on input rewritten by a `PermissionRequest` hook, are now decided as if no hook had answered, or asked again.
* Worktree creation refuses checkouts whose `.git` folders are links or hold hard links.
* Marketplace and plugin installs fail when a git submodule isn't on the recorded commit.
* `/logout` in a background session now signs out every session on the computer.
* Removed the `subagentStatusLine` setting. A plugin's `agent` setting is deprecated.

#### Major bug fixes

* Fixed `/compact` summarizing away a message Claude hadn't answered yet.
* Fixed a resumed session joining your next message to an old interrupted message.
* Fixed memory spikes after Claude changed a very large file, and Edit/Bash running out of memory on certain `/proc` files, devices and named pipes.
* Fixed a settings save in a running session undoing a hand edit of `settings.json`.
* Fixed `claude plugin` commands and `claude mcp list` signing you out of a Console profile.
* Fixed Windows file-reading Bash commands running without a permission prompt when given a wildcard or list of files.
* Fixed non-streaming requests failing on errors that streamed requests recover from.

-----

## Claude Code changes

### New Documents

#### [Code Mode](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/claude-code/code-mode.md) [[Source](https://code.claude.com/docs/en/code-mode)]

New page for Code Mode, an experimental, off-by-default feature in which Claude writes JavaScript that makes several tool calls (parallel commands, chained results, filtered output) in one step. It explains how to view the code (`Ctrl+O` transcript viewer), when to use it, and its limitations: resuming only in the terminal, auto mode classifying the code rather than each call, and a ten-minute limit unless code runs in the background. It also covers requirements, permission checks, hook behavior, and how to turn it on or off for an organization.

### Changed documents

#### [amazon-bedrock](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/claude-code/amazon-bedrock.md) [[Source](https://code.claude.com/docs/en/amazon-bedrock)]

* When Bedrock rejects the session's model as unavailable, Claude Code switches to another model (or a configured fallback chain). The page lists when it doesn't switch and how to disable it with `CLAUDE_CODE_DISABLE_MODEL_ACCESS_FALLBACK=1`. [[lines 348-358](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/claude-code/amazon-bedrock.md?plain=1#L348-L358)] [[Source](https://code.claude.com/docs/en/amazon-bedrock#when-a-model-is-disabled-mid-session)]
* Mantle: set both `CLAUDE_CODE_USE_BEDROCK` and `CLAUDE_CODE_USE_MANTLE`, and a new `400` section covers model IDs Mantle doesn't serve. [[lines 516-522](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/claude-code/amazon-bedrock.md?plain=1#L516-L522)] [[lines 622-627](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/claude-code/amazon-bedrock.md?plain=1#L622-L627)] [[Source](https://code.claude.com/docs/en/amazon-bedrock#run-mantle-alongside-the-invoke-api)]

#### [auto-mode-config](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/claude-code/auto-mode-config.md) [[Source](https://code.claude.com/docs/en/auto-mode-config)]

* Notes how routing all shell commands through the classifier works in a Code Mode session.

#### [claude-apps-gateway-config](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/claude-code/claude-apps-gateway-config.md) [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config)]

* Per-developer attribution on Bedrock: set `assume_role` with `session_name` on every `bedrock` and `mantle` upstream. [[line 518](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/claude-code/claude-apps-gateway-config.md?plain=1#L518)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config#per-developer-aws-cost-attribution)]
* Foundry RBAC now names the `Foundry User` or `Cognitive Services User` role. [[line 657](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/claude-code/claude-apps-gateway-config.md?plain=1#L657)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config#microsoft-foundry)]
* To use the `fable` alias with `auto_include_builtin_models: false`, add a `claude-fable-5` entry to `models`. [[line 1002](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/claude-code/claude-apps-gateway-config.md?plain=1#L1002)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config#models)]
* Policy merging: deny-lists and hook arrays (`permissions.deny`/`ask`, `deniedMcpServers`, `deniedModels`, `hooks`, and others) take the union of base and policy. [[lines 1028-1032](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/claude-code/claude-apps-gateway-config.md?plain=1#L1028-L1032)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config#managed)]
* Claude Code doesn't read an alias's `upstream_model` to size its context window. [[line 1284](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/claude-code/claude-apps-gateway-config.md?plain=1#L1284)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config#context-window-in-terminal-sessions)]

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* New `CLAUDE_CODE_EXPERIMENTAL_CODE_MODE` variable (`1` to start sessions in Code Mode, `0` to keep it off). [[line 297](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/claude-code/env-vars.md?plain=1#L297)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* New "Stopped an OAuth request" section: Claude Code stops MCP OAuth requests that an endpoint redirects elsewhere or more than 5 times. [[lines 1824-1840](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/claude-code/errors.md?plain=1#L1824-L1840)] [[Source](https://code.claude.com/docs/en/errors#stopped-an-oauth-request)]
* New Remote Control errors about the `--settings` file being skipped or changing after start. [[lines 251-252](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/claude-code/errors.md?plain=1#L251-L252)] [[Source](https://code.claude.com/docs/en/errors#find-your-error)]
* New auto-mode denial reason for a call changed after review. [[line 827](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/claude-code/errors.md?plain=1#L827)] [[Source](https://code.claude.com/docs/en/errors#a-hook-changed-this-calls-input-after-auto-mode-reviewed-it)]
* Cloud sessions: a `403` or DNS error can mean the host isn't on the environment's allowlist. Image-size errors can name a different pixel limit. [[line 2222](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/claude-code/errors.md?plain=1#L2222)] [[Source](https://code.claude.com/docs/en/errors#host-not-allowed-in-a-cloud-session)]
* PreModelSwitch refusal when managed-plugin hooks can't be checked now applies only before v2.1.323. [[line 2890](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/claude-code/errors.md?plain=1#L2890)] [[Source](https://code.claude.com/docs/en/errors#model-switch-was-blocked-by-a-premodelswitch-hook)]

#### [feature-availability](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/claude-code/feature-availability.md) [[Source](https://code.claude.com/docs/en/feature-availability)]

* Added Code Mode to the availability table (experimental, local CLI only). [[lines 116-125](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/claude-code/feature-availability.md?plain=1#L116-L125)] [[Source](https://code.claude.com/docs/en/feature-availability#cli-capabilities-that-vary-by-provider)]
* Updated the per-provider "Not available" lists. [[line 240](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/claude-code/feature-availability.md?plain=1#L240)] [[Source](https://code.claude.com/docs/en/feature-availability#summary-by-provider)]

#### [google-vertex-ai](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/claude-code/google-vertex-ai.md) [[Source](https://code.claude.com/docs/en/google-vertex-ai)]

* Same automatic model switch when the model is unavailable in your project or region, with `/model` `s` to keep working and `CLAUDE_CODE_DISABLE_MODEL_ACCESS_FALLBACK=1` to opt out. [[lines 227-237](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/claude-code/google-vertex-ai.md?plain=1#L227-L237)] [[Source](https://code.claude.com/docs/en/google-vertex-ai#when-a-model-is-disabled-mid-session)]

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* `subagentStatusLine` removed from the list of settings narrowed to managed settings. [[line 256](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/claude-code/hooks.md?plain=1#L256)] [[Source](https://code.claude.com/docs/en/hooks#hook-locations)]
* Clarified the HTTP hook `onFailure` field. [[line 504](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/claude-code/hooks.md?plain=1#L504)] [[Source](https://code.claude.com/docs/en/hooks#http-hook-fields)]
* Notes that `PreToolUse` timeouts and failures work differently in Code Mode. [[line 900](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/claude-code/hooks.md?plain=1#L900)] [[line 984](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/claude-code/hooks.md?plain=1#L984)] [[Source](https://code.claude.com/docs/en/hooks#timeouts)]
* Code Mode output can be withheld by hooks, and the block `reason` is added to context in that case. [[line 1519](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/claude-code/hooks.md?plain=1#L1519)] [[line 1568](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/claude-code/hooks.md?plain=1#L1568)] [[Source](https://code.claude.com/docs/en/hooks#userpromptsubmit)]
* ConfigChange hooks also run for managed policy and skill file changes. [[line 3008](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/claude-code/hooks.md?plain=1#L3008)] [[Source](https://code.claude.com/docs/en/hooks#configchange)]

#### [interactive-mode](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* `Alt+M` cycles permission modes on Windows when VT input mode isn't enabled; clarified spellcheck behavior. [[line 35](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/claude-code/interactive-mode.md?plain=1#L35)] [[line 595](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/claude-code/interactive-mode.md?plain=1#L595)] [[Source](https://code.claude.com/docs/en/interactive-mode#general-controls)]

#### [keybindings](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/claude-code/keybindings.md) [[Source](https://code.claude.com/docs/en/keybindings)]

* New default `ctrl+x` chords in Chat (`ctrl+x ctrl+=`, `ctrl+x ctrl+-`, `ctrl+x ctrl+_`, `ctrl+x =`, `ctrl+x -`) and the matching unbind example. [[line 580](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/claude-code/keybindings.md?plain=1#L580)] [[lines 630-634](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/claude-code/keybindings.md?plain=1#L630-L634)] [[Source](https://code.claude.com/docs/en/keybindings#unbind-default-shortcuts)]

#### [microsoft-foundry](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/claude-code/microsoft-foundry.md) [[Source](https://code.claude.com/docs/en/microsoft-foundry)]

* Simplified permissions guidance to the `Foundry User` or `Cognitive Services User` role, replacing the custom role definition. [[line 146](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/claude-code/microsoft-foundry.md?plain=1#L146)] [[Source](https://code.claude.com/docs/en/microsoft-foundry#azure-rbac-configuration)]

#### [model-config](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* If a managed plugin or its hooks fail to load, model switches are still allowed but its PreModelSwitch hooks don't run. [[line 158](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/claude-code/model-config.md?plain=1#L158)] [[Source](https://code.claude.com/docs/en/model-config#setting-your-model)]
* Unrecognized model IDs now warn that Claude Code assumes a different context window. [[line 904](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/claude-code/model-config.md?plain=1#L904)] [[Source](https://code.claude.com/docs/en/model-config#correct-the-window-for-a-gateway-or-custom-model-id)]

#### [permission-modes](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/claude-code/permission-modes.md) [[Source](https://code.claude.com/docs/en/permission-modes)]

* How to leave plan mode with `Shift+Tab`, and a note that with Code Mode the classifier reviews the code once, not each inner tool call. [[line 303](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/claude-code/permission-modes.md?plain=1#L303)] [[line 592](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/claude-code/permission-modes.md?plain=1#L592)] [[Source](https://code.claude.com/docs/en/permission-modes#analyze-before-you-edit-with-plan-mode)]

#### [plugins-reference](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/claude-code/plugins-reference.md) [[Source](https://code.claude.com/docs/en/plugins-reference)]

* Restructured `plugin.json` reference with a clearer intro and fields table (mirrors the manifest reference page). [[line 116](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/claude-code/plugins-reference.md?plain=1#L116)] [[Source](https://code.claude.com/docs/en/plugins-reference#fields)]

#### [plugins/components](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/claude-code/plugins/components.md) [[Source](https://code.claude.com/docs/en/plugins/components)]

* Rewrote the intro and example-plugin description, and removed some embedded example content. [[line 21](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/claude-code/plugins/components.md?plain=1#L21)] [[Source](https://code.claude.com/docs/en/plugins/components#explore-the-plugin-directory)]

#### [plugins/manifest-reference](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/claude-code/plugins/manifest-reference.md) [[Source](https://code.claude.com/docs/en/plugins/manifest-reference)]

* Clarified the top-level keys table (only `name` is required) and the default-location layout example. [[line 116](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/claude-code/plugins/manifest-reference.md?plain=1#L116)] [[line 621](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/claude-code/plugins/manifest-reference.md?plain=1#L621)] [[Source](https://code.claude.com/docs/en/plugins/manifest-reference#fields)]

#### [sandboxing](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/claude-code/sandboxing.md) [[Source](https://code.claude.com/docs/en/sandboxing)]

* On Linux and WSL2, a filesystem entry for a path that doesn't exist yet has no effect, so create it first. [[line 275](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/claude-code/sandboxing.md?plain=1#L275)] [[Source](https://code.claude.com/docs/en/sandboxing#configure-sandboxing)]
* Tighter rules on who can set `filesystem.disabled`: not project settings; managed-only when managed settings configure `sandbox.filesystem`; ignored when `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB` is set. [[lines 377-379](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/claude-code/sandboxing.md?plain=1#L377-L379)] [[Source](https://code.claude.com/docs/en/sandboxing#which-settings-can-disable-it)]

#### [settings-reference](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/claude-code/settings-reference.md) [[Source](https://code.claude.com/docs/en/settings-reference)]

* Auto mode shell-classifier key behaves differently in Code Mode. [[line 883](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/claude-code/settings-reference.md?plain=1#L883)] [[Source](https://code.claude.com/docs/en/settings-reference#automodeclassifyallshell)]
* Sandbox path entries that don't exist yet are ignored on Linux/WSL2. [[line 1531](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/claude-code/settings-reference.md?plain=1#L1531)] [[Source](https://code.claude.com/docs/en/settings-reference#sandboxfilesystemallowwrite)]
* The `env` setting overwrites the same shell variable, and the highest-precedence settings file wins. [[line 2453](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/claude-code/settings-reference.md?plain=1#L2453)] [[Source](https://code.claude.com/docs/en/settings-reference#how-env-values-interact-with-your-shell)]
* Code Mode can be turned on via `CLAUDE_CODE_EXPERIMENTAL_CODE_MODE` from the shell, user settings or `--settings`. [[line 2494](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/claude-code/settings-reference.md?plain=1#L2494)] [[Source](https://code.claude.com/docs/en/settings-reference#variables-claude-code-ignores-in-env)]
* Removed the `subagentStatusLine` example. [[line 3173](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/claude-code/settings-reference.md?plain=1#L3173)] [[Source](https://code.claude.com/docs/en/settings-reference#statusline)]

#### [setup](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/claude-code/setup.md) [[Source](https://code.claude.com/docs/en/setup)]

* Alpine/musl: install requires `bash` and `curl`, and Claude Code requires `bash` or `zsh`. [[line 140](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/claude-code/setup.md?plain=1#L140)] [[Source](https://code.claude.com/docs/en/setup#alpine-linux-and-musl-based-distributions)]

#### [statusline](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/claude-code/statusline.md) [[Source](https://code.claude.com/docs/en/statusline)]

* Removed the subagent status line section, matching the removal of the `subagentStatusLine` setting. [[line 1083](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/claude-code/statusline.md?plain=1#L1083)] [[Source](https://code.claude.com/docs/en/statusline#windows-configuration)]

-----

## API changes

### Changed documents

#### [agents-and-tools/tool-use/programmatic-tool-calling](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/api/agents-and-tools/tool-use/programmatic-tool-calling.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling)]

* The pending call's ~4 minute timeout starts when Claude's code makes the call, so don't use `expires_at` as your deadline. Respond as soon as you can. [[line 456](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/api/agents-and-tools/tool-use/programmatic-tool-calling.md?plain=1#L456)] [[line 1468](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/api/agents-and-tools/tool-use/programmatic-tool-calling.md?plain=1#L1468)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling#container-lifecycle)]

#### [agents-and-tools/tool-use/tool-runner](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/api/agents-and-tools/tool-use/tool-runner.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-runner)]

* No longer described as beta. [[line 48](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/api/agents-and-tools/tool-use/tool-runner.md?plain=1#L48)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-runner#initialize-client)]
* New caveat: when you take over an iteration, you must keep the conversation valid by appending the assistant message and tool results. [[line 836](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/api/agents-and-tools/tool-use/tool-runner.md?plain=1#L836)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-runner#taking-over-message-history)]
* New "Compacting long conversations" section covering threshold compaction and on-demand compaction (`compact_before_next_turn()`). [[line 836](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/api/agents-and-tools/tool-use/tool-runner.md?plain=1#L836)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-runner#taking-over-message-history)]

#### [api/beta](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/api/api/beta.md) [[Source](https://platform.claude.com/docs/en/api/beta)]

* Many `AnthropicBeta` values (such as `message-batches-2024-09-24`, `prompt-caching-2024-07-31`, `pdfs-2024-09-25`, `token-counting-2024-11-01`, `extended-cache-ttl-2025-04-11`, `cache-diagnosis-2026-04-07`) are marked deprecated and no longer needed. `files-api-2025-04-14` and `skills-2025-10-02` are deprecated with migration steps, since sending them selects the old beta response shapes. The same change repeats across the per-language SDK beta pages (Python, TypeScript, Go, Java, Ruby, C#, CLI).

#### [build-with-claude/claude-in-microsoft-foundry](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/api/build-with-claude/claude-in-microsoft-foundry.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry)]

* New hosting options comparison: hosted on Azure (US Data Zone Standard available, prompts stay within Azure) vs hosted on Anthropic (all Claude models, Global Standard).
* New RBAC prerequisite (`Foundry User` or `Cognitive Services User`), deployment setup steps (model version selects hosting, region scope), and the `ANTHROPIC_FOUNDRY_BASE_URL` variable.
* Notes on private networking, 1M context availability, and updated troubleshooting.

#### [build-with-claude/message-threads](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/api/build-with-claude/message-threads.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/message-threads)]

* Expanded guide to server-side message threads: create, continue (send only new messages plus `previous_message_id`) and replay, with expiry after 5 minutes idle and deletion within 1 hour.
* New SDK thread helper section and examples with top-level `cache_control` for caching each turn.
* Recovery, forking, params, fallbacks and sticky routing behavior, the helper's refusal handling, and new error codes `thread_fingerprint_mismatch` and `thread_unsupported_request`. Threads are append-only, so compaction means starting a new thread from a summary.

#### [manage-claude/admin-api-keys](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/api/manage-claude/admin-api-keys.md) [[Source](https://platform.claude.com/docs/en/manage-claude/admin-api-keys)]

* Reorganized around a comparison table of the key for Claude Console vs Claude Enterprise (sign-in address, where to create, prefix, who can create, scopes, which APIs it works with), with a separate Console creation section.

#### [manage-claude/analytics-api](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/api/manage-claude/analytics-api.md) [[Source](https://platform.claude.com/docs/en/manage-claude/analytics-api)]

* Key types for the two analytics APIs presented as a table; points to the in-product Analytics dashboard.

#### [manage-claude/compliance-api-access](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/api/manage-claude/compliance-api-access.md) [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-api-access)]

* Key types table, enablement for standalone vs parent-linked Console organizations, a warning that turning the Compliance API off stops activity recording, and who can create keys.

#### [manage-claude/wif-reference](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/api/manage-claude/wif-reference.md) [[Source](https://platform.claude.com/docs/en/manage-claude/wif-reference)]

* Clarified token exchange fields and environment variables. The env-var path activates only when the rule ID, organization ID and a token source are set, and the minted token is scoped to the named workspace.

#### [managed-agents/migration](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/api/managed-agents/migration.md) [[Source](https://platform.claude.com/docs/en/managed-agents/migration)]

* Added "What you control" list and guidance for agents built with `client.messages.create()`; mapped the SDK `permission_mode`/`can_use_tool` to per-tool permission policies.

#### [managed-agents/reference](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/api/managed-agents/reference.md) [[Source](https://platform.claude.com/docs/en/managed-agents/reference)]

* Documented the `redacted` content block, the new `session.deleted` event, and clarified `workflow_run.status_running`.

#### [managed-agents/scheduled-deployments](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/api/managed-agents/scheduled-deployments.md) [[Source](https://platform.claude.com/docs/en/managed-agents/scheduled-deployments)]

* On Claude Platform on AWS, set `execution_identity` to an `aws_role` so each run's session uses an IAM role.
* Archiving or deleting an agent archives its deployments. Added a recovery procedure for a deployment paused by an archived subagent.

#### [managed-agents/self-hosted](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/api/managed-agents/self-hosted.md) [[Source](https://platform.claude.com/docs/en/managed-agents/self-hosted)]

* Added a License section for the server software.

#### [managed-agents/workflow-runs](https://github.com/gpambrozio/ClaudeDocs/blob/c211dd9ad08b53eee0ca6d1328b8bc416cf1356d/docs-md/api/managed-agents/workflow-runs.md) [[Source](https://platform.claude.com/docs/en/managed-agents/workflow-runs)]

* Clarified run lifecycle: runs start running or idle, pause at the budget and resume when it's raised, and are "open" from `workflow_run.created` until `workflow_run.status_ended`.
* Run events arrive on the primary thread's stream and don't trigger webhooks. New `timeout_error` for the lifetime limit.
* Agent threads in a run: agent field, thread events on the primary stream, no phase field, and how to ask the agent to print the workflow it wrote.

#### Other API pages

* Smaller updates to Managed Agents (events and streaming, multiagent orchestration, permission policies, secure deployment pages, self-hosted sandboxes, session threads), `text-watermark`, `ip-allowlist`, and generated SDK reference pages (sessions, memory stores, environments, vaults, organization) across all languages.
