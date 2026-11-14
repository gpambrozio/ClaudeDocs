# [Claude docs changes for November 14th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/fe64a31143080f1c2631d94da43d0fb22ab007fd) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/fe64a31143080f1c2631d94da43d0fb22ab007fd)]

## Executive Summary
- Claude Code 2.1.325 changes the sandbox default: sandboxed Bash commands now follow the normal permission flow unless you set `sandbox.autoAllowBashIfSandboxed: true`. The release also hardens many permission, sandbox and Bash-rule checks.
- New guide for using Claude Code with Claude Models on Google Cloud (Anthropic managed), with Google Cloud credentials, IAM and Marketplace billing. This is separate from Google Cloud's Agent Platform (Vertex AI).
- Subagent model selection is documented more precisely: nested subagents inherit from the subagent that spawned them, and the order of precedence is spelled out.
- Mods docs expand: per-mod rows in the prompt band, `$.theme.set` replacing `$.ui.backdrop`, organization-owned mods, and a stricter built-in guard.
- The API reference is regenerated across all SDKs (about 780 files). Per-method error lists are added, and the managed-agents `multiagent` examples and some beta deprecation notes are removed.

## New Claude Code versions

### [2.1.325](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/versions/2.1.325.md)

#### New features

* [VSCode] Prompt suggestions: Tab accepts the suggested next prompt, and `promptSuggestionEnabled: false` turns them off
* [VSCode] Console sign-in that creates no API key, and a field to paste the redirect URL when signing in to an MCP server over SSH, WSL or containers
* Spinner tip in VS Code about re-running a notebook cell after Claude reads or edits a Jupyter notebook
* A line under policy-block errors tells you how to continue (`/rewind` or `/clear`)

#### Existing feature improvements

* Sandboxed Bash commands now follow the normal permission flow by default; set `sandbox.autoAllowBashIfSandboxed: true` to keep running them without prompts (managed settings that enable the sandbox need the same key)
* Read-only git commands now ask first in repositories that aren't the project's or a trusted one (use `--add-dir`)
* Scheduled tasks and `/loop` ask before running a skill that declares `allowed-tools` or hooks; add `Skill(name)` to `permissions.allow` to run it unattended
* "Always allow" in Desktop, IDE and SDK hosts only offers a rule alone when saving it would allow that command again
* The sandbox refuses writes to `.claude` settings, skills, agents, commands and hooks in added directories, and protects worktree settings, hooks and shared git folders more fully
* Isolated worktree sessions are refused `git bisect run`, `git maintenance register|start` and `scalar` set-up commands
* Plugins from a managed remote marketplace in `prependPlugins` or `appendPlugins` count as the organization's; `pluginDigests` is deprecated and ignored
* Plugin MCP bundles (`.mcpb`, `.dxt`) unpack under the plugins directory so read-only plugin folders load
* Marketplace `ref` accepts the full ID of any commit on a branch or tag (older clients can't clone such a pin)
* `claude remote-control` exits with status 4 when it stops by itself and 69 when it can't register, so a service manager can restart it
* MCP tasks: Esc on a background task's question means "answer later", Claude is told when a task awaits your answer, and `/tasks` can show the question again
* `CLAUDE_CODE_MAX_CONTEXT_TOKENS` also sets the context window of unrecognized `claude-` model IDs, such as a gateway's `claude-sonnet-latest`
* `/cost`, `--max-budget-usd` and usage metrics count a mod's `$.model.complete` and `$.model.classify` calls
* Subagents cut off at the output token limit are asked for the whole answer again, more briefly
* Sandbox helper programs, ripgrep and local git run without sign-in tokens, API keys or the mTLS key passphrase in their environment
* Nested `.claude/skills` in `--plugin-dir` plugins no longer load from a session started above them
* Cloud sessions now start despite `sandbox.failIfUnavailable`, since the hosted container has no command sandbox

#### Major bug fixes

* Fixed a security issue in how zstd-compressed responses are decoded
* Fixed several permission gaps: some Bash deny/ask rules not applying, compound commands running without asking, a Bash allow rule running a different program than it names, relative deny rules not covering the project after `cd`, and a committed `.claude/settings.local.json` being treated as the user's own
* Fixed deny rules not applying to approvals that arrive after a restart in self-hosted runner and `claude remote-control` sessions
* Fixed artifact permission issues: subagents changing or uploading to externally visible artifacts without asking, and publishes skipping the confirmation
* Fixed subagents with their own model being moved to the plan-mode model under `opusplan` or `haiku`, and subagents sizing reads with the main session's model
* Fixed sessions on many third-party gateways and Foundry failing with context length errors instead of compacting
* Fixed recent turns going missing from a resumed session after an unclean exit
* Fixed a saved `sonnet[1m]` setting being rewritten to a model ID the API rejects
* Fixed background sessions on a claude.ai login using and billing an API key from the shell, and sessions moving to another sign-in
* Fixed token counting on Amazon Bedrock sending the conversation when `allowedProviders` forbids it
* Fixed `/security-review` and skills' inline git commands failing in bare-repo, `--separate-git-dir` and Android `repo` worktrees
* Fixed Linux sandboxed commands failing with `bwrap: Can't create file` under symlinked home directories
* Fixed several MCP issues: stuck tasks, lost elicitations in headless mode, and "Not connected" errors after reconnects

-----

## Claude Code changes

### New Documents

#### [Claude Models on Google Cloud (Anthropic managed)](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/claude-models-on-google-cloud-anthropic-managed.md) [[Source](https://code.claude.com/docs/en/claude-models-on-google-cloud-anthropic-managed)]

Setup guide for Claude Code with the Claude API that Anthropic runs through your Google Cloud project. It needs Claude Code v2.1.307 or later, the `roles/claude.user` IAM role, a project ID and a `wrkspc_` workspace ID. You create Application Default Credentials (a Google account via `gcloud auth application-default login`, or a service account key file). You then add three environment variables to the `env` block of `~/.claude/settings.json`, starting with `CLAUDE_CODE_USE_ANTHROPIC_GOOGLE_CLOUD`. It distinguishes this offering from Google Cloud's Agent Platform (formerly Vertex AI).

### Changed documents

#### [headless](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/headless.md) [[Source](https://code.claude.com/docs/en/headless)]

* `-p` runs stay open until background subagents and workflows finish, or the 10-minute cap ends the wait. [[line 80](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/headless.md?plain=1#L80)] [[Source](https://code.claude.com/docs/en/headless#background-tasks-at-exit)]
* New section on giving a long subagent command more time with `BASH_DEFAULT_TIMEOUT_MS`. [[lines 90-95](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/headless.md?plain=1#L90-L95)] [[Source](https://code.claude.com/docs/en/headless#give-a-long-subagent-command-more-time)]

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* The Bash `if` filter is best-effort: when Claude Code can't split the input into subcommands, the hook runs regardless of the pattern. [[line 439](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/hooks.md?plain=1#L439)] [[Source](https://code.claude.com/docs/en/hooks#how-if-patterns-match-bash-commands)]
* Clarified `hook error` notices, which events pass plain-text stdout to Claude, and non-blocking status codes. [[lines 824-872](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/hooks.md?plain=1#L824-L872)] [[Source](https://code.claude.com/docs/en/hooks#exit-code-0)]
* `continue: false` doesn't block a `PreToolUse` call (also return `permissionDecision: "deny"`), and `suppressOutput` has no effect. Stop semantics for Pre/PostToolUse are documented. [[lines 1096-1108](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/hooks.md?plain=1#L1096-L1108)] [[Source](https://code.claude.com/docs/en/hooks#json-output)]
* `PostToolUseFailure` can't rewrite a result; use PreToolUse and PostToolUse for redaction. [[line 1219](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/hooks.md?plain=1#L1219)] [[Source](https://code.claude.com/docs/en/hooks#decision-control)]

#### [hooks-guide](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/hooks-guide.md) [[Source](https://code.claude.com/docs/en/hooks-guide)]

* The protected-files hook example now notes that Claude can still change those files through shell commands, and points to `Edit` deny rules and sandboxing. [[lines 305-308](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/hooks-guide.md?plain=1#L305-L308)] [[Source](https://code.claude.com/docs/en/hooks-guide#block-edits-to-protected-files)]

#### [ide-integrations](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/ide-integrations.md) [[Source](https://code.claude.com/docs/en/ide-integrations)]

* New "Use or turn off suggested prompts" section: Tab accepts a suggestion, and `promptSuggestionEnabled: false` disables it. [[lines 201-209](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/ide-integrations.md?plain=1#L201-L209)] [[Source](https://code.claude.com/docs/en/ide-integrations#use-or-turn-off-suggested-prompts)]

#### [google-vertex-ai](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/google-vertex-ai.md) [[Source](https://code.claude.com/docs/en/google-vertex-ai)]

* Note that this page covers Google Cloud's Agent Platform, and links to the new Anthropic-managed Google Cloud page. [[lines 10-13](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/google-vertex-ai.md?plain=1#L10-L13)] [[Source](https://code.claude.com/docs/en/google-vertex-ai#claude-code-on-google-clouds-agent-platform)]

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* MCP tasks can be stopped from `/tasks` with `x`. An elicitation dialog stays hidden while `/tasks` is open, and Esc answers later. [[lines 503-517](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/mcp.md?plain=1#L503-L517)] [[Source](https://code.claude.com/docs/en/mcp#stop-an-mcp-task-or-get-its-result)]
* `--strict-mcp-config` can be used to load only the servers passed with `--mcp-config`. [[line 807](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/mcp.md?plain=1#L807)] [[Source](https://code.claude.com/docs/en/mcp#project-scope)]

#### [model-config](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* Added Claude Models on Google Cloud (Anthropic managed) to the alias table (Opus 5.5, Sonnet 5.5, Haiku 4.5) and to the Opus 5.5 default list. [[line 44](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/model-config.md?plain=1#L44)] [[Source](https://code.claude.com/docs/en/model-config#model-aliases)]
* With Remote Control, a model-prompt answer can come from a connected device (v2.1.323+). [[line 109](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/model-config.md?plain=1#L109)] [[Source](https://code.claude.com/docs/en/model-config#fable-and-usage-credits)]
* Sessions started with `claude-opus-4-1`-style IDs on the Anthropic API run on the model `opus` resolves to. [[line 187](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/model-config.md?plain=1#L187)] [[Source](https://code.claude.com/docs/en/model-config#setting-your-model)]
* The fallback chain skips models unsupported by auto mode, with a new "Which entries Claude Code tries" subsection. [[lines 540-546](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/model-config.md?plain=1#L540-L546)] [[Source](https://code.claude.com/docs/en/model-config#which-entries-claude-code-tries)]
* `ultrathink` can raise a turn to `xhigh` effort in VS Code's chat box and the desktop Code tab (v2.1.316+). [[lines 722-732](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/model-config.md?plain=1#L722-L732)] [[Source](https://code.claude.com/docs/en/model-config#use-ultrathink-for-one-off-deep-reasoning)]

#### [permissions](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/permissions.md) [[Source](https://code.claude.com/docs/en/permissions)]

* Documented `permissions.denyInsteadOfPrompting` for unattended sessions. [[line 85](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/permissions.md?plain=1#L85)] [[Source](https://code.claude.com/docs/en/permissions#permission-modes)]
* Sandboxed Bash runs without prompting only when `autoAllowBashIfSandboxed` is `true`. [[line 744](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/permissions.md?plain=1#L744)] [[Source](https://code.claude.com/docs/en/permissions#how-permissions-interact-with-sandboxing)]
* The VS Code extension asks for folder trust in a "Trust this folder in Claude Code?" dialog. [[line 785](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/permissions.md?plain=1#L785)] [[Source](https://code.claude.com/docs/en/permissions#project-allow-rules-and-workspace-trust)]

#### [plugins/mods/admin](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/plugins/mods/admin.md) [[Source](https://code.claude.com/docs/en/plugins/mods/admin)]

* An organization's own mods aren't checked by the restriction; every other mod counts as a user's. Organization mods can be installed to run as yours, and marketplaces can be hosted for approved mods. [[lines 39-60](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/plugins/mods/admin.md?plain=1#L39-L60)] [[Source](https://code.claude.com/docs/en/plugins/mods/admin#stop-user-installed-mods-from-loading)]
* The built-in guard protects managed hooks, the system prompt and managed `CLAUDE.md`. On v2.1.323+, a user's mod can keep a managed MCP server from connecting. [[lines 60-62](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/plugins/mods/admin.md?plain=1#L60-L62)] [[Source](https://code.claude.com/docs/en/plugins/mods/admin#know-what-happens-by-default)]
* Reviewing mods: the `hooks:` and `calls:` output is explained, with a row for `$.mcp.call`. [[lines 159-177](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/plugins/mods/admin.md?plain=1#L159-L177)] [[Source](https://code.claude.com/docs/en/plugins/mods/admin#review-what-a-mod-can-do)]

#### [plugins/mods/interface](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/plugins/mods/interface.md) [[Source](https://code.claude.com/docs/en/plugins/mods/interface)]

* `ui.render` hooks can take a matcher filter. Since v2.1.323 each mod gets its own row in the prompt band (filter on `{ component: 'AbovePrompt' }`). [[lines 176-194](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/plugins/mods/interface.md?plain=1#L176-L194)] [[Source](https://code.claude.com/docs/en/plugins/mods/interface#pick-where-to-draw)]
* The permission prompt isn't a render site, but the `AskUserQuestion` dialog is. [[line 280](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/plugins/mods/interface.md?plain=1#L280)] [[Source](https://code.claude.com/docs/en/plugins/mods/interface#change-what-claude-code-already-draws)]
* `$.theme.set` and `$.theme.clear` replace `$.ui.backdrop` (removed in v2.1.319), with an updated backdrop example. [[lines 398-427](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/plugins/mods/interface.md?plain=1#L398-L427)] [[Source](https://code.claude.com/docs/en/plugins/mods/interface#put-a-backdrop-behind-the-conversation)]

#### [plugins/mods/troubleshoot](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/plugins/mods/troubleshoot.md) [[Source](https://code.claude.com/docs/en/plugins/mods/troubleshoot)]

* Where to find mod errors depending on session type. [[line 14](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/plugins/mods/troubleshoot.md?plain=1#L14)] [[Source](https://code.claude.com/docs/en/plugins/mods/troubleshoot#find-out-why-a-mod-does-nothing)]
* New guard messages: `tried to lift a deny rule in your settings` and `the rules and hooks in your settings could not be checked...`. [[lines 72-73](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/plugins/mods/troubleshoot.md?plain=1#L72-L73)] [[Source](https://code.claude.com/docs/en/plugins/mods/troubleshoot#messages-from-the-built-in-guard)]
* New `reload failed` section, with and without "the previous version stays loaded". [[lines 175-183](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/plugins/mods/troubleshoot.md?plain=1#L175-L183)] [[Source](https://code.claude.com/docs/en/plugins/mods/troubleshoot#reload-failed)]

#### [remote-control](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/remote-control.md) [[Source](https://code.claude.com/docs/en/remote-control)]

* `/resume` and `/teleport` disconnect Remote Control first if the session has a share link. [[line 177](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/remote-control.md?plain=1#L177)] [[Source](https://code.claude.com/docs/en/remote-control#what-connected-devices-see)]
* Effort-level changes from a connected device, the server-mode ~10-minute give-up, unanswered Fable usage-credits prompts ending the turn, and `/usage-credits` over mobile or web. [[lines 183-380](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/remote-control.md?plain=1#L183-L380)] [[Source](https://code.claude.com/docs/en/remote-control#what-connected-devices-see)]
* Troubleshooting for credential failures now uses `--debug-file`. [[lines 509-516](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/remote-control.md?plain=1#L509-L516)] [[Source](https://code.claude.com/docs/en/remote-control#remote-credentials-fetch-failed)]

#### [sandboxing](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/sandboxing.md) [[Source](https://code.claude.com/docs/en/sandboxing)]

* `autoAllowBashIfSandboxed` no longer defaults to `true`; the default sandbox mode is regular permissions mode. [[lines 393-395](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/sandboxing.md?plain=1#L393-L395)] [[Source](https://code.claude.com/docs/en/sandboxing#what-changes-when-filesystem-isolation-is-off)]
* Managed-settings guidance flipped: enabling the sandbox gives regular permissions mode, and auto-allow needs `autoAllowBashIfSandboxed: true`. [[line 1091](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/sandboxing.md?plain=1#L1091)] [[Source](https://code.claude.com/docs/en/sandboxing#sandbox-prints-sandbox-settings-not-changed)]

#### [sessions](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/sessions.md) [[Source](https://code.claude.com/docs/en/sessions)]

* `claude --resume <session-id>` documented. [[line 18](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/sessions.md?plain=1#L18)] [[Source](https://code.claude.com/docs/en/sessions#resume-a-session)]
* New "Flags to pass again when you resume": `--mcp-config`, `--plugin-dir`, `--add-dir`, `--settings`, `--fallback-model`. [[lines 54-68](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/sessions.md?plain=1#L54-L68)] [[Source](https://code.claude.com/docs/en/sessions#flags-to-pass-again-when-you-resume)]
* Plan mode is restored when a deny rule removes `ExitPlanMode` or `denyInsteadOfPrompting` is on. [[lines 80-88](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/sessions.md?plain=1#L80-L88)] [[Source](https://code.claude.com/docs/en/sessions#permission-mode-on-resume)]

#### [settings-reference](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/settings-reference.md) [[Source](https://code.claude.com/docs/en/settings-reference)]

* `sandbox.autoAllowBashIfSandboxed` default is now `false` (it was `true` before v2.1.324), with an example setting both keys. [[lines 1354-1368](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/settings-reference.md?plain=1#L1354-L1368)] [[Source](https://code.claude.com/docs/en/settings-reference#sandboxautoallowbashifsandboxed)]
* `sandbox.failIfUnavailable` details: exit at startup, and cloud exceptions. [[line 1335](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/settings-reference.md?plain=1#L1335)] [[Source](https://code.claude.com/docs/en/settings-reference#sandboxfailifunavailable)]
* The advisor key has no effect where the advisor isn't available (e.g. Bedrock). [[line 288](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/settings-reference.md?plain=1#L288)] [[Source](https://code.claude.com/docs/en/settings-reference#advisormodel)]
* The filesystem layer being off disables `denyRead` and `credentials.files` deny entries. [[line 1652](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/settings-reference.md?plain=1#L1652)] [[Source](https://code.claude.com/docs/en/settings-reference#sandboxfilesystemdisabled)]

#### [setup](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/setup.md) [[Source](https://code.claude.com/docs/en/setup)]

* Moving a native install to the stable channel can downgrade you. To avoid that, set `minimumVersion` to your current version, via `/config` ("Stay on current version") or the settings file. [[lines 219-250](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/setup.md?plain=1#L219-L250)] [[Source](https://code.claude.com/docs/en/setup#configure-release-channel)]
* New "Set version limits for your organization" subsection for managed `minimumVersion`. [[line 250](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/setup.md?plain=1#L250)] [[Source](https://code.claude.com/docs/en/setup#set-version-limits-for-your-organization)]

#### [skills](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)]

* Custom commands have been merged into skills: `.claude/commands/` files still work and Claude can invoke them. Use `disable-model-invocation: true` to stop that. [[line 13](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/skills.md?plain=1#L13)] [[Source](https://code.claude.com/docs/en/skills#extend-claude-with-skills)]
* Synced skills in terminal and VS Code sessions don't run `!` commands or attach `@` files. Live change detection covers `SKILL.md` text only. [[lines 314-322](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/skills.md?plain=1#L314-L322)] [[Source](https://code.claude.com/docs/en/skills#how-claude-code-handles-the-body-of-a-synced-skill)]
* A project skill's `allowed-tools` applies even in `-p` runs in untrusted folders. [[line 621](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/skills.md?plain=1#L621)] [[Source](https://code.claude.com/docs/en/skills#pre-approve-tools-for-a-skill)]

#### [slash-commands](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/slash-commands.md) [[Source](https://code.claude.com/docs/en/slash-commands)]

* The same skill and custom-command changes as in `skills`. [[line 13](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/slash-commands.md?plain=1#L13)] [[Source](https://code.claude.com/docs/en/slash-commands#extend-claude-with-skills)]

#### [sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* Subagent models are now described relative to the parent conversation. A nested subagent inherits from the subagent that spawned it, and `inherit` follows the same rule. [[lines 35-61](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/sub-agents.md?plain=1#L35-L61)] [[Source](https://code.claude.com/docs/en/sub-agents#built-in-subagents)]
* Rewritten model-order list: per-invocation parameter, definition `model`, `CLAUDE_CODE_SUBAGENT_MODEL`, then the parent's model. [[lines 345-358](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/sub-agents.md?plain=1#L345-L358)] [[Source](https://code.claude.com/docs/en/sub-agents#choose-a-model)]

#### [vs-code](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/vs-code.md) [[Source](https://code.claude.com/docs/en/vs-code)]

* New "Use or turn off suggested prompts" section (Tab to accept, `promptSuggestionEnabled`). [[lines 201-209](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/vs-code.md?plain=1#L201-L209)] [[Source](https://code.claude.com/docs/en/vs-code#use-or-turn-off-suggested-prompts)]

#### [worktrees](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/worktrees.md) [[Source](https://code.claude.com/docs/en/worktrees)]

* A reopened worktree starts fresh from the default branch only if the sandbox isn't restricting writes and the worktree is clean. Otherwise it reopens at its old tip, and `git fetch origin` plus a new `--worktree` name starts from the latest default branch. [[lines 231-245](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/claude-code/worktrees.md?plain=1#L231-L245)] [[Source](https://code.claude.com/docs/en/worktrees#reuse-a-worktree-name)]

-----

## API changes

### New Documents

None.

### Changed documents

About 780 API reference pages were regenerated, mostly the per-language SDK and CLI references (`typescript`, `python`, `csharp`, `cli` and the raw HTTP pages). The changes below recur across them.

#### [api/python/beta](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/api/api/python/beta.md) [[Source](https://platform.claude.com/docs/en/api/python/beta)]

* New "Errors" section for `BetaOrganizationNotEnrolledInBetaError` and `BetaUnsupportedCharsetError` (HTTP 400), with `details` types. [[lines 539-627](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/api/api/python/beta.md?plain=1#L539-L627)] [[Source](https://platform.claude.com/docs/en/api/python/beta#beta-organization-not-enrolled-in-beta-error-details)]
* Per-method "Errors" lists on Models and Messages, such as `ClaudeCodeKeyCreatorNotMemberError`, `OrganizationOnHoldError`, `AvailableToolsLimitExceededError`, `ClaudeCodeVersionTooOldError` and `CMEKKeyDisabledError`. A note explains how to tell streaming errors apart by error code. [[lines 1027-1040](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/api/api/python/beta.md?plain=1#L1027-L1040)] [[Source](https://platform.claude.com/docs/en/api/python/beta#returns)]

#### [api/beta/agents/create](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/api/api/beta/agents/create.md) [[Source](https://platform.claude.com/docs/en/api/beta/agents/create)]

* Example responses no longer show the populated `multiagent` block (`advisor`, `subagents`, `workflows`, type `multiagent_20261001`) and show `"multiagent": null`. The same change applies to the other agents, deployments, sessions and environments pages and their CLI equivalents. The TypeScript reference still documents `multiagent_20261001`, including its merge semantics on update. [[line 1971](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/api/api/beta/agents/create.md?plain=1#L1971)] [[Source](https://platform.claude.com/docs/en/api/beta/agents/create#response-200)]

#### [api/beta/messages](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/api/api/beta/messages.md) [[Source](https://platform.claude.com/docs/en/api/beta/messages)]

* Example responses simplified: `citations`, `diagnostics` and `stop_details` now show `null` instead of sample objects. [[Messages page](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/api/api/beta/messages.md)]

#### [api/typescript/beta](https://github.com/gpambrozio/ClaudeDocs/blob/fe64a31143080f1c2631d94da43d0fb22ab007fd/docs-md/api/api/typescript/beta.md) [[Source](https://platform.claude.com/docs/en/api/typescript/beta)]

* Largest regeneration (about 150k changed lines, along with `typescript/beta/messages`, `typescript/messages` and `typescript/beta/sessions`). This is mainly reformatting and restructuring of the generated reference. The multiagent coordinator agent types (`BetaManagedAgentsSessionMultiagentCoordinatorAgent`) are added to the C# reference.

#### Deprecation notices across the reference pages

* Roughly 580 "This value is no longer needed. Remove it from your requests." notes were removed from beta header values. Migration notices for the Skills and Files beta headers were removed, and `advisor-tool-2026-03-01` was removed from the beta value lists. The end-of-life notice for models retiring November 30, 2026 (migrate to `claude-sonnet-5-5`) was also removed from some pages.
