# [Claude docs changes for June 23rd, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/9434d899fa2bb88f52c930838a9aa1f5dac245e7) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/9434d899fa2bb88f52c930838a9aa1f5dac245e7)]

## Executive Summary
- New `claude mcp login/logout` CLI commands let you authenticate MCP servers over SSH or without opening the interactive panel
- Shell mode `!` commands now trigger Claude to respond automatically — eliminating the need for a second prompt after running commands
- Background subagents now surface permission prompts in your main session instead of silently auto-denying tool calls
- New `plugin-relevance.md` guide explains how marketplace operators can configure Claude Code to suggest plugins based on session signals
- Computer use is no longer HIPAA eligible (corrected in the data retention table)

## New Claude Code versions

### [2.1.186](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/versions/2.1.186.md)

#### New features

* Added `claude mcp login <name>` and `claude mcp logout <name>` to authenticate MCP servers from the CLI without opening the interactive `/mcp` menu, with `--no-browser` stdin redirect support for SSH
* Added status filtering (press `f`) to the `/workflows` agent detail view
* Added a "Skills" section to the `/plugin` Installed tab
* Added `teammateMode: "iterm2"` setting for explicit iTerm2 native split panes via the `it2` CLI
* Added "Claude Platform on AWS · refresh credentials" option to `/login` when `awsAuthRefresh` is configured
* `!` bash commands now trigger Claude to respond to the output automatically; set `"respondToBashCommands": false` to keep the previous context-only behavior

#### Existing feature improvements

* Improved `claude mcp get` and `claude mcp remove` to suggest the closest configured server name on a typo
* Improved memory: the agent is now reminded to compact its `MEMORY.md` index when nearing the size limit
* Improved skill frontmatter: `display-name`, `default-enabled`, `fallback`, and `metadata.*` keys now accept kebab-case, snake_case, and camelCase
* Improved malformed `SKILL.md` YAML frontmatter handling: loads the skill body with empty metadata instead of failing silently
* Changed `CLAUDE_CODE_MAX_RETRIES` to cap at 15; for unattended sessions use `CLAUDE_CODE_RETRY_WATCHDOG` instead
* Changed background subagents to surface permission prompts in the main session instead of auto-denying; the dialog shows which agent is asking, and Esc denies just that tool
* Changed `/review <pr>` to use the same review engine as `/code-review medium`

#### Major bug fixes

* Fixed streaming requests failing with "Content block not found" or JSON parse errors after the machine wakes from sleep
* Fixed subagent transcript scroll position bleeding into the main transcript on exit
* Fixed `Agent(type)` deny rules and `Agent(x,y)` allowed-types restrictions not being enforced for named subagent spawns
* Fixed Workflow `agent({schema})` subagents looping forever on repeated schema validation failures instead of aborting after 5 attempts
* Fixed `~~strikethrough~~` showing literal tildes instead of rendering as strikethrough
* Fixed session cost not showing for usage-based Enterprise and Team subscribers
* Fixed agent teams: teammates spawned via tmux/pane backends now inherit the leader's `--effort` level

-----

## Claude Code changes

### New Documents

#### [plugin-relevance](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/claude-code/plugin-relevance.md) [[Source](https://code.claude.com/docs/en/plugin-relevance)]

New guide for marketplace operators and enterprise administrators. Explains how to add a `relevance` block to a plugin's `marketplace.json` entry so Claude Code suggests the plugin based on session signals (working directory, CLI commands run, files read, host URLs, and manifest dependencies). Covers the three suggestion surfaces (spinner tip, session-start notification, Discover tab pin), how to enable suggestions via `pluginSuggestionMarketplaces` in managed settings, field reference for all signal types, and how to validate your marketplace with `claude plugin validate`.

### Changed documents

#### [agent-sdk/python](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/claude-code/agent-sdk/python.md) [[Source](https://code.claude.com/docs/en/agent-sdk/python)]

* `CLAUDE_CODE_MAX_RETRIES` is now capped at 15; new `CLAUDE_CODE_RETRY_WATCHDOG=1` variable mentioned for unattended runs that need to retry capacity errors indefinitely. [[line 826](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/claude-code/agent-sdk/python.md?plain=1#L826)] [[Source](https://code.claude.com/docs/en/agent-sdk/python#handle-slow-or-stalled-api-responses)]

#### [agent-sdk/typescript](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* `CLAUDE_CODE_MAX_RETRIES` is now capped at 15; new `CLAUDE_CODE_RETRY_WATCHDOG=1` variable mentioned for unattended runs. [[line 464](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L464)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#handle-slow-or-stalled-api-responses)]

#### [agent-teams](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/claude-code/agent-teams.md) [[Source](https://code.claude.com/docs/en/agent-teams)]

* Added `iterm2` as a new `teammateMode` value (v2.1.186): uses iTerm2 native split panes via the `it2` CLI and shows an error with the install command if `it2` is missing. [[line 94](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/claude-code/agent-teams.md?plain=1#L94)] [[Source](https://code.claude.com/docs/en/agent-teams#choose-a-display-mode)]

#### [claude-platform-on-aws](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/claude-code/claude-platform-on-aws.md) [[Source](https://code.claude.com/docs/en/claude-platform-on-aws)]

* Removed the marketing banner/contact-sales block at the top of the page.
* Added documentation that with `awsAuthRefresh` configured, `/login` shows a "Claude Platform on AWS · refresh credentials" option that re-reads AWS credentials without restarting Claude Code. [[line 40](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/claude-code/claude-platform-on-aws.md?plain=1#L40)] [[Source](https://code.claude.com/docs/en/claude-platform-on-aws#1-configure-aws-credentials)]

#### [cli-reference](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* Added `claude mcp login <name>` and `claude mcp logout <name>` commands to the reference table, including `--no-browser` flag for SSH use. [[lines 25-26](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/claude-code/cli-reference.md?plain=1#L25-L26)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-commands)]
* Added `iterm2` as a valid value for `--teammate-mode` (added in v2.1.186). [[line 105](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/claude-code/cli-reference.md?plain=1#L105)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-flags)]

#### [commands](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/claude-code/commands.md) [[Source](https://code.claude.com/docs/en/commands)]

* Clarified that `/review` runs the same engine as `/code-review` on a GitHub pull request (not a deeper cloud-based review). [[line 13](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/claude-code/commands.md?plain=1#L13)] [[Source](https://code.claude.com/docs/en/commands#commands-across-a-typical-workflow)]
* Updated `/review [PR]` description: now accepts a PR number, lists open PRs with no arguments, and uses the `/code-review` engine. [[line 96](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/claude-code/commands.md?plain=1#L96)] [[Source](https://code.claude.com/docs/en/commands#all-commands)]

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* `CLAUDE_CODE_CONNECT_TIMEOUT_MS` is now marked as removed in v2.1.186 (now a no-op); `API_TIMEOUT_MS` should be used instead. [[line 148](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/claude-code/env-vars.md?plain=1#L148)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* Added `CLAUDE_CODE_FORCE_STRIKETHROUGH` env var (v2.1.186): forces strikethrough rendering when terminal supports it but is not auto-detected. [[line 204](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/claude-code/env-vars.md?plain=1#L204)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* `CLAUDE_CODE_MAX_RETRIES` is now documented as capped at 15 (v2.1.186). [[line 207](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/claude-code/env-vars.md?plain=1#L207)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* Added `CLAUDE_CODE_RETRY_WATCHDOG`: set to `1` in unattended sessions to retry 429/529 capacity errors indefinitely instead of failing after `CLAUDE_CODE_MAX_RETRIES`. Requires v2.1.186. [[line 239](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/claude-code/env-vars.md?plain=1#L239)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* Updated `CLAUDE_CODE_FORCE_SESSION_PERSISTENCE` to note that the tmux case is auto-detected since v2.1.178 and to mention `screen` sessions as another use case. [[line 203](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/claude-code/env-vars.md?plain=1#L203)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* Added `Waiting for API response · will retry in` to the error lookup table. [[line 35](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/claude-code/errors.md?plain=1#L35)] [[Source](https://code.claude.com/docs/en/errors#find-your-error)]
* Documented the 20-second stall detection threshold (v2.1.185+; was 10 seconds in earlier versions) that shows the "Waiting for API response" banner before any retry. [[line 55](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/claude-code/errors.md?plain=1#L55)] [[Source](https://code.claude.com/docs/en/errors#automatic-retries)]
* Added `CLAUDE_CODE_RETRY_WATCHDOG` to the retry tuning table. [[line 62](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/claude-code/errors.md?plain=1#L62)] [[Source](https://code.claude.com/docs/en/errors#automatic-retries)]

#### [interactive-mode](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* Shell mode `!` description updated: Claude now responds automatically to command output (v2.1.186). [[line 71](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/claude-code/interactive-mode.md?plain=1#L71)] [[Source](https://code.claude.com/docs/en/interactive-mode#quick-commands)]
* Added note explaining the new auto-response behavior, how to disable it with `respondToBashCommands: false`, and that before v2.1.186 shell mode always added output to context without a response. [[line 270](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/claude-code/interactive-mode.md?plain=1#L270)] [[Source](https://code.claude.com/docs/en/interactive-mode#shell-mode-with-prefix)]

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Added new "Authenticate from the command line" section documenting `claude mcp login <name>` and `claude mcp logout <name>`, including `--no-browser` for SSH connections. [[lines 473-491](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/claude-code/mcp.md?plain=1#L473-L491)] [[Source](https://code.claude.com/docs/en/mcp#authenticate-from-the-command-line)]

#### [monitoring-usage](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* Updated `CLAUDE_CODE_MAX_RETRIES` description to note the cap at 15. [[line 967](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/claude-code/monitoring-usage.md?plain=1#L967)] [[Source](https://code.claude.com/docs/en/monitoring-usage#detect-retry-exhaustion)]

#### [permissions](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/claude-code/permissions.md) [[Source](https://code.claude.com/docs/en/permissions)]

* Clarified that `--add-dir` loads both `.claude/settings.json` and `.claude/settings.local.json` (not just plugin settings). [[line 320](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/claude-code/permissions.md?plain=1#L320)] [[Source](https://code.claude.com/docs/en/permissions#additional-directories-grant-file-access-not-configuration)]

#### [plugin-marketplaces](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/claude-code/plugin-marketplaces.md) [[Source](https://code.claude.com/docs/en/plugin-marketplaces)]

* Added `relevance` as a new marketplace-specific plugin field (requires v2.1.152+), with a link to the new `plugin-relevance.md` guide. [[line 214](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/claude-code/plugin-marketplaces.md?plain=1#L214)] [[Source](https://code.claude.com/docs/en/plugin-marketplaces#optional-plugin-fields)]
* Clarified that some git servers (e.g., AWS CodeCommit) do not support fetching commits by SHA, so the `ref` must still exist on those servers. [[line 248](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/claude-code/plugin-marketplaces.md?plain=1#L248)] [[Source](https://code.claude.com/docs/en/plugin-marketplaces#plugin-sources)]

#### [settings](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* Added `respondToBashCommands` setting (v2.1.186): controls whether Claude responds after a `!` shell command runs; default `true`. [[line 261](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/claude-code/settings.md?plain=1#L261)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]
* Added `iterm2` as a valid `teammateMode` value (v2.1.186). [[line 276](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/claude-code/settings.md?plain=1#L276)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]

#### [skills](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)]

* Added note that malformed YAML frontmatter causes Claude Code to load the skill body with empty metadata (so the skill still works via `/skill-name`) and that `--debug` reveals the parse error. [[line 767](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/claude-code/skills.md?plain=1#L767)] [[Source](https://code.claude.com/docs/en/skills#skill-not-triggering)]

#### [sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* Updated background subagents behavior (v2.1.186): permission prompts now surface in the main session naming the requesting subagent; Esc denies that one tool call without stopping the subagent. Before v2.1.186, background subagents auto-denied any tool call that would have prompted. [[line 674](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/claude-code/sub-agents.md?plain=1#L674)] [[Source](https://code.claude.com/docs/en/sub-agents#run-subagents-in-foreground-or-background)]
* Clarified that `SendMessage` is always available for resuming subagents by agent ID or name; structured team-protocol messages require agent teams to be enabled. [[line 762](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/claude-code/sub-agents.md?plain=1#L762)] [[Source](https://code.claude.com/docs/en/sub-agents#resume-subagents)]

#### [tools-reference](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/claude-code/tools-reference.md) [[Source](https://code.claude.com/docs/en/tools-reference)]

* Updated `SendMessage` description: no longer requires `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` for resuming subagents by agent ID; structured team-protocol messages still require agent teams. [[line 32](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/claude-code/tools-reference.md?plain=1#L32)] [[Source](https://code.claude.com/docs/en/tools-reference)]
* Updated background subagent tool permission behavior description to match v2.1.186 changes. [[line 91](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/claude-code/tools-reference.md?plain=1#L91)] [[Source](https://code.claude.com/docs/en/tools-reference#agent-tool-behavior)]

#### [ultrareview](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/claude-code/ultrareview.md) [[Source](https://code.claude.com/docs/en/ultrareview)]

* Updated comparison table to include `/code-review` as a distinct option: now shows all three commands (`/code-review`, `/review <pr>`, `/code-review ultra`) with their targets, depth, duration, cost, and best-use. [[lines 82-92](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/claude-code/ultrareview.md?plain=1#L82-L92)] [[Source](https://code.claude.com/docs/en/ultrareview#how-ultrareview-compares-to-/code-review-and-/review)]

#### [workflows](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/claude-code/workflows.md) [[Source](https://code.claude.com/docs/en/workflows)]

* Added `f` key shortcut to filter the agent list in the selected phase by status in the `/workflows` progress view. [[line 96](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/claude-code/workflows.md?plain=1#L96)] [[Source](https://code.claude.com/docs/en/workflows#watch-the-run)]

-----

## API changes

### Changed documents

#### [agents-and-tools/tool-use/define-tools](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/api/agents-and-tools/tool-use/define-tools.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools)]

* Updated model recommendation from Opus 4.7 to Opus 4.8 for complex tools and ambiguous queries. [[line 9](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/api/agents-and-tools/tool-use/define-tools.md?plain=1#L9)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools)]
* Added a full multi-language code example (with language tabs) for forcing tool use with `tool_choice`, replacing the previous single-line snippet. [[line 138](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/api/agents-and-tools/tool-use/define-tools.md?plain=1#L138)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools)]

#### [agents-and-tools/tool-use/handle-tool-calls](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/api/agents-and-tools/tool-use/handle-tool-calls.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls)]

* Added `search_result` as a valid content block type for tool results (alongside `text`, `image`, and `document`). [[line 30](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/api/agents-and-tools/tool-use/handle-tool-calls.md?plain=1#L30)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls)]

#### [agents-and-tools/tool-use/strict-tool-use](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/api/agents-and-tools/tool-use/strict-tool-use.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/strict-tool-use)]

* Added a "Next steps" card section linking to web fetch tool, tool use with prompt caching, structured outputs, and define tools. [[line 121](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/api/agents-and-tools/tool-use/strict-tool-use.md?plain=1#L121)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/strict-tool-use)]

#### [api/cli/beta/messages/batches/results](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/api/api/cli/beta/messages/batches/results.md) [[Source](https://platform.claude.com/docs/en/api/cli/beta/messages/batches/results)]

* Page restored from a "Console temporarily unavailable" error state to the full CLI reference for retrieving Message Batch results, including parameters and response schema.

#### [build-with-claude/batch-processing](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/api/build-with-claude/batch-processing.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/batch-processing)]

* Added "Next steps" cards linking to search results and prompt caching.

#### [build-with-claude/extended-thinking](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/api/build-with-claude/extended-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]

* Restructured supported models list into a table showing `budget_tokens` support, recommended thinking mode, per model. [[line 101](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/api/build-with-claude/extended-thinking.md?plain=1#L101)] [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]
* Added Claude Fable 5 and Claude Mythos 5 to the interleaved thinking support table; added Claude Haiku 4.5 (not supported) and clarified earlier Claude 4 models. [[line 217](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/api/build-with-claude/extended-thinking.md?plain=1#L217)] [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]
* Updated max output tokens: Claude Sonnet 4.6 now supports 128k (was 64k). [[line 144](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/api/build-with-claude/extended-thinking.md?plain=1#L144)] [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]
* Replaced per-model comparison text with a condensed table covering `budget_tokens`, thinking output, interleaved thinking, and block preservation. [[line 242](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/api/build-with-claude/extended-thinking.md?plain=1#L242)] [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]
* Added "Adaptive thinking" to the "Next steps" section. [[line 267](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/api/build-with-claude/extended-thinking.md?plain=1#L267)] [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]

#### [build-with-claude/fast-mode](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/api/build-with-claude/fast-mode.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/fast-mode)]

* Added that fast mode is compatible with streaming (where the OTPS gain is most visible). [[line 39](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/api/build-with-claude/fast-mode.md?plain=1#L39)] [[Source](https://platform.claude.com/docs/en/build-with-claude/fast-mode)]
* Clarified that fast mode does not silently fall back to standard speed on rate limits — it returns a `429` or `529` instead. [[line 316](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/api/build-with-claude/fast-mode.md?plain=1#L316)] [[Source](https://platform.claude.com/docs/en/build-with-claude/fast-mode)]

#### [build-with-claude/handling-stop-reasons](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/api/build-with-claude/handling-stop-reasons.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons)]

* Added a quick-reference table at the top mapping each `stop_reason` value to when it occurs and what to do. [[line 12](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/api/build-with-claude/handling-stop-reasons.md?plain=1#L12)] [[Source](https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons)]
* Added `stop_details: null` to the example response for `end_turn`. [[line 44](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/api/build-with-claude/handling-stop-reasons.md?plain=1#L44)] [[Source](https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons)]
* Clarified that `model_context_window_exceeded` is currently only typed in the SDKs' `beta` namespace and requires `client.beta.messages`; added which models support it natively vs. via a beta header. [[line 236](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/api/build-with-claude/handling-stop-reasons.md?plain=1#L236)] [[Source](https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons)]
* Added "Next steps" cards linking to refusals/fallback, tool runner, streaming, and errors. [[line 512](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/api/build-with-claude/handling-stop-reasons.md?plain=1#L512)] [[Source](https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons)]

#### [build-with-claude/refusals-and-fallback](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/api/build-with-claude/refusals-and-fallback.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback)]

* Changed the primary code example from TypeScript to multi-language tabs (Python shown by default). [[line 20](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/api/build-with-claude/refusals-and-fallback.md?plain=1#L20)] [[Source](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback)]

#### [build-with-claude/search-results](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/api/build-with-claude/search-results.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/search-results)]

* Added "Next steps" cards linking to citations, web search tool, Messages API reference, and prompt caching. [[line 537](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/api/build-with-claude/search-results.md?plain=1#L537)] [[Source](https://platform.claude.com/docs/en/build-with-claude/search-results)]

#### [manage-claude/api-and-data-retention](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/api/manage-claude/api-and-data-retention.md) [[Source](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention)]

* Computer use is no longer HIPAA eligible — changed from "Yes" to "No" in the HIPAA column of the feature eligibility table. [[line 175](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/api/manage-claude/api-and-data-retention.md?plain=1#L175)] [[Source](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention)]

#### [test-and-evaluate/strengthen-guardrails/handle-streaming-refusals](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/api/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals.md) [[Source](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals)]

* Replaced guidance to reset context with recommendation to retry on a fallback model using server-side fallback or SDK middleware. [[line 47](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/api/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals.md?plain=1#L47)] [[Source](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals)]
* Added "Migration notes" section covering: refusals arrive as HTTP 200 (not errors), newer models include `stop_details`, retry on a different model, check batch results for refusals, and centralize on `stop_reason`. [[line 105](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/api/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals.md?plain=1#L105)] [[Source](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals)]
* Added "Next steps" cards. [[line 128](https://github.com/gpambrozio/ClaudeDocs/blob/9434d899fa2bb88f52c930838a9aa1f5dac245e7/docs-md/api/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals.md?plain=1#L128)] [[Source](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals)]
