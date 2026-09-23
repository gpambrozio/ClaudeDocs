# [Claude docs changes for September 23rd, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/f777d4c30946e90f1138c87c54d07df75f3121e6) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/f777d4c30946e90f1138c87c54d07df75f3121e6)]

## Executive Summary
- **Claude Opus 5.5** (`claude-opus-5-5`) launched and is now the default Opus model everywhere — 1M context, $4/$20 per MTok (down from Opus 5's $5/$25), always-on adaptive thinking, and four breaking changes for existing Opus 5 integrations: thinking can't be disabled, forced tool use (`tool_choice: any`/`tool`) is rejected, thinking blocks are bound to the model/conversation, and the Claude API/Google Cloud drop the older `computer_20251124` tool in favor of the `computer_toolset_20260801` toolset.
- Claude Code 2.1.280 makes Opus the default model on **Pro and Team Standard** plans too (previously Sonnet), matching Max/Team Premium/Enterprise, and reworks effort-level defaults so newly released models like Opus 5.5 start at their own default (`medium`) instead of inheriting an old saved level.
- New MCP connector beta (`mcp-client-2026-09-15`) lets you **pin an MCP server's tool list** so a server that changes its tools mid-session doesn't change what Claude sees, and a companion beta (`inline-tools-2026-09-15`) lets a mid-conversation system message **define a tool by full value** instead of just referencing it — both keep the prompt cache intact.
- Safety and reliability fixes: auto mode no longer retries a denied action forever, file writes through a symlinked path are now judged by where they actually land (closing a permission bypass), and a stray `manifest.json` in `~/.claude/skills/` no longer moves personal skills into `.trash/`.
- The VS Code extension gains `/status`, `/sandbox`, `/chrome`, `/export`, and `/plan` command-menu dialogs, plus per-skill visibility controls in the `/skills` dialog; the TypeScript Agent SDK adds alpha support for **MCP Apps** (`readMcpResource()` to render a tool's `ui://` widget) and a way for host applications to declare their own scheduled runs.

-----

## New Claude Code versions

### [2.1.280](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/versions/2.1.280.md)

#### New features

* Added Claude Opus 5.5 (`claude-opus-5-5`), now the default Opus model — 1M context, $4/$20 per Mtok with $0.20/Mtok cache reads
* Added mouse support to more lists in fullscreen mode: the wheel scrolls the `/skills` list, and a skill's state options in `/plugin` can be clicked
* Added `CLAUDE_CODE_MAX_MCP_DESCRIPTION_LENGTH` to change the 2,048-character cap on MCP tool descriptions and server instructions
* Added hook output sizes and the number of oversized outputs saved to a file to the `hook_execution_complete` OpenTelemetry event
* [VS Code] Added a Status dialog (`/status`), a Sandbox dialog (`/sandbox`), a Claude in Chrome dialog (`/chrome`), Export conversation (`/export`), a typed `/plan`, and each skill's source/token estimate/on-off state in the Slash commands dialog (`/skills`)
* [Claude Tag] Added Slack's native Working indicator, Stop button, and thread title to Claude's threads in channels

#### Existing feature improvements

* Changed the default model on Pro and Team Standard plans from Sonnet to Opus, matching Max, Team Premium, and Enterprise
* Changed effort-level resolution: an effort level saved before `/effort` became per-model no longer applies to newly released models such as Opus 5.5, which start at their own default until you pick a level; Opus 4.7, Opus 4.8, and Fable 5 also stop holding their launch-default effort over other settings
* Improved `/permissions`: focus returns to the rule list after viewing, adding, or deleting a rule, and delete-rule/remove-directory confirmations now default to No
* Improved code blocks that don't name a language: colored like inline code, so commands stand out from surrounding text
* Improved `@` file suggestions: a file whose name matches the query now ranks above one that only matches across folder names
* Improved artifact pages: no Print buttons or device features the viewer blocks, and dark mode that reaches form controls and scrollbars
* Improved `/ultrareview` uploads: renamed copies of key files, such as `id_rsa copy`, now also stay on your machine

#### Major bug fixes

* Fixed conversations failing on every turn with a "role 'system' must precede an 'assistant' message" API error
* Fixed writes through a symlinked path being judged by their in-tree spelling: `acceptEdits`, allow rules, and auto mode no longer approve a write that actually lands outside the intended path
* Fixed auto mode retrying an action over and over when a safety check declined to review it (now denied once); fixed auto mode denying actions over and over without pause when a safety check gave no answer (retries now back off, and the turn stops after ten in a row)
* Fixed Write tool calls failing validation when a model sends `path`, `file_text`, or `file_content` instead of `file_path` and `content`
* Fixed resuming a session with unfinished background agents, shells, or workflows starting a model turn on its own before you typed anything
* Fixed messages sent to a background subagent being silently lost in headless and SDK sessions
* Fixed a finished subagent's report being lost when the conversation that launched it was compacted before the report was read
* Fixed one cause of long-running fullscreen sessions exiting with "Claude Code exited after an unrecoverable interface error"
* Fixed Claude Code hanging when a settings file is replaced by a named pipe mid-read
* Fixed background plugin marketplace auto-update ignoring git credential helpers, so private-repo marketplaces were re-cloned every run or never updated
* Fixed skills in `~/.claude/skills/` being moved to `~/.claude/skills/.trash/` when a `manifest.json` in that folder listed their names
* [VS Code] Fixed Claude Code never starting when the Python extension hangs while activating
* [Claude Code on the web] Fixed `gh` and GitHub API calls inside a cloud session on a GitHub Enterprise Server repository failing after about eight hours

-----

## Claude Code changes

### Changed documents

#### [agent-sdk/typescript](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* New alpha `readMcpResource(serverName, uri)` query method and `SDKControlMcpReadResourceResponse` type: reads an MCP Apps `ui://` resource from a connected server so an application can render a tool's widget; requires the server capability `mcp_read_resource_v1`. [[lines 543-574, 863-882](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L863-L882)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#query-object)]
* New `inline_pastes` field on `SDKUserMessage`: lists which parts of `message.content` the user pasted rather than typed, so Claude Code can wrap them in `<pasted_content>` tags. [[line 1273, 1287](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L1287)]
* New way to declare a host-scheduled run: set `CLAUDE_CODE_HOST_SCHEDULED_RUN=1` and send the run's message with `origin: { kind: "task-notification", subkind: "scheduled-trigger", fireReason: "..." }` so Claude Code frames the turn as a scheduled task rather than live user input; a new `fireReason` field also appears on Anthropic-verified routine deliveries. [[lines 1799-1836](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L1830-L1836)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#declare-a-scheduled-run)]
* `McpServerStatus`'s `tools` entries gained `_meta`, carrying an MCP Apps tool's `ui://` resource URI and visibility, for use with `readMcpResource()`. [[lines 4535, 4542](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L4542)]

#### [artifacts](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/claude-code/artifacts.md) [[Source](https://code.claude.com/docs/en/artifacts)]

* Documented that artifact availability depends on Claude Code loading your organization's policy from `api.anthropic.com`; a proxy, VPN, or web filter that blocks it makes artifacts unavailable until it loads, and Claude now says why when you ask for one. [[lines 301-303](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/claude-code/artifacts.md?plain=1#L301-L303)] [[Source](https://code.claude.com/docs/en/artifacts#availability)]

#### [claude-directory](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/claude-code/claude-directory.md) [[Source](https://code.claude.com/docs/en/claude-directory)]

* New "Frontmatter fields by file" reference table listing which frontmatter fields skills, commands, subagents, output styles, and rules each accept. [[lines 1286-1299](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/claude-code/claude-directory.md?plain=1#L1286-L1299)] [[Source](https://code.claude.com/docs/en/claude-directory#frontmatter-fields-by-file)]

#### [claude-md](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/claude-code/claude-md.md) [[Source](https://code.claude.com/docs/en/claude-md)] / [memory](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/claude-code/memory.md)

* New "Rule frontmatter reference" documenting the `paths` field that scopes a `.claude/rules/` file, and how a parse error is handled. [[lines 215-227](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/claude-code/memory.md?plain=1#L215-L227)] [[Source](https://code.claude.com/docs/en/memory#rules-frontmatter-reference)]
* `/memory` and `/context` now list an `AGENTS.md` that Claude reads directly through the Project instructions setting, not just one a `CLAUDE.md` imports. [[line 558](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/claude-code/memory.md?plain=1#L558)] [[Source](https://code.claude.com/docs/en/memory#agents-md-isnt-being-read)]

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* On macOS and Linux, a plugin marketplace entry whose source path contains a backslash after the leading `./` is now refused, alongside the existing absolute/`..`/network-path refusals. [[line 3235](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/claude-code/errors.md?plain=1#L3235)] [[Source](https://code.claude.com/docs/en/errors#plugin-source-path-refused)]

#### [fast-mode](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/claude-code/fast-mode.md) [[Source](https://code.claude.com/docs/en/fast-mode)]

* `/fast` now toggles with Space and confirms with Enter, instead of toggling with Tab. [[line 24](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/claude-code/fast-mode.md?plain=1#L24)] [[Source](https://code.claude.com/docs/en/fast-mode#toggle-fast-mode)]
* Opus 5.5 is now the fast mode default, at $8/$40 per MTok (Opus 5 and Opus 4.8 stay at $10/$50). [[lines 42, 69](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/claude-code/fast-mode.md?plain=1#L69)]

#### [ide-integrations](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/claude-code/ide-integrations.md) [[Source](https://code.claude.com/docs/en/ide-integrations)] / [vs-code](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/claude-code/vs-code.md)

* New `/plan` typed command: switches to plan mode, starts planning a task you give it, or opens the current plan file. [[lines 98-101](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/claude-code/vs-code.md?plain=1#L98-L101)] [[Source](https://code.claude.com/docs/en/vs-code#use-the-prompt-box)]
* Typing `/skills` now opens the Slash commands dialog with each skill's visibility (**On**/**Name only**/locked) shown and clickable to change. [[line 114](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/claude-code/vs-code.md?plain=1#L114)] [[Source](https://code.claude.com/docs/en/vs-code#use-the-prompt-box)]
* New Customize section entries: **Status** (`/status`), **Sandbox** (`/sandbox`), **Claude in Chrome** (`/chrome`), and **Export conversation** (`/export`, optionally with a filename to skip the dialog). [[lines 124-127](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/claude-code/vs-code.md?plain=1#L124-L127)] [[Source](https://code.claude.com/docs/en/vs-code#use-the-prompt-box)]
* New "Paste text" section: pasted text stays visible instead of collapsing to a placeholder, and invisible Unicode characters are stripped from pasted (and sent) text with a notice. [[lines 178-186](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/claude-code/vs-code.md?plain=1#L178-L186)] [[Source](https://code.claude.com/docs/en/vs-code#paste-text)]

#### [keybindings](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/claude-code/keybindings.md) [[Source](https://code.claude.com/docs/en/keybindings)]

* `confirm:yes`/`confirm:no` default bindings dropped `Y`/`N`, keeping only Enter/Escape, so a bare `y`/`n` binding no longer acts on dialogs that don't show those letters as their own keys (opt back in by binding them explicitly in `keybindings.json`). [[lines 136-165](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/claude-code/keybindings.md?plain=1#L136-L165)] [[Source](https://code.claude.com/docs/en/keybindings#confirmation-actions)]
* `select:first`/`select:last` bindings, plus Home/End, now apply in most selection lists (such as `/model`), not just `/skills`. [[lines 347-349](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/claude-code/keybindings.md?plain=1#L347-L349)] [[Source](https://code.claude.com/docs/en/keybindings#select-actions)]

#### [llm-gateway-protocol](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/claude-code/llm-gateway-protocol.md) [[Source](https://code.claude.com/docs/en/llm-gateway-protocol)]

* When a gateway or upstream rejects the advisor tool as unrecognized (a `400`/`422` naming the tool type after `Input tag`, such as `Input tag 'advisor_20260301'`), Claude Code now retries once without it and disables `/advisor` for that base URL until exit, instead of failing every turn. [[line 221](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/claude-code/llm-gateway-protocol.md?plain=1#L221)] [[Source](https://code.claude.com/docs/en/llm-gateway-protocol#automatic-retry-and-error-forwarding)]

#### [model-config](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* The `opus` alias now resolves to Opus 5.5 on the Anthropic API, Claude Platform on AWS, Amazon Bedrock, and Google Cloud's Agent Platform, and `default` now resolves to Opus 5.5 on Pro as well as the account types that already defaulted to Opus. [[lines 39-54, 399-403](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/claude-code/model-config.md?plain=1#L399-L403)] [[Source](https://code.claude.com/docs/en/model-config#default-model-behavior)]
* Switching models with `/model` now also changes the model of subagents that inherit the main conversation's model, since Claude Code resolves a subagent's model when it's started, not when it's defined. [[line 121](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/claude-code/model-config.md?plain=1#L121)] [[Source](https://code.claude.com/docs/en/model-config#setting-your-model)]
* Simplified effort-level resolution: the per-model "hold" on Fable 5, Opus 4.7, and Opus 4.8's default effort is gone, replaced by each model simply falling back to its own default (`medium` for Opus 5.5, `xhigh` for Opus 4.7, `high` otherwise) when nothing else sets a level. [[lines 512-528](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/claude-code/model-config.md?plain=1#L512-L528)] [[Source](https://code.claude.com/docs/en/model-config#adjust-effort-level)]

#### [monitoring-usage](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* `hook_execution_complete` gained `stdout_chars`, `additional_context_chars`, `system_message_chars`, `initial_user_message_chars`, and `num_outputs_persisted` (hook outputs saved to a file over the 10,000-character cap). [[lines 1112-1116](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/claude-code/monitoring-usage.md?plain=1#L1112-L1116)] [[Source](https://code.claude.com/docs/en/monitoring-usage#hook-execution-complete-event)]

#### [network-config](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/claude-code/network-config.md) [[Source](https://code.claude.com/docs/en/network-config)]

* Added `github.com` to the required-URLs allowlist table, for cloning GitHub-hosted plugin marketplaces and plugins (including the official Anthropic marketplace) over HTTPS or SSH. [[line 208](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/claude-code/network-config.md?plain=1#L208)] [[Source](https://code.claude.com/docs/en/network-config#required-urls)]

#### [output-styles](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/claude-code/output-styles.md) [[Source](https://code.claude.com/docs/en/output-styles)]

* Largely rewritten: **Default** is now documented as an explicit, selectable style (`default` appears in the `/output-style` list); each built-in style got its own subsection with examples; `outputStyle` can now be set in `~/.claude/settings.json` as a cross-project default and is case-sensitive; and a new "Choose between an output style and other features" table replaces the old feature-comparison table, adding hooks and `--append-system-prompt` to the comparison. [[lines 1-193](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/claude-code/output-styles.md?plain=1#L167-L193)] [[Source](https://code.claude.com/docs/en/output-styles#choose-between-an-output-style-and-other-features)]

#### [plugin-marketplaces](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/claude-code/plugin-marketplaces.md) [[Source](https://code.claude.com/docs/en/plugin-marketplaces)]

* Background marketplace auto-update now checks for new commits using your configured git credential helpers (never prompting), instead of always disabling them; a helper that would need to prompt still fails quietly and keeps the existing checkout, and the previous global-URL-rewrite workaround is no longer needed. [[lines 774-797](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/claude-code/plugin-marketplaces.md?plain=1#L774-L797)] [[Source](https://code.claude.com/docs/en/plugin-marketplaces#background-auto-updates)]

#### [plugins-reference](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/claude-code/plugins-reference.md) [[Source](https://code.claude.com/docs/en/plugins-reference)]

* New "Plugin agent frontmatter" section: documents that `color` and `experimental` are now supported for plugin agents, and `initialPrompt` is explicitly not supported (in addition to the existing `hooks`/`mcpServers`/`permissionMode` restriction). [[lines 62-67](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/claude-code/plugins-reference.md?plain=1#L62-L67)] [[Source](https://code.claude.com/docs/en/plugins-reference#plugin-agent-frontmatter)]
* New "Limit a field to fixed options" section documenting the validation rules for a `userConfig` field's `options` list (a fixed picker of choices), and a worked example. [[lines 641-677](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/claude-code/plugins-reference.md?plain=1#L641-L677)] [[Source](https://code.claude.com/docs/en/plugins-reference#limit-a-field-to-fixed-options)]

#### [settings-example](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/claude-code/settings-example.md) [[Source](https://code.claude.com/docs/en/settings-example)]

* Example settings file now sets effort per model under `modelSettings` instead of the top-level `effortLevel` key, reflecting the new per-model effort resolution. [[lines 23-27, 54-59](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/claude-code/settings-example.md?plain=1#L54-L59)]

#### [settings-reference](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/claude-code/settings-reference.md) [[Source](https://code.claude.com/docs/en/settings-reference)]

* Clarified `effortLevel`: in your user settings file it's the legacy form `/effort` wrote before per-model levels existed, and it keeps applying only to Opus 5, Fable 5.1, and earlier models — Opus 5.5 and later models ignore it and start at their own default until you save a level under `modelSettings`. In project/local/managed settings or `--settings`, it still applies to every model. [[line 860](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/claude-code/settings-reference.md?plain=1#L860)] [[Source](https://code.claude.com/docs/en/settings-reference#effortlevel)]
* `fastMode` now also runs on Opus 5.5. [[line 908](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/claude-code/settings-reference.md?plain=1#L908)] [[Source](https://code.claude.com/docs/en/settings-reference#fastmode)]

#### [skills](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)] / [slash-commands](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/claude-code/slash-commands.md)

* New "Personal skills disappeared" troubleshooting entry: explains the (now-fixed) `manifest.json`-triggered move to `~/.claude/skills/.trash/`, and how to restore a skill from there before the 30-day retention sweep. [[lines 1071-1077](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/claude-code/skills.md?plain=1#L1071-L1077)] [[Source](https://code.claude.com/docs/en/skills#personal-skills-disappeared)]
* Frontmatter reference: field names must match exactly (case included) or they're silently ignored, and a skill with unparseable YAML frontmatter now still loads with no fields set rather than failing. [[lines 306-319](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/claude-code/skills.md?plain=1#L306-L319)] [[Source](https://code.claude.com/docs/en/skills#frontmatter-reference)]

#### [sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* Background subagents can now use the `LSP` tool (previously dropped along with other non-essential built-ins). [[line 415](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/claude-code/sub-agents.md?plain=1#L415)] [[Source](https://code.claude.com/docs/en/sub-agents#available-tools)]
* The `--agents` CLI flag's JSON now explicitly ignores (rather than rejects) `color` and `experimental`, which aren't supported there. [[line 211](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/claude-code/sub-agents.md?plain=1#L211)] [[Source](https://code.claude.com/docs/en/sub-agents#define-subagents-via-cli)]

#### [ultrareview](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/claude-code/ultrareview.md) [[Source](https://code.claude.com/docs/en/ultrareview)]

* Claude now tells you explicitly when an in-progress review's cloud session was stopped/archived, or when it can't be found (deleted, or you switched accounts) — with guidance to `claude --resume` under the account that started it. [[lines 136-141](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/claude-code/ultrareview.md?plain=1#L136-L141)] [[Source](https://code.claude.com/docs/en/ultrareview#monitor-a-review)]

#### [voice-dictation](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/claude-code/voice-dictation.md) [[Source](https://code.claude.com/docs/en/voice-dictation)]

* New "Cancel a recording" section: Esc or Ctrl+C now cancels a dictation (or its still-processing transcript) and restores the prompt, without interrupting Claude's response or counting toward the two-press exit. [[lines 90-96](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/claude-code/voice-dictation.md?plain=1#L90-L96)] [[Source](https://code.claude.com/docs/en/voice-dictation#cancel-a-recording)]
* Holding/tapping Space to dictate now only fires where the keypress would otherwise type text — it no longer hijacks Space in the transcript viewer (paging) or vim NORMAL mode (a command). [[line 64](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/claude-code/voice-dictation.md?plain=1#L64)] [[Source](https://code.claude.com/docs/en/voice-dictation#hold-to-record-and-release-to-send)]

-----

## API changes

### New Documents

#### [models/opus-5-5/overview](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/api/models/opus-5-5/overview.md) [[Source](https://platform.claude.com/docs/en/models/opus-5-5/overview)]

The model page for Claude Opus 5.5, released September 22, 2026: model IDs across every platform, a 1M-token context window, 128K max output, $4/$20 per MTok pricing with $0.20/MTok cache reads, availability, and links to the related guides.

#### [models/opus-5-5/whats-new-opus-5-5](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/api/models/opus-5-5/whats-new-opus-5-5.md) [[Source](https://platform.claude.com/docs/en/models/opus-5-5/whats-new-opus-5-5)]

New guide covering Opus 5.5's four breaking changes (thinking can't be disabled, forced tool use unsupported, thinking blocks tied to the model/conversation, `computer_20251124` unsupported on the Claude API and Google Cloud), new beta feature support (inline tool definitions, compaction on demand), behavior differences from Opus 5 (default effort `medium`, more thinking per turn at a given effort, text between tool calls arrives as `thinking` blocks, more safeguard categories, sharper visual reading), pricing, and availability.

#### [models/opus-5-5/migration-guide](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/api/models/opus-5-5/migration-guide.md) [[Source](https://platform.claude.com/docs/en/models/opus-5-5/migration-guide)]

New step-by-step migration guide to Claude Opus 5.5 from Opus 5, Opus 4.8, Opus 4.7 and earlier Opus models, and Sonnet 5, with a checklist for each breaking change.

#### [build-with-claude/prompt-engineering/prompting-claude-opus-5-5](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/api/build-with-claude/prompt-engineering/prompting-claude-opus-5-5.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5)]

New prompting guide for Claude Opus 5.5: capability improvements relevant to prompting, calibrating effort, adapting prompts written for thinking-disabled, guidance for unattended agentic runs, safeguard refusals, requesting more user-facing progress updates, context in multi-app workflows, time signals for multi-agent harnesses, thinking instructions in chat system prompts, marking pasted text, tools for complex visual inputs, and frontend design defaults.

### Changed documents

#### [about-claude/model-deprecations](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/api/about-claude/model-deprecations.md) [[Source](https://platform.claude.com/docs/en/about-claude/model-deprecations)]

* Added `claude-opus-5-5`, Active, retirement not sooner than September 22, 2027. [[line 78](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/api/about-claude/model-deprecations.md?plain=1#L78)] [[Source](https://platform.claude.com/docs/en/about-claude/model-deprecations#model-status)]

#### [about-claude/models/choosing-a-model](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/api/about-claude/models/choosing-a-model.md) [[Source](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model)]

* Opus 5.5 replaces Opus 5 as the recommended starting point for "complex agentic coding and enterprise work" and in the capability-first workflow; Claude Fable 5 and Claude Mythos 5 were dropped from the "also available" callout. [[lines 14-73](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/api/about-claude/models/choosing-a-model.md?plain=1#L58-L73)] [[Source](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model#establish-key-criteria)]

#### [about-claude/pricing](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/api/about-claude/pricing.md) [[Source](https://platform.claude.com/docs/en/about-claude/pricing)]

* Added Claude Opus 5.5 pricing throughout: $4/$20 base, $5/$8 cache writes, $0.20 cache reads (5% of base input, a new multiplier tier alongside the 10% standard and 2.5% Fable/Mythos rates), $2/$10 batch, and $8/$40 fast mode. [[lines 23, 40-42, 142-144, 160-166, 188, 229](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/api/about-claude/pricing.md?plain=1#L142-L144)]

#### [agents-and-tools/mcp-connector](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/api/agents-and-tools/mcp-connector.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/mcp-connector)]

* New beta feature: pin an MCP server's tool list with the `mcp-client-2026-09-15` beta header (superset of `mcp-client-2025-11-20`). The API records a server's tools in a response's `mcp_tool_listing` block; sending that block back, or copying its `tools` into an MCPToolset's new `tools` field, makes the API use that fixed list instead of asking the server again — so a server that changes its tools mid-conversation can't change what Claude sees. [[lines 359, 527-1097](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/api/agents-and-tools/mcp-connector.md?plain=1#L527-L560)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/mcp-connector#pin-an-mcp-servers-tool-list-beta)]

#### [build-with-claude/effort](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/api/build-with-claude/effort.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/effort)]

* New "Recommended effort levels for Claude Opus 5.5" section. [[section added](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/api/build-with-claude/effort.md?plain=1)]

#### [build-with-claude/mid-conversation-system-messages](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/api/build-with-claude/mid-conversation-system-messages.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages)]

* New beta feature: "Define tools in a message" — with the `inline-tools-2026-09-15` beta header, a `tool_addition` block can carry a tool's full definition (not just a name reference), so you can introduce a new tool, change a schema, or bump a server tool's version mid-conversation by appending a message, without touching the `tools` array or invalidating the prompt cache. The same header covers adding/removing tools by reference, superseding `mid-conversation-tool-changes-2026-07-01`. [[line 447](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/api/build-with-claude/mid-conversation-system-messages.md?plain=1#L447)] [[Source](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages#define-tools-in-a-message-beta)]
* New beta feature: "Add an MCP server mid-conversation" — combined with the MCP connector's tool-list pinning, an MCP server can be introduced partway through a conversation the same way. [[line 1019](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/api/build-with-claude/mid-conversation-system-messages.md?plain=1#L1019)] [[Source](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages#add-an-mcp-server-mid-conversation-beta)]

#### [manage-claude/cmek-aws-kms](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/api/manage-claude/cmek-aws-kms.md) [[Source](https://platform.claude.com/docs/en/manage-claude/cmek-aws-kms)]

* Reworked the KMS key-policy walkthrough: the policy now binds explicitly to your Anthropic organization ID via an `EncryptionContext` condition (validation refuses a key policy without it), with a new "Finding your organization ID" callout, and a separate, simpler path for Claude Platform on AWS (service-principal grant, no organization condition, no separate validation step) that skips most of the standard steps. [[lines 17, 36-99, 170](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/api/manage-claude/cmek-aws-kms.md?plain=1#L36-L99)] [[Source](https://platform.claude.com/docs/en/manage-claude/cmek-aws-kms#claude-platform-on-aws)]

#### [models/overview](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/api/models/overview.md) [[Source](https://platform.claude.com/docs/en/models/overview)]

* Comparison table now leads with Claude Opus 5.5 in place of Opus 5 (updated pricing, retirement date, always-on adaptive thinking, `medium` default effort); Opus 5 moved to the "Legacy models (still available)" list. [[lines 18-59](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/api/models/overview.md?plain=1#L18-L59)] [[Source](https://platform.claude.com/docs/en/models/overview#models-overview)]

#### [release-notes/overview](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/api/release-notes/overview.md) [[Source](https://platform.claude.com/docs/en/release-notes/overview)]

* Added a September 22, 2026 section with four entries: the Opus 5.5 launch, its breaking changes, fast mode availability for it, and the new inline-tool-definition/MCP-tool-pinning beta features. [[lines 15-23](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/api/release-notes/overview.md?plain=1#L15-L23)] [[Source](https://platform.claude.com/docs/en/release-notes/overview#september-22-2026)]

#### [resources/overview](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/api/resources/overview.md) [[Source](https://platform.claude.com/docs/en/resources/overview)]

* Added a link to the Claude Opus 5.5 System Card. [[lines 9-12](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/api/resources/overview.md?plain=1#L9-L12)] [[Source](https://platform.claude.com/docs/en/resources/overview#overview)]

#### Claude Opus 5.5 reference updates (well over 100 API reference and guide pages, e.g. [agents-and-tools/tool-use/computer-use-tool](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/api/agents-and-tools/tool-use/computer-use-tool.md), [build-with-claude/prompt-caching](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/api/build-with-claude/prompt-caching.md), [cli-sdks-libraries/sdks/python](https://github.com/gpambrozio/ClaudeDocs/blob/f777d4c30946e90f1138c87c54d07df75f3121e6/docs-md/api/cli-sdks-libraries/sdks/python.md))

* Nearly every remaining changed file in today's diff is a mechanical update for the Opus 5.5 launch: code examples switched from `claude-opus-5`/`Model.CLAUDE_OPUS_5` to `claude-opus-5-5`/`Model.CLAUDE_OPUS_5_5` across every language, feature-support tables and `featureMetadata` lists gained a `claude-opus-5-5` entry, and pages that call out Opus 5's specific behavior (fast mode, computer use tool versions, thinking-block binding, fallback routing, tool-use system-prompt token counts, SDK version bumps) added the equivalent Opus 5.5 note alongside it. None of these add information beyond what's in the Opus 5.5 pages above, so they aren't itemized file by file here.

-----
