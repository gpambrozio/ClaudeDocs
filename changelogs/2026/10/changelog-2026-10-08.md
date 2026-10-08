# [Claude docs changes for October 8th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/22b170d8584c52e49bbc1db54fa957f9bba13b47) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/22b170d8584c52e49bbc1db54fa957f9bba13b47)]

## Executive Summary
- Claude Haiku 5.5 (`claude-haiku-5-5`) launches: 1M context, $0.10/$0.50 per Mtok, new model docs, migration guide and prompting guide. It is now the default `haiku` alias on the Anthropic API in Claude Code 2.1.293.
- New Managed Agents docs cover live response previews via event deltas, and session inspection and usage tracking in the Console.
- New browser and computer use SDK toolset docs, plus a page on claiming monthly API credits with Max and Team plans.
- Claude Code docs add keybindings for the above-prompt band and mod panes, a full `subagentStatusLine` task field reference, and `--json` output for `plugin marketplace` commands.
- Claude Code 2.1.294 fixes `prompt` and `agent` hooks written as instructions (such as "Block commands that...") so they actually block.

## New Claude Code versions

### [2.1.293](https://github.com/gpambrozio/ClaudeDocs/blob/22b170d8584c52e49bbc1db54fa957f9bba13b47/versions/2.1.293.md)

#### New features

* Added Claude Haiku 5.5 (`claude-haiku-5-5`), now the default Haiku model on the Anthropic API (1M context, $0.10/$0.50 per Mtok)
* Added `agentType` to the `subagentStatusLine` payload
* Added `isDeferred` to `$.tool.register` for mods, so a tool's schema can be listed in the prompt from the start instead of behind tool search
* `mock.session` added to `claude plugin test` so tests can read rows appended with `$.session.append`

#### Existing feature improvements

* Faster startup for Team and Enterprise orgs: policy and managed settings are fetched earlier, with a retry after 3 seconds
* Improved Claude in Chrome reliability and its cloud-session error message for multi-organization users
* Artifacts now pin libraries to exact versions that are at least two weeks old
* claude.ai skill syncing now checks about every 40 minutes instead of every 10 while idle
* Agent lists and MCP server announcements now sort non-ASCII names after ASCII names
* `claude purge` now deletes what it can, lists what it couldn't, and exits 1
* Claude Tag: channel rule limit raised from 20 to 50; Claude joins announcement channels without posting its intro
* Code Review's Add a repository dialog now explains why each repository couldn't be added

#### Major bug fixes

* Fixed Claude treating its own last actions before a context compaction as done, and retracting or redoing finished work
* Fixed a memory leak in HTTP MCP connections
* Fixed messages being lost when `←` moved a session to the background, and several related backgrounding issues
* Fixed `/model` effort selection wrapping around and accidentally saving Low as a model's default
* Fixed path-scoped rules and nested CLAUDE.md files not loading when Claude views files through Bash `cat`, `head`, `tail`, `sed -n` or `grep`
* Fixed `claude logs`, `stop`, `kill`, `rm` and daemon commands sometimes signing you out
* Fixed `claude plugin eval` refusing Bash-granting runs on Macs with Docker Desktop
* Fixed `/ultrareview` upload refusing some repositories on Linux
* Reverted the 2.1.281 auto mode denial message change and the 2.1.290 cloud session wakeup fix

### [2.1.294](https://github.com/gpambrozio/ClaudeDocs/blob/22b170d8584c52e49bbc1db54fa957f9bba13b47/versions/2.1.294.md)

#### Existing feature improvements

* Improved how `prompt` hooks on Stop and SubagentStop written as instructions are judged, so Claude is less likely to stop early

#### Major bug fixes

* Fixed `prompt` and `agent` hooks written as instructions (such as "Block commands that...") allowing what they should block

-----

## Claude Code changes

### Changed documents

#### [headless](https://github.com/gpambrozio/ClaudeDocs/blob/22b170d8584c52e49bbc1db54fa957f9bba13b47/docs-md/claude-code/headless.md) [[Source](https://code.claude.com/docs/en/headless)]

* Stream output docs now cover forked skills as well as subagents, and explain `parent_tool_use_id` values, including the `forked-command-` prefix for a skill started with `/<skill-name>` as the prompt. [[lines 190-199](https://github.com/gpambrozio/ClaudeDocs/blob/22b170d8584c52e49bbc1db54fa957f9bba13b47/docs-md/claude-code/headless.md?plain=1#L190-L199)] [[Source](https://code.claude.com/docs/en/headless#follow-subagent-messages)]
* Added a table of how a run starts, which `parent_tool_use_id` it carries and when its messages arrive, plus minimum Claude Code versions for each forwarding behavior. [[lines 199-215](https://github.com/gpambrozio/ClaudeDocs/blob/22b170d8584c52e49bbc1db54fa957f9bba13b47/docs-md/claude-code/headless.md?plain=1#L199-L215)] [[Source](https://code.claude.com/docs/en/headless#follow-subagent-messages)]

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/22b170d8584c52e49bbc1db54fa957f9bba13b47/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* WorktreeRemove now documents when it runs on exiting an interactive worktree session, including automatic removal of unnamed worktrees with no changes. It warns that non-git directories always look clean, so the hook should check for uncommitted work. [[lines 2977-2985](https://github.com/gpambrozio/ClaudeDocs/blob/22b170d8584c52e49bbc1db54fa957f9bba13b47/docs-md/claude-code/hooks.md?plain=1#L2977-L2985)] [[Source](https://code.claude.com/docs/en/hooks#worktreeremove)]

#### [keybindings](https://github.com/gpambrozio/ClaudeDocs/blob/22b170d8584c52e49bbc1db54fa957f9bba13b47/docs-md/claude-code/keybindings.md) [[Source](https://code.claude.com/docs/en/keybindings)]

* New contexts `AbovePrompt`, `AbovePromptInput` and `AbovePromptSelect`. [[lines 63-65](https://github.com/gpambrozio/ClaudeDocs/blob/22b170d8584c52e49bbc1db54fa957f9bba13b47/docs-md/claude-code/keybindings.md?plain=1#L63-L65)] [[Source](https://code.claude.com/docs/en/keybindings#contexts)]
* New "Above-prompt actions" (`abovePrompt:toggle`, `focus`, `next`, `press` and more) and "Pane actions" (`pane:scrollUp`, `grow`, `close` and more) for mod-drawn UI, with default keys. [[lines 396-437](https://github.com/gpambrozio/ClaudeDocs/blob/22b170d8584c52e49bbc1db54fa957f9bba13b47/docs-md/claude-code/keybindings.md?plain=1#L396-L437)] [[Source](https://code.claude.com/docs/en/keybindings#above-prompt-actions)]

#### [model-config](https://github.com/gpambrozio/ClaudeDocs/blob/22b170d8584c52e49bbc1db54fa957f9bba13b47/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* Alias table now includes `haiku`: Haiku 5.5 on the Anthropic API, Haiku 4.5 on other providers. Haiku 5.5 needs v2.1.293 or later. [[lines 36-57](https://github.com/gpambrozio/ClaudeDocs/blob/22b170d8584c52e49bbc1db54fa957f9bba13b47/docs-md/claude-code/model-config.md?plain=1#L36-L57)] [[Source](https://code.claude.com/docs/en/model-config#model-aliases)]
* Resumed sessions on a Haiku model move to whatever `haiku` resolves to now. [[lines 139-141](https://github.com/gpambrozio/ClaudeDocs/blob/22b170d8584c52e49bbc1db54fa957f9bba13b47/docs-md/claude-code/model-config.md?plain=1#L139-L141)] [[Source](https://code.claude.com/docs/en/model-config#setting-your-model)]
* Haiku 5.5 supports all five effort levels and defaults to `medium`. `/effort status` shows the active level. Fallback effort text was simplified. [[lines 525-593](https://github.com/gpambrozio/ClaudeDocs/blob/22b170d8584c52e49bbc1db54fa957f9bba13b47/docs-md/claude-code/model-config.md?plain=1#L525-L593)] [[Source](https://code.claude.com/docs/en/model-config#effort-level-after-a-fallback)]

#### [plugins/cli-reference](https://github.com/gpambrozio/ClaudeDocs/blob/22b170d8584c52e49bbc1db54fa957f9bba13b47/docs-md/claude-code/plugins/cli-reference.md) [[Source](https://code.claude.com/docs/en/plugins/cli-reference)]

* `plugin marketplace add`, `remove` and `update` accept `--json` and print a result object, documented with `command`, `outcome`, `marketplace` and `failureCode` fields (v2.1.287+). [[lines 120-134](https://github.com/gpambrozio/ClaudeDocs/blob/22b170d8584c52e49bbc1db54fa957f9bba13b47/docs-md/claude-code/plugins/cli-reference.md?plain=1#L120-L134)] [[Source](https://code.claude.com/docs/en/plugins/cli-reference#json-result-for-marketplace-commands)]
* `plugin eval` JSON report adds `gatingHooks`, which shows whether refusing mod hooks have a `.catch` handler. [[line 636](https://github.com/gpambrozio/ClaudeDocs/blob/22b170d8584c52e49bbc1db54fa957f9bba13b47/docs-md/claude-code/plugins/cli-reference.md?plain=1#L636)] [[Source](https://code.claude.com/docs/en/plugins/cli-reference#output-and-exit-codes)]

#### [plugins/mods/api](https://github.com/gpambrozio/ClaudeDocs/blob/22b170d8584c52e49bbc1db54fa957f9bba13b47/docs-md/claude-code/plugins/mods/api.md) [[Source](https://code.claude.com/docs/en/plugins/mods/api)]

* Tools deferred by MCP tool search hide their description; set `isDeferred: false` to always show it. [[line 64](https://github.com/gpambrozio/ClaudeDocs/blob/22b170d8584c52e49bbc1db54fa957f9bba13b47/docs-md/claude-code/plugins/mods/api.md?plain=1#L64)] [[Source](https://code.claude.com/docs/en/plugins/mods/api#add-a-tool)]
* Documented what happens when a mod refuses a `$.process.spawn` call after the command has already started or finished. [[lines 189-193](https://github.com/gpambrozio/ClaudeDocs/blob/22b170d8584c52e49bbc1db54fa957f9bba13b47/docs-md/claude-code/plugins/mods/api.md?plain=1#L189-L193)] [[Source](https://code.claude.com/docs/en/plugins/mods/api#reach-files-processes-and-the-network)]

#### [plugins/mods/gallery](https://github.com/gpambrozio/ClaudeDocs/blob/22b170d8584c52e49bbc1db54fa957f9bba13b47/docs-md/claude-code/plugins/mods/gallery.md) [[Source](https://code.claude.com/docs/en/plugins/mods/gallery)]

* Explained when `Image` elements fall back to dimmed `alt` text (unsupported terminals, tmux/screen, background sessions) and the `CLAUDE_CODE_FORCE_TERMINAL_IMAGES` override. [[lines 374-381](https://github.com/gpambrozio/ClaudeDocs/blob/22b170d8584c52e49bbc1db54fa957f9bba13b47/docs-md/claude-code/plugins/mods/gallery.md?plain=1#L374-L381)] [[Source](https://code.claude.com/docs/en/plugins/mods/gallery#image-and-client)]

#### [quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/22b170d8584c52e49bbc1db54fa957f9bba13b47/docs-md/claude-code/quickstart.md) [[Source](https://code.claude.com/docs/en/quickstart)]

* Noted that the installer shows no progress while downloading, and reorganized the example prompts and command lists into clearer sections. [[lines 46-250](https://github.com/gpambrozio/ClaudeDocs/blob/22b170d8584c52e49bbc1db54fa957f9bba13b47/docs-md/claude-code/quickstart.md?plain=1#L46-L250)] [[Source](https://code.claude.com/docs/en/quickstart#step-1-install-claude-code)]

#### [statusline](https://github.com/gpambrozio/ClaudeDocs/blob/22b170d8584c52e49bbc1db54fa957f9bba13b47/docs-md/claude-code/statusline.md) [[Source](https://code.claude.com/docs/en/statusline)]

* New "Task fields" table for `subagentStatusLine` listing every field, including the new `agentType` (v2.1.293). [[lines 1095-1121](https://github.com/gpambrozio/ClaudeDocs/blob/22b170d8584c52e49bbc1db54fa957f9bba13b47/docs-md/claude-code/statusline.md?plain=1#L1095-L1121)] [[Source](https://code.claude.com/docs/en/statusline#subagent-status-lines)]
* Troubleshooting restructured into headed sections. [[lines 1132-1151](https://github.com/gpambrozio/ClaudeDocs/blob/22b170d8584c52e49bbc1db54fa957f9bba13b47/docs-md/claude-code/statusline.md?plain=1#L1132-L1151)] [[Source](https://code.claude.com/docs/en/statusline#troubleshooting)]

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/22b170d8584c52e49bbc1db54fa957f9bba13b47/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* Values in the settings `env` key are copied as written with no shell expansion, so `~` and `$HOME` stay literal. Use absolute paths. [[lines 82-83](https://github.com/gpambrozio/ClaudeDocs/blob/22b170d8584c52e49bbc1db54fa957f9bba13b47/docs-md/claude-code/env-vars.md?plain=1#L82-L83)] [[Source](https://code.claude.com/docs/en/env-vars#in-settings-files)]

Many other Claude Code pages received smaller edits, including amazon-bedrock, microsoft-foundry, claude-apps-gateway-config, cloud-environments, desktop, ide-integrations, vs-code, skills and slash-commands.

-----

## API changes

### New Documents

#### [api-credits-for-subscribers](https://github.com/gpambrozio/ClaudeDocs/blob/22b170d8584c52e49bbc1db54fa957f9bba13b47/docs-md/api/about-claude/api-credits-for-subscribers.md) [[Source](https://platform.claude.com/docs/en/about-claude/api-credits-for-subscribers)]

How Claude Max and Team plans include monthly Claude API credits. It explains how to claim them by linking a Console organization, which plans are eligible, and what the credits cover. They apply only to the Claude API in the Console, not to other platforms.

#### [browser-use-sdk](https://github.com/gpambrozio/ClaudeDocs/blob/22b170d8584c52e49bbc1db54fa957f9bba13b47/docs-md/api/agents-and-tools/tool-use/browser-use-sdk.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-sdk)]

How to run the browser use tool or computer use tool from the Python or TypeScript SDK. You subclass a toolset class and implement one method per member tool. The SDK handles routing, policies, approval callbacks and `tool_result` building. It covers the computer toolset too.

#### [event-deltas](https://github.com/gpambrozio/ClaudeDocs/blob/22b170d8584c52e49bbc1db54fa957f9bba13b47/docs-md/api/managed-agents/event-deltas.md) [[Source](https://platform.claude.com/docs/en/managed-agents/event-deltas)]

Managed Agents beta feature. Opt in with the `event_deltas[]` query parameter on the event stream to render `agent.message` text as a live preview while the model generates it. The buffered `agent.message` stays the authoritative record.

#### [session-observability](https://github.com/gpambrozio/ClaudeDocs/blob/22b170d8584c52e49bbc1db54fa957f9bba13b47/docs-md/api/managed-agents/session-observability.md) [[Source](https://platform.claude.com/docs/en/managed-agents/session-observability)]

Inspect Managed Agents sessions in the Console session viewer (timeline minimap, per-thread lanes), and read token usage and list cost to debug unexpected agent behavior.

#### [haiku-5-5/migration-guide](https://github.com/gpambrozio/ClaudeDocs/blob/22b170d8584c52e49bbc1db54fa957f9bba13b47/docs-md/api/models/haiku-5-5/migration-guide.md) [[Source](https://platform.claude.com/docs/en/models/haiku-5-5/migration-guide)]

Code changes needed to move from Claude Haiku 4.5 to Haiku 5.5.

#### [haiku-5-5/overview](https://github.com/gpambrozio/ClaudeDocs/blob/22b170d8584c52e49bbc1db54fa957f9bba13b47/docs-md/api/models/haiku-5-5/overview.md) [[Source](https://platform.claude.com/docs/en/models/haiku-5-5/overview)]

Model ID, pricing and limits for Claude Haiku 5.5.

#### [haiku-5-5/whats-new-haiku-5-5](https://github.com/gpambrozio/ClaudeDocs/blob/22b170d8584c52e49bbc1db54fa957f9bba13b47/docs-md/api/models/haiku-5-5/whats-new-haiku-5-5.md) [[Source](https://platform.claude.com/docs/en/models/haiku-5-5/whats-new-haiku-5-5)]

Haiku 5.5 targets high-volume, latency-sensitive work such as classification, routing, extraction and subagents. It supports adaptive thinking with effort and a 1M context window with up to 128k output. It uses the newer tokenizer, which counts about 30% more tokens than Haiku 4.5, and its thinking blocks work only in the account that produced them or a linked one. Includes a table of changes from Haiku 4.5 and the action each needs.

#### [prompting-claude-haiku-5-5](https://github.com/gpambrozio/ClaudeDocs/blob/22b170d8584c52e49bbc1db54fa957f9bba13b47/docs-md/api/build-with-claude/prompt-engineering/prompting-claude-haiku-5-5.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-haiku-5-5)]

Prompting guidance specific to Claude Haiku 5.5.

#### [claude-haiku-5-5](https://github.com/gpambrozio/ClaudeDocs/blob/22b170d8584c52e49bbc1db54fa957f9bba13b47/docs-md/api/release-notes/system-prompts/claude-haiku-5-5.md) [[Source](https://platform.claude.com/docs/en/release-notes/system-prompts/claude-haiku-5-5)]

Published system prompt for Claude Haiku 5.5.

### Changed documents

#### SDK reference pages

The generated per-language `api/*/beta/messages` reference pages (CLI, Ruby, Java, C#, Go and others) were regenerated with very large diffs, and the Haiku 5.5 model is likely reflected in them. They have no hand-written changes to summarize.
